from parserc.SimpleCListener import *


def get_rule_name(node):
    if hasattr(node, 'getRuleIndex'):
        return SimpleCParser.ruleNames[node.getRuleIndex()]
    else:
        return 'None'


def is_id(name):
    if name.find('\'') != -1 or name.find('\"') != -1:
        return False
    try:
        float(name)
        return False
    except ValueError:
        return True


class TreeChecker(SimpleCListener):
    def __init__(self):
        self.paramTable = {}
        self.current_layer = 0
        self.function_name_flag = 0
        self.error = 0
        self.errorMsg = ''
        self.ignored_symbol = ['printf']

    def delete_from_tabel(self):
        delete_list = []
        for param in self.paramTable:
            if self.current_layer in self.paramTable[param]:
                self.paramTable[param].__delitem__(self.current_layer)
            if len(self.paramTable[param]) == 0:
                delete_list.append(param)
        for x in delete_list:
            if x in self.paramTable:
                self.paramTable.__delitem__(x)

    def enterFunctionDefinition(self, ctx):
        self.function_name_flag = 1
        self.current_layer += 1

    def exitFunctionDefinition(self, ctx):
        self.delete_from_tabel()
        self.current_layer -= 1

    def enterStatement(self, ctx):
        self.current_layer += 1

    def exitStatement(self, ctx):
        self.delete_from_tabel()
        self.current_layer -= 1

    def enterDirectDeclarator(self, ctx):
        if get_rule_name(ctx.children[0]) != 'None':
            return
        if self.function_name_flag == 1:
            self.current_layer -= 1
        name = ctx.children[0].getText()
        if name not in self.paramTable:
            self.paramTable[name] = {}
        if self.current_layer in self.paramTable[name]:
            self.error += 1
            self.errorMsg += ('existed: ' + name + '\n')
        else:
            self.paramTable[name][self.current_layer] = True
        if self.function_name_flag == 1:
            self.current_layer += 1
            self.function_name_flag = 0

    def enterPrimaryExpression(self, ctx:SimpleCParser.PrimaryExpressionContext):
        name = ctx.getText()
        if is_id(name) and not name in self.ignored_symbol:
            if name not in self.paramTable:
                self.error += 1
                self.errorMsg += ('undeclared identifier: ' + name + '\n')
            else:
                for i in range(0, self.current_layer):
                    if i in self.paramTable[name] and not self.paramTable[name][i]:
                        self.error += 1
                        self.errorMsg += ('undeclared identifier: ' + name + '\n')


def check_tree(tree):
    checker = TreeChecker()
    walker = ParseTreeWalker()
    walker.walk(checker, tree)
    return checker.error, checker.errorMsg
