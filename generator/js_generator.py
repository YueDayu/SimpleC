from parserc.SimpleCListener import *


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

    def deal_with_labeled_statement(self, node):
        print('labeledStatement')

    def deal_with_compound_statement(self, node): # 大括号语句
        print('compoundStatement')

    def deal_with_expression_statement(self, node):
        self.deal_with_expression(node.children[0])

    def deal_with_selection_statement(self, node): # if else (else if 是拼凑而成)
        print('selectionStatement')

    def deal_with_iteration_statement(self, node): # for & while
        print('iterationStatement')

    def deal_with_jump_statement(self, node): # return
        print('jumpStatement')

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


#TODO
    def deal_with_function_definition(self, node): # 参照我下边注释掉的代码
        print('function')

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
        # add a sys function
        if self.result.find('strlen') > -1:
            self.result = 'function strlen(ch) {\n  return ch.len();\n}\n' + self.result


# class JsGenerator(SimpleCListener):
#     def __init__(self):
#         self.result = ''
#         self.parameterNum = -1
#         self.ExpressNum = 0
#         self.isDefineStrlen = False
#         self.currentLevel = 0
#         self.isShowExpression = 0
#
#     def get_space(self):
#         return '  ' * self.currentLevel
#
#     def enterDeclaration(self, ctx):
#         self.result += (self.get_space() + 'var ')
#
#     def enterInitDeclarator(self, ctx):
#         if len(ctx.children) > 1:
#             self.result += (ctx.getText() + ', ').replace('[]', '')
#         else:
#             if ctx.getText().find('[') > -1:
#                 node = ctx.children[0].children[0]
#                 self.result += (node.children[0].getText() + '=new Array(' + node.children[2].getText() + '), ')
#             else:
#                 self.result += (ctx.getText() + ', ')
#
#         if (not self.isDefineStrlen) and (self.result.find('strlen') > -1):
#             self.isDefineStrlen = True
#             self.result = 'function strlen(ch) {\n  return ch.len();\n}\n' + self.result
#
#     def exitDeclaration(self, ctx):
#         self.result = self.result[0:-2]
#         self.result += ';\n'
#
#     def deal_with_express(self, ctx):
#         self.result += (self.get_space() + ctx.getText())
#
#     # def deal_with_statement(self, ctx):
#
#
#     # def enterSelectionStatement(self, ctx):
#     #     self.result += (self.get_space() + 'if (' + ctx.children[2].getText() + ') {\n')
#     #     self.currentLevel += 1
#     #     print(SimpleCParser.ruleNames[ctx.getRuleIndex()])
#     #     self.result += (self.get_space() + ctx.children[4].getText() + '\n')
#     #     self.isShowExpression = 1
#     #
#     # def exitSelectionStatement(self, ctx):
#     #     self.currentLevel -= 1
#     #     self.result += (self.get_space() + '} \n')
#
#     # # todo
#     # def enterExpression(self, ctx):
#     #     if self.ExpressNum == 0:
#     #         print(ctx.getText())
#     #         # self.result += (ctx.getText() + '\n')
#     #     self.ExpressNum += 1
#     #
#     # def exitExpression(self, ctx):
#     #     self.ExpressNum -= 1
#
#     def enterParameterTypeList(self, ctx):
#         self.parameterNum = 0
#
#     def exitParameterTypeList(self, ctx):
#         self.parameterNum = -1
#         self.result += ') { \n'
#
#     def enterDeclarator(self, ctx):
#         if self.parameterNum >= 0:
#             if self.parameterNum >= 1:
#                 self.result += ', '
#             self.result += ctx.getText().replace('[]', '')
#             self.parameterNum += 1
#
#     def enterFunctionDefinition(self, ctx):
#         self.currentLevel += 1
#         self.result += 'function '
#         function_name = ctx.children[1].children[0].children[0].getText()
#         self.result += function_name
#         self.result += '('
#         if len(ctx.children[1].children[0].children) < 4:
#             self.result += ') { \n'
#
#     def exitFunctionDefinition(self, ctx):
#         self.currentLevel -= 1
#         self.result += '} \n'
#
#     def showRes(self):
#         print(self.result)
#
#     def save_to_file(self, filename):
#         f = open(filename, 'w')
#         f.write(self.result)
#         f.close()
