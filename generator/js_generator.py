from parserc.SimpleCListener import *


class JsGenerator(SimpleCListener):
    def __init__(self):
        self.result = ''

    # def enterFunctionDefinition(self, ctx):
    #     print('')

    def enterDeclaration(self, ctx):
        print(ctx.getText())

    # def enterDirectDeclarator(self, ctx):
    #     print(ctx.toString)
    #
    # def exitDeclaration(self, ctx):
    #     print(';')
    #
    # def exitFunctionDefinition(self, ctx):
    #     print('')

    def save_to_file(self, filename):
        f = open(filename, 'w')
        f.write(self.result)
        f.close()
