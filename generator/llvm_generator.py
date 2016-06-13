from parserc.SimpleCListener import *
from js_generator import *
from llvmlite import ir

class LLVMTypes(object):
    int32 = ir.IntType(32)
    int16 = ir.IntType(16)
    int8 = ir.IntType(8)
    float32 = ir.FloatType()
    float64 = ir.DoubleType()
    void = ir.VoidType()
    typeStrMap = {
        "int": int32,
        "short": int16,
        "char": int8,
        "long": int32,
        "float": float32,
        "double": float64,
        "void": void
    }
    def to_lltype(typeStr):
        return typeStrMap[typeStr]

class LLVMGenerator(JsGenerator):

    def __init__(self):
        super(JsGenerator, self).__init__()

    def deal_with_inline_expression(self, node):
        pass

    def deal_with_expression(self, node):
        pass

    def deal_with_block_item(self, node):
        pass

    def deal_with_block_item_list(self, node):
        pass

    def deal_with_labeled_statement(self, node):
        pass

    def deal_with_compound_statement(self, node):
        pass

    def deal_with_expression_statement(self, node):
        pass

    def deal_with_selection_statement(self, node):
        pass

    def deal_with_iteration_statement(self, node):
        pass

    def deal_with_jump_statement(self, node):
        pass

    def deal_with_declaration(self, node, new_line=True):
        pass

    def deal_with_function_definition(self, node):
        ret_types = self.get_all_node('typeSpecifier', node.children[0])
        ret_type = ""
        for i in ret_types:
            ret_type.append(" " + i.getText())
        ret_type = ret_type.strip()
        function_name = node.children[1].children[0].children[0].getText()
        declarator_nodes = self.get_all_node('parameterDeclaration', node.children[1].children[0].children[2])
        for (i, ctx) in enumerate(declarator_nodes):
            arg_type_specifiers = self.get_all_node('typeSpecifier', ctx.children[0])
            arg_type = ""
            for r in arg_type_specifiers:
                arg_type.append(" " + i.getText())
            arg_type = arg_type.strip()
            arg_name = ctx.children[1].children[0].children[0].getText()
            

        self.deal_with_compound_statement(node.children[-1])

    def deal_with_compilation_unit(self, node):
        self.module = ir.Module()
        self.localVars = {}
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
        fout.write(repr(module))
        fout.close()
