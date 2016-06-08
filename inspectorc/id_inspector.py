from parserc.SimpleCListener import *


def get_rule_name(node):
    if hasattr(node, 'getRuleIndex'):
        return SimpleCParser.ruleNames[node.getRuleIndex()]
    else:
        return 'None'


class TreeChecker(SimpleCListener):
    def __init__(self):
        self.paramTable = {}
        self.current_layer = 0
        self.function_name_flag = 0
        self.error = 0
        self.errorMsg = ''

    def delete_from_tabel(self):
        for param in self.paramTable:
            if self.current_layer in self.paramTable[param]:
                self.paramTable[param].__delitem__(self.current_layer)

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
            self.errorMsg += ('existed: ' + name)
        else:
            self.paramTable[name][self.current_layer] = True
        if self.function_name_flag == 1:
            self.current_layer += 1
            self.function_name_flag = 0


def check_tree(tree):
    checker = TreeChecker()
    walker = ParseTreeWalker()
    walker.walk(checker, tree)
    return checker.error, checker.errorMsg
