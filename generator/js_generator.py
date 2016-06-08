from parserc.SimpleCListener import *


function_strlen = """function strlen(ch) {
  return ch.length;
}\n"""
function_printf = """function printf(str) {
  if (arguments.length > 1)
    console.log(str, arguments[1]);
  else
    console.log(str);
}\n"""
function_run = "main();"


def get_rule_name(node):
    if hasattr(node, 'getRuleIndex'):
        return SimpleCParser.ruleNames[node.getRuleIndex()]
    else:
        return 'None'


class JsGenerator(object):
    def __init__(self):
        self.result = ''
        self.current_layer = 0

    def get_space(self):
        return '  ' * self.current_layer

    def get_all_node(self, rule_name, root, is_skip=True):
        result = []
        if not hasattr(root, 'children'):
            return result
        for i in root.children:
            if is_skip:
                if get_rule_name(i) == rule_name:
                    result.append(i)
                else:
                    result += self.get_all_node(rule_name, i)
            else:
                if get_rule_name(i) == rule_name:
                    result.append(i)
                result += self.get_all_node(rule_name, i)
        return result

    def deal_with_inline_expression(self, node):
        """
        deal with the inline expression(the minimum unit to translate). For example, if (node)
        :param node:
        :return:
        """
        self.result += (node.getText())

    def deal_with_expression(self, node):
        """
        deal with an independent expression, end with a \n
        :param node:
        :return:
        """
        self.result += (self.get_space() + node.getText() + ';\n')

    def deal_with_block_item(self, node):
        new_node = node.children[0]
        name = get_rule_name(new_node)
        if name == 'declaration':
            self.deal_with_declaration(new_node)
        else:
            self.deal_with_statement(new_node)

    def deal_with_block_item_list(self, node):
        if len(node.children) == 1:
            self.deal_with_block_item(node.children[0])
        else:
            self.deal_with_block_item_list(node.children[0])
            self.deal_with_block_item(node.children[1])

    def deal_with_labeled_statement(self, node):
        print('labeledStatement')

    def deal_with_compound_statement(self, node): # 大括号语句
        self.result += '{ \n'
        if len(node.children) == 3:
            self.current_layer += 1
            self.deal_with_block_item_list(node.children[1])
            self.current_layer -= 1
        self.result += (self.get_space() + '} \n')

    def deal_with_expression_statement(self, node):
        flag = False
        if len(self.result[self.result.rfind('\n'):].strip()) > 2:
            self.result += '\n'
            self.current_layer += 1
            flag = True
        self.deal_with_expression(node.children[0])
        if flag:
            self.current_layer -= 1

    def deal_with_selection_statement(self, node): # if else (else if 是拼凑而成)
        if str(node.children[0]) == 'if':
            if len(self.result[self.result.rfind('\n'):].strip()) < 1:
                self.result += self.get_space()
            self.result += 'if ('
            self.deal_with_inline_expression(node.children[2])
            self.result += ') '
            self.deal_with_statement(node.children[4])
            if len(node.children) > 5:
                self.result += (self.get_space() + 'else ')
                self.deal_with_statement(node.children[6])
        else:
            print('not support yet')

    def deal_with_iteration_statement(self, node): # for & while
        temp_name = str(node.children[0])
        self.result += self.get_space()
        if temp_name == 'while':
            self.result += 'while ('
            self.deal_with_inline_expression(node.children[2])
            self.result += ')'
            self.deal_with_statement(node.children[4])
        elif temp_name == 'do':
            print('not support yet')
        else:
            self.result += 'for ('
            i = 2
            while str(node.children[i]) != ')':
                if get_rule_name(node.children[i]) == 'expression':
                    self.deal_with_inline_expression(node.children[i])
                else:
                    self.result += '; '
                i += 1
            self.result += ')'
            self.deal_with_statement(node.children[-1])

    def deal_with_jump_statement(self, node):
        self.result += (self.get_space() + node.getText().replace('return', 'return ') + '\n')

    def deal_with_statement(self, node):
        new_node = node.children[0]
        name = get_rule_name(new_node)
        if name == 'compoundStatement':
            self.deal_with_compound_statement(new_node)
        elif name == 'expressionStatement':
            self.deal_with_expression_statement(new_node)
        elif name == 'selectionStatement':
            self.deal_with_selection_statement(new_node)
        elif name == 'iterationStatement':
            self.deal_with_iteration_statement(new_node)
        elif name == 'jumpStatement':
            self.deal_with_jump_statement(new_node)
        else:
            print('Error! not support')

    def deal_with_declaration(self, node, new_line=True):
        if new_line:
            self.result += (self.get_space() + 'var ')
        else:
            self.result += 'var '
        init_declarator_nodes = self.get_all_node('initDeclarator', node)
        for ctx in init_declarator_nodes:
            if len(ctx.children) > 1:
                self.result += (ctx.getText() + ', ').replace('[]', '')
            else:
                if ctx.getText().find('[') > -1:
                    node = ctx.children[0].children[0]
                    self.result += (node.children[0].getText() + '=new Array(' + node.children[2].getText() + '), ')
                else:
                    self.result += (ctx.getText() + ', ')
        self.result = self.result[0:-2]
        if new_line:
            self.result += ';\n'

    def deal_with_function_definition(self, node):
        self.result += 'function '
        function_name = node.children[1].children[0].children[0].getText()
        self.result += function_name
        self.result += '('
        declarator_nodes = self.get_all_node('declarator', node.children[1].children[0].children[2])
        for (i, ctx) in enumerate(declarator_nodes):
            self.result += ctx.getText().replace('[]', '')
            if i != len(declarator_nodes) - 1:
                self.result += ', '
        self.result += ') '
        self.deal_with_compound_statement(node.children[-1])

    def deal_with_external_declaration(self, node):
        new_node = node.children[0]
        name = get_rule_name(new_node)
        if name == 'functionDefinition':
            self.deal_with_function_definition(new_node)
        elif name == 'declaration':
            self.deal_with_declaration(new_node)
        else:
            print('Delete useless stray.')

    def deal_with_translation_unit(self, node):
        for i in node.children:
            name = get_rule_name(i)
            if name == 'translationUnit':
                self.deal_with_translation_unit(i)
            else:
                self.deal_with_external_declaration(i)

    def deal_with_compilation_unit(self, node):
        for i in node.children:
            name = get_rule_name(i)
            if name == 'translationUnit':
                self.deal_with_translation_unit(i)
            elif name == 'None':
                print('translate finished!')
            else:
                print('Error.')
        self.result += function_printf
        self.result += function_strlen
        self.result += function_run

    def save_to_file(self, filename):
        fout = open(filename, 'w')
        fout.write(self.result)
        fout.close()
