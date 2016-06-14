from parserc.SimpleCListener import *
from generator.js_generator import *
from llvmlite import ir
import codecs

def parse_escape(s):
    return codecs.escape_decode(bytes(s, "ascii"))[0].decode("ascii")

class LLVMTypes(object):
    int32 = ir.IntType(32)
    int16 = ir.IntType(16)
    int8 = ir.IntType(8)
    int1 = ir.IntType(1)
    float32 = ir.FloatType()
    float64 = ir.DoubleType()
    void = ir.VoidType()
    typeStrMap = {
        "int": int32,
        "short": int16,
        "char": int8,
        "long": int32,
        "bool": int1,
        "float": float32,
        "double": float64,
        "void": void
    }

    def to_lltype(self, typeStr):
        return self.typeStrMap[typeStr]

    def get_array_type(self, elem_type, count):
        return ir.ArrayType(elem_type, count)

    def get_pointer_type(self, pointee_type):
        return ir.PointerType(pointee_type)

    def register_struct(self, name, llvm_elem_types):
        #TODO
        pass

    def to_llvm_const(self, llvm_type, value):
        if (type(value) is str):
            if llvm_type == self.int8:
                if (len(value) > 1):
                    return self.int8(ord(value[1]))
                else:
                    return llvm_type(int(value))
            elif llvm_type == self.float32 or llvm_type == self.float64:
                return llvm_type(float(value))
            elif llvm_type == self.int16 or llvm_type == self.int32:
                return llvm_type(int(value))
            elif isinstance(llvm_type, ir.ArrayType) and llvm_type.element == self.int8:
                #string
                str_val = parse_escape(value[1:-1]) + '\0'
                return ir.Constant(llvm_type, bytearray(str_val, 'ascii'))
            else:
                #TODO
                print("No known conversion: '%s' to '%s'\n" % (value, llvm_type))
        elif (type(value) is int):
            return llvm_type(value)
        else:
            return value

    def is_int(self, llvm_type):
        return isinstance(llvm_type, ir.IntType)

    def is_float(self, llvm_type):
        return llvm_type in [self.float32, self.float64]        

    def to_llvm_type(self, builder, target_type, value):
        if value.type == target_type:
            return value
        elif self.is_int(value.type) and self.is_int(target_type):
            if value.type.width < target_type.width:
                return builder.sext(value, target_type)
            elif target_type == self.int1:
                return builder.icmp_unsigned('!=', value, self.to_llvm_const(self.int1, 0))
            else:
                return builder.trunc(value, target_type)
        elif self.is_float(value.type) and self.is_float(target_type):
            if value.type == self.float32:
                return builder.fpext(value, target_type)
            else:
                return builder.fptrunc(value, target_type)
        elif self.is_float(value.type) and self.is_int(target_type):
            return builder.fptosi(value, target_type)
        elif self.is_int(value.type) and self.is_float(target_type):
            return builder.sitofp(value, target_type)
        elif type(value.type) == ir.ArrayType and type(target_type) == ir.PointerType and value.type.element == target_type.pointee:
            zero = self.to_llvm_const(self.int32, 0)
            tmp = builder.alloca(value.type)
            builder.store(value, tmp)
            return builder.gep(tmp, [zero, zero])
        elif isinstance(value.type, ir.ArrayType) and isinstance(target_type, ir.ArrayType) and value.type.element == target_type.element:
            return builder.bitcast(value, target_type)
        else:
            print("No known conversion from '%s' to '%s'\n" % (value.type, target_type))

class LLVMGenerator(JsGenerator):

    def __init__(self):
        super(JsGenerator, self).__init__()

    def emit_printf(self):
        printf_type = ir.FunctionType(self.llvmTypes.int32, (self.llvmTypes.get_pointer_type(self.llvmTypes.int8),), var_arg=True)
        printf_func = ir.Function(self.module, printf_type, "printf")
        self.localVars["printf"] = printf_func

    def deal_with_pointer(self, node, base_type):
        #TODO
        return self.llvmTypes.get_pointer_type(base_type)

    def deal_with_declarator(self, node, typeStr):
        llvm_base_type = self.llvmTypes.to_lltype(typeStr)
        for child in node.children:
            rule_name = get_rule_name(child)
            if (rule_name == 'pointer'):
                llvm_base_type = self.deal_with_pointer(child, llvm_base_type)
            elif (rule_name == 'directDeclarator'):
                res_type, res_name = self.deal_with_direct_declarator(child, llvm_base_type)
        return res_type, res_name

    def deal_with_direct_declarator(self, node, base_type):
        if not hasattr(node, 'children') or len(node.children) <= 1:
            return base_type, node.getText()
        else:
            if node.children[1].getText() == '[': #Array
                if (node.children[2].getText() != ']'):
                    array_size = int(node.children[2].getText()) #TODO: deal with expression
                    new_type = self.llvmTypes.get_array_type(elem_type=base_type, count=array_size)
                else: #Pointer in function parameter
                    new_type = self.llvmTypes.get_pointer_type(base_type)
                return self.deal_with_direct_declarator(node.children[0], new_type)
            else:
                #TODO
                print(node.getText())

    def deal_with_inline_expression(self, node):
        pass

    def deal_with_primary_expression(self, node):
        if len(node.children) == 3: #brackets
            return self.deal_with_expression(node.children[1])
        else:
            text = node.getText()
            if text[0] == "'":
                return self.llvmTypes.to_llvm_const(self.llvmTypes.int8, text)
            elif text[0].isalpha() or text[0] == '_':
                if text in self.localVars:
                    var = self.localVars[text]
                    if type(var) in [ir.Argument, ir.Function]:
                        var_val = var
                    else:
                        if (isinstance(var.type.pointee, ir.ArrayType)):
                            zero = self.llvmTypes.to_llvm_const(self.llvmTypes.int32, 0)
                            var_val = self.builder.gep(var, [zero, zero])
                        else:
                            var_val = self.builder.load(var)
                    return var_val
                else:
                    #TODO raise exception
                    print(self.module.functions)
                    print("Undefined identifier: '%s'\n" % text)
            elif text[0] == '"':
                str_len = len(parse_escape(text[1:-1]))
                return self.llvmTypes.to_llvm_const(self.llvmTypes.get_array_type(self.llvmTypes.int8, str_len + 1), text)
            else:
                return self.llvmTypes.to_llvm_const(self.llvmTypes.int32, text)

    def deal_with_argument_expression_list(self, node):
        if len(node.children) == 1:
            return [self.deal_with_assignment_expression(node.children[0])]
        else:
            args = self.deal_with_argument_expression_list(node.children[0])
            args.append(self.deal_with_assignment_expression(node.children[2]))
            return args

    def deal_with_postfix_expression(self, node):
        if get_rule_name(node.children[0]) == 'primaryExpression':
            return self.deal_with_primary_expression(node.children[0])
        elif get_rule_name(node.children[0]) == 'postfixExpression':
            lhs = self.deal_with_postfix_expression(node.children[0])
            op = node.children[1].getText()
            if op == '[':
                # Array Indexing
                array_index = self.deal_with_expression(node.children[2])
                ptr = self.builder.gep(lhs, [array_index])
                return self.builder.load(ptr)
            elif op == '(':
                #Function call
                args = self.deal_with_argument_expression_list(node.children[2]) if len(node.children) > 3 else []
                converted_args = [self.llvmTypes.to_llvm_type(self.builder, value=arg, target_type=callee_arg.type)
                    for arg, callee_arg in zip(args, lhs.args)]
                if len(converted_args) < len(args):
                    converted_args += args[len(lhs.args):]
                return self.builder.call(lhs, converted_args)
            elif op == '.':
                #TODO
                print(node.getText())
            elif op == '->':
                #TODO
                print(node.getText())
            elif op == '++':
                lhs_ptr = self.deal_with_assignment_lhs_postfix(node.children[0])
                one = self.llvmTypes.to_llvm_const(lhs.type, 1)
                res = self.builder.add(lhs, one)
                self.builder.store(res, lhs_ptr)
                return lhs
            elif op == '--':
                lhs_ptr = self.deal_with_assignment_lhs_postfix(node.children[0])
                one = self.llvmTypes.to_llvm_const(lhs.type, 1)
                res = self.builder.sub(lhs, one)
                self.builder.store(res, lhs_ptr)
                return lhs
            else:
                print("Postfix Expression: '%s'\n" % node.getText())

    def deal_with_cast_expression(self, node):
        if get_rule_name(node.children[0]) == 'unaryExpression':
            return self.deal_with_unary_expression(node.children[0])
        else:
            if node.children[0].getText() == '(':
                to_type = self.llvmTypes.to_lltype(node.children[1].getText())
                #TODO handle complex types
                val = self.deal_with_cast_expression(node.children[3])
                return self.llvmTypes.to_llvm_type(self.builder, value=val, target_type=to_type)
            else:
                #TODO
                print(node.getText())

    def deal_with_binary_expression(self, node):
        lhs = self.deal_with_value_expression(node.children[0])
        op = node.children[1].getText()
        rhs = self.deal_with_value_expression(node.children[2])
        #TODO choose appropriate type to convert oprands to
        if op == '||':
            converted_lhs = self.llvmTypes.to_llvm_type(self.builder, value=lhs, target_type=self.llvmTypes.int1)
            converted_rhs = self.llvmTypes.to_llvm_type(self.builder, value=rhs, target_type=self.llvmTypes.int1)
            return self.builder.or_(converted_lhs, converted_rhs)
        elif op == '&&':
            converted_lhs = self.llvmTypes.to_llvm_type(self.builder, value=lhs, target_type=self.llvmTypes.int1)
            converted_rhs = self.llvmTypes.to_llvm_type(self.builder, value=rhs, target_type=self.llvmTypes.int1)
            return self.builder.and_(converted_lhs, converted_rhs)
        elif op == '|':
            convert_target = lhs.type
            converted_lhs = self.llvmTypes.to_llvm_type(self.builder, value=lhs, target_type=convert_target)
            converted_rhs = self.llvmTypes.to_llvm_type(self.builder, value=rhs, target_type=convert_target)
            return self.builder.or_(converted_lhs, converted_rhs)
        elif op == '^':
            convert_target = lhs.type
            converted_lhs = self.llvmTypes.to_llvm_type(self.builder, value=lhs, target_type=convert_target)
            converted_rhs = self.llvmTypes.to_llvm_type(self.builder, value=rhs, target_type=convert_target)
            return self.builder.xor(converted_lhs, converted_rhs)
        elif op == '&':
            convert_target = lhs.type
            converted_lhs = self.llvmTypes.to_llvm_type(self.builder, value=lhs, target_type=convert_target)
            converted_rhs = self.llvmTypes.to_llvm_type(self.builder, value=rhs, target_type=convert_target)
            return self.builder.and_(converted_lhs, converted_rhs)
        elif op in ['<', '<=', '==', '!=', '>=', '>']:
            convert_target = lhs.type
            converted_lhs = self.llvmTypes.to_llvm_type(self.builder, value=lhs, target_type=convert_target)
            converted_rhs = self.llvmTypes.to_llvm_type(self.builder, value=rhs, target_type=convert_target)
            if self.llvmTypes.is_int(convert_target):
                return self.builder.icmp_signed(op, converted_lhs, converted_rhs)
            elif self.llvmTypes.is_float(convert_target):
                return self.builder.fcmp_orderde(converted_lhs, converted_rhs)
            else:
                #TODO raise exception
                print(node.getText())
        elif op == '<<':
            convert_target = lhs.type
            converted_lhs = self.llvmTypes.to_llvm_type(self.builder, value=lhs, target_type=convert_target)
            converted_rhs = self.llvmTypes.to_llvm_type(self.builder, value=rhs, target_type=convert_target)
            if self.llvmTypes.is_int(convert_target):
                return self.builder.shl(converted_lhs, converted_rhs)
            else:
                #TODO raise exception
                print(node.getText())
        elif op == '>>':
            convert_target = lhs.type
            converted_lhs = self.llvmTypes.to_llvm_type(self.builder, value=lhs, target_type=convert_target)
            converted_rhs = self.llvmTypes.to_llvm_type(self.builder, value=rhs, target_type=convert_target)
            if self.llvmTypes.is_int(convert_target):
                return self.builder.ashr(converted_lhs, converted_rhs)
            else:
                #TODO raise exception
                print(node.getText())
        elif op == '+':
            convert_target = lhs.type
            converted_lhs = self.llvmTypes.to_llvm_type(self.builder, value=lhs, target_type=convert_target)
            converted_rhs = self.llvmTypes.to_llvm_type(self.builder, value=rhs, target_type=convert_target)
            if self.llvmTypes.is_int(convert_target):
                return self.builder.add(converted_lhs, converted_rhs)
            elif self.llvmTypes.is_float(convert_target):
                return self.builder.fadd(converted_lhs, converted_rhs)
            else:
                #TODO raise exception
                print(node.getText())
        elif op == '-':
            convert_target = lhs.type
            converted_lhs = self.llvmTypes.to_llvm_type(self.builder, value=lhs, target_type=convert_target)
            converted_rhs = self.llvmTypes.to_llvm_type(self.builder, value=rhs, target_type=convert_target)
            if self.llvmTypes.is_int(convert_target):
                return self.builder.sub(converted_lhs, converted_rhs)
            elif self.llvmTypes.is_float(convert_target):
                return self.builder.fsub(converted_lhs, converted_rhs)
            else:
                #TODO raise exception
                print(node.getText())
        elif op == '*':
            convert_target = lhs.type
            converted_lhs = self.llvmTypes.to_llvm_type(self.builder, value=lhs, target_type=convert_target)
            converted_rhs = self.llvmTypes.to_llvm_type(self.builder, value=rhs, target_type=convert_target)
            if self.llvmTypes.is_int(convert_target):
                return self.builder.mul(converted_lhs, converted_rhs)
            elif self.llvmTypes.is_float(convert_target):
                return self.builder.fmul(converted_lhs, converted_rhs)
            else:
                #TODO raise exception
                print(node.getText())
        elif op == '/':
            convert_target = lhs.type
            converted_lhs = self.llvmTypes.to_llvm_type(self.builder, value=lhs, target_type=convert_target)
            converted_rhs = self.llvmTypes.to_llvm_type(self.builder, value=rhs, target_type=convert_target)
            if self.llvmTypes.is_int(convert_target):
                return self.builder.sdiv(converted_lhs, converted_rhs)
            elif self.llvmTypes.is_float(convert_target):
                return self.builder.fdiv(converted_lhs, converted_rhs)
            else:
                #TODO raise exception
                print(node.getText())
        elif op == '%':
            convert_target = lhs.type
            converted_lhs = self.llvmTypes.to_llvm_type(self.builder, value=lhs, target_type=convert_target)
            converted_rhs = self.llvmTypes.to_llvm_type(self.builder, value=rhs, target_type=convert_target)
            if self.llvmTypes.is_int(convert_target):
                return self.builder.srem(converted_lhs, converted_rhs)
            else:
                #TODO raise exception
                print(node.getText())
        else:
            #TODO raise exception
            print(lhs, op, rhs)

    def deal_with_value_expression(self, node):
        if get_rule_name(node) == 'primaryExpression':
            return self.deal_with_primary_expression(node)
        elif len(node.children) == 1:
            return self.deal_with_value_expression(node.children[0])
        else:
            rule_name = get_rule_name(node)
            if rule_name == 'postfixExpression':
                return self.deal_with_postfix_expression(node)                
            elif rule_name == 'unaryExpression':
                return self.deal_with_unary_expression(node)
            elif rule_name == 'castExpression':
                return self.deal_with_cast_expression(node)
            else:
                return self.deal_with_binary_expression(node)

    def deal_with_conditional_expression(self, node):
        if len(node.children) == 1:
            return self.deal_with_value_expression(node.children[0])
        else:
            print("Conditional Expression: '%s'\n" % node.getText())

    def deal_with_unary_expression(self, node):
        if len(node.children) == 1:
            return self.deal_with_postfix_expression(node.children[0])
        else:
            if get_rule_name(node.children[0]) == 'unaryOperator':
                #TODO
                print(node.getText())
            elif node.children[0].getText() == '++':
                lhs_ptr = self.deal_with_assignment_lhs(node.children[1])
                one = self.llvmTypes.to_llvm_const(lhs_ptr.type.pointee, 1)
                lhs = self.builder.load(lhs_ptr)
                res = self.builder.add(lhs, one)
                self.builder.store(res, lhs_ptr)
                return res
            elif node.children[0].getText() == '--':
                lhs_ptr = self.deal_with_assignment_lhs(node.children[1])
                one = self.llvmTypes.to_llvm_const(lhs_ptr.type.pointee, 1)
                lhs = self.builder.load(lhs_ptr)
                res = self.builder.sub(lhs, one)
                self.builder.store(res, lhs_ptr)
                return res
            else:
                #TODO
                print(node.getText())

    def deal_with_assignment_lhs_primary(self, node):
        if len(node.children) == 1:
            #TODO check variable declared
            return self.localVars[node.getText()]
        else:
            print("Assignment LHS must be mutable variable: '%s'" % node.getText())
            #TODO raise exception

    def deal_with_assignment_lhs_postfix(self, node):
        if len(node.children) == 1:
            return self.deal_with_assignment_lhs_primary(node.children[0])
        else:
            if node.children[1].getText() == '[': #Array index
                array_ptr = self.deal_with_assignment_lhs_postfix(node.children[0])
                array_index = self.llvmTypes.to_llvm_type(self.builder, target_type=self.llvmTypes.int32, value=self.deal_with_expression(node.children[2]))
                zero = self.llvmTypes.to_llvm_const(self.llvmTypes.int32, 0)
                if type(array_ptr) is ir.Argument:
                    array_indices = [array_index]
                else:
                    array_indices = [zero, array_index]
                res = self.builder.gep(array_ptr, array_indices)
                return res
            elif node.children[1].getText() == '.':
                #TODO
                print(node.getText())
            elif node.children[1].getText() == '->':
                #TODO
                print(node.getText())
            else:
                print("Error: Assignment LHS must be mutable: '%s'\n" % node.getText())
                #TODO raise exception

    def deal_with_assignment_lhs(self, node):
        if len(node.children) == 1:
            return self.deal_with_assignment_lhs_postfix(node.children[0])
        else:
            if get_rule_name(node.children[0]) == 'unaryOperator':
                #TODO handle pointer dereference
                print(node.getText())
            else:
                print("Error: Assignment LHS must be mutable variable: '%s'" % node.getText())
                #TODO raise exception

    def deal_with_assignment_expression(self, node):
        if len(node.children) == 1:
            return self.deal_with_conditional_expression(node.children[0])
        else:
            lhs = self.deal_with_assignment_lhs(node.children[0])
            op = node.children[1].getText()
            rhs = self.deal_with_assignment_expression(node.children[2])
            if (op == '='):
                converted_rhs = self.llvmTypes.to_llvm_type(self.builder, value=rhs, target_type=lhs.type.pointee)
                self.builder.store(converted_rhs, lhs)
                return converted_rhs
            else:
                #TODO
                print(node.getText())

    def deal_with_expression(self, node): #return: expression value
        if len(node.children) == 1:
            return self.deal_with_assignment_expression(node.children[0])
        else:
            self.deal_with_expression(node.children[0])
            return self.deal_with_assignment_expression(node.children[2])

    def deal_with_block_item(self, node):
        new_node = node.children[0]
        name = get_rule_name(new_node)
        if name == 'declaration':
            self.deal_with_declaration(new_node, is_global=False)
        else:
            self.deal_with_statement(new_node)

    def deal_with_labeled_statement(self, node):
        print(node.getText())

    def deal_with_compound_statement(self, node):
        self.deal_with_block_item_list(node.children[1])

    def deal_with_expression_statement(self, node):
        if get_rule_name(node.children[0]) == 'expression':
            self.deal_with_expression(node.children[0])

    def deal_with_selection_statement(self, node):
        if node.children[0].getText() == 'if':
            pred_expr_node = node.children[2]
            then_node = node.children[4]
            pred_val = self.deal_with_expression(pred_expr_node)
            pred = self.llvmTypes.to_llvm_type(self.builder, value=pred_val, target_type=self.llvmTypes.int1)
            if (len(node.children) > 6): # has else
                else_node = node.children[6]
                with self.builder.if_else(pred) as (then, otherwise):
                    with then:
                        self.deal_with_statement(then_node)
                    with otherwise:
                        self.deal_with_statement(else_node)
            else:
                with self.builder.if_then(pred):
                    self.deal_with_statement(then_node)
        else:
            #TODO handle switch
            print("Switch statement: '%s'" % node.getText())

    def deal_with_for_loop(self, node):
        child_idx = 2
        if get_rule_name(node.children[child_idx]) == 'expression':
            self.deal_with_expression(node.children[child_idx])
            child_idx += 2
        elif get_rule_name(node.children[child_idx]) == 'declaration':
            self.deal_with_declaration(node.children[child_idx], is_global=false)
            child_idx += 1
        else:
            child_idx += 1
        name_prefix = self.builder.block.name
        cond_block = self.builder.append_basic_block(name=name_prefix + ".loop_cond")
        loop_block = self.builder.append_basic_block(name=name_prefix + ".loop_body")
        update_block = self.builder.append_basic_block(name=name_prefix + ".loop_update")
        end_block = self.builder.append_basic_block(name=name_prefix + ".loop_end")
        last_continue = self.continue_block
        last_break = self.break_block
        self.continue_block = update_block
        self.break_block = end_block
        self.builder.branch(cond_block)
        self.builder.position_at_start(cond_block)
        if get_rule_name(node.children[child_idx]) == 'expression':
            loop_cond_val = self.deal_with_expression(node.children[child_idx])
            child_idx += 2
            converted_loop_cond = self.llvmTypes.to_llvm_type(self.builder, target_type=self.llvmTypes.int1, value=loop_cond_val)
            self.builder.cbranch(converted_loop_cond, loop_block, end_block)
        else:
            child_idx += 1
            self.builder.branch(loop_block)
        self.builder.position_at_start(update_block)
        if get_rule_name(node.children[child_idx]) == 'expression':
            self.deal_with_expression(node.children[child_idx])
            child_idx += 2
        else:
            child_idx += 1
        self.builder.branch(cond_block)
        self.builder.position_at_start(loop_block)
        self.deal_with_statement(node.children[child_idx])
        self.builder.branch(update_block)
        self.builder.position_at_start(end_block)
        self.continue_block = last_continue
        self.break_block = last_break

    def deal_with_while_loop(self, node):
        name_prefix = self.builder.block.name
        cond_block = self.builder.append_basic_block(name=name_prefix + ".while_cond")
        loop_block = self.builder.append_basic_block(name=name_prefix + ".while_body")
        end_block = self.builder.append_basic_block(name=name_prefix + ".while_end")
        last_continue, last_break = self.continue_block, self.break_block
        self.continue_block, self.break_block = cond_block, end_block
        self.builder.branch(cond_block)
        self.builder.position_at_start(cond_block)
        cond_val = self.deal_with_expression(node.children[2])
        converted_loop_cond = self.llvmTypes.to_llvm_type(self.builder, target_type=self.llvmTypes.int1, value=cond_val)
        self.builder.cbranch(converted_loop_cond, loop_block, end_block)
        self.builder.position_at_start(loop_block)
        self.deal_with_statement(node.children[4])
        self.builder.branch(cond_block)
        self.builder.position_at_start(end_block)
        self.continue_block = last_continue
        self.break_block = last_break

    def deal_with_iteration_statement(self, node):
        loop_str = node.children[0].getText()
        if loop_str == 'for':
            self.deal_with_for_loop(node)
        elif loop_str == 'while':
            self.deal_with_while_loop(node)
        else:
            #TODO
            print(node.getText())

    def deal_with_jump_statement(self, node):
        jump_str = node.children[0].getText()
        if jump_str == 'return':
            if len(node.children) > 2:
                ret_val = self.deal_with_expression(node.children[1])
                converted_val = self.llvmTypes.to_llvm_type(self.builder, target_type=self.builder.function.type.pointee.return_type, value=ret_val)
                self.builder.ret(converted_val)
            else:
                self.builder.ret_void()
        elif jump_str == 'continue':
            self.builder.branch(self.continue_block)
        elif jump_str == 'break':
            self.builder.branch(self.break_block)
        else:
            #TODO
            print(node.getText())

    def deal_with_initializer(self, node):
        if len(node.children) == 1:
            return self.deal_with_assignment_expression(node.children[0])
        else:
            #TODO
            print(node.getText())

    def deal_with_init_declarator(self, node, type_str, is_global=True):
        if len(node.children) > 1:
            init_val = self.deal_with_initializer(node.children[2])

        llvm_var_type, var_name = self.deal_with_declarator(node.children[0], type_str)
        if len(node.children) > 1:
            if isinstance(llvm_var_type, ir.PointerType) and isinstance(init_val.type, ir.ArrayType) and llvm_var_type.pointee == init_val.type.element:
                llvm_var_type = init_val.type
            converted_val = self.llvmTypes.to_llvm_type(self.builder, value=init_val, target_type=llvm_var_type)

        if is_global:
            self.localVars[var_name] = ir.GlobalVariable(self.module, llvm_var_type, name=var_name)
            self.localVars[var_name].linkage = "internal"
            if len(node.children) > 1:
                self.localVars[var_name].initializer = converted_val
        else:
            self.localVars[var_name] = self.builder.alloca(llvm_var_type)
            if len(node.children) > 1:
                self.builder.store(converted_val, self.localVars[var_name])

    def deal_with_declaration(self, node, is_global=True):
        type_str_nodes = self.get_all_node('typeSpecifier', node.children[0])
        type_str = ""
        for i in type_str_nodes:
            type_str += " " + i.getText()
        type_str = type_str.strip()
        declarator_nodes = self.get_all_node('initDeclarator', node.children[1])
        for ctx in declarator_nodes:
            self.deal_with_init_declarator(ctx, type_str, is_global)

    def deal_with_function_definition(self, node):
        ret_types = self.get_all_node('typeSpecifier', node.children[0])
        ret_type = " ".join([i.getText() for i in ret_types]).strip()
        function_name = node.children[1].children[0].children[0].getText()
        declarator_nodes = self.get_all_node('parameterDeclaration', node.children[1].children[0].children[2])
        arg_names = []
        llvm_arg_types = []
        for ctx in declarator_nodes:
            arg_type_specifiers = self.get_all_node('typeSpecifier', ctx.children[0])
            arg_type = " ".join([r.getText() for r in arg_type_specifiers]).strip()
            llvm_arg_type, arg_name = self.deal_with_declarator(ctx.children[1], arg_type)
            arg_names.append(arg_name)
            llvm_arg_types.append(llvm_arg_type)

        llvm_function_type = ir.FunctionType(self.llvmTypes.to_lltype(ret_type), llvm_arg_types)
        llvm_function = ir.Function(self.module, llvm_function_type, name=function_name)
        self.builder = ir.IRBuilder(llvm_function.append_basic_block(name="entry"))

        self.localVars[function_name] = llvm_function

        for arg_name, llvm_arg in zip(arg_names, llvm_function.args):
            self.localVars[arg_name] = llvm_arg

        self.continue_block = None
        self.break_block = None

        self.deal_with_compound_statement(node.children[-1])

        if llvm_function_type.return_type == self.llvmTypes.void:
            self.builder.ret_void()

    def deal_with_compilation_unit(self, node):
        self.llvmTypes = LLVMTypes()
        self.module = ir.Module()
        self.localVars = {}
        self.emit_printf()
        for i in node.children:
            name = get_rule_name(i)
            if name == 'translationUnit':
                self.deal_with_translation_unit(i)
            elif name == 'None':
                print('translate finished!')
            else:
                print('Error.')

    def save_to_file(self, filename):
        fout = open(filename, 'w')
        fout.write(repr(self.module))
        fout.close()
