from antlr4 import *
from SimpleCLexer import SimpleCLexer
from SimpleCParser import SimpleCParser
import sys


def parsec(filename):
    input = FileStream(filename)
    lexer = SimpleCLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SimpleCParser(stream)
    tree = parser.compilationUnit()
    return tree


if __name__ == '__main__':
    print(parsec(sys.argv[1]).toStringTree())
