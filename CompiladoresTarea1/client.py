from antlr4 import *
from antlr.marzoParser import marzoParser
from antlr.marzoLexer import marzoLexer
from listeners.gencode import GenCode

import sys


def main():
    # Ignacio Alvarado Reyes A01656149
    parser = marzoParser(CommonTokenStream(marzoLexer(FileStream("input.txt"))))
    tree = parser.program()

    ifParser = marzoParser(CommonTokenStream(marzoLexer(FileStream("inputIf.txt"))))
    ifTree = ifParser.program()

    gencode = GenCode()
    walker = ParseTreeWalker()
    walker.walk(gencode, tree)
    print("")
    print("Compiling If sentence")
    walker.walk(gencode, ifTree)


if __name__ == '__main__':
    main()