import parserc.parser_entry as parser
# import parserc.SimpleCParser as SimpleCParser
from generator.js_generator import JsGenerator
from antlr4 import *
import sys


if __name__ == '__main__':
    tree = parser.parsec(sys.argv[1])
    printer = JsGenerator()
    printer.deal_with_compilation_unit(tree)
    printer.save_to_file(sys.argv[2])
