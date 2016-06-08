import parserc.parser_entry as parser
from generator.js_generator import JsGenerator
import sys
from inspectorc.id_inspector import *


if __name__ == '__main__':
    tree = parser.parsec(sys.argv[1])
    error_num, error_msg = check_tree(tree)
    if error_num != 0:
        print('Error!')
        print(error_msg)
    else:
        printer = JsGenerator()
        printer.deal_with_compilation_unit(tree)
        printer.save_to_file(sys.argv[2])
