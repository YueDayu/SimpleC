import parserc.parser_entry as parser
import sys


if __name__ == '__main__':
    # print(parserc.parser_entry.parsec(sys.argv[1]))
    print(parser.parsec(sys.argv[1]).toStringTree())
