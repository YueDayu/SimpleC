import parserc.parser_entry as parser
from generator.js_generator import JsGenerator
from antlr4 import *
import sys


if __name__ == '__main__':
    tree = parser.parsec(sys.argv[1])
    printer = JsGenerator()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    printer.save_to_file(sys.argv[2])
