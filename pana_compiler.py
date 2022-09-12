import sys
from grammar.pruebaLexer import pruebaLexer
from grammar.pruebaParser import pruebaParser

from syntax_tree.customVisitor import CustomVisitor

from test_files import *


from antlr4 import InputStream, CommonTokenStream, FileStream


def main(argv):
    """
    Compiles the code
    :param code: code to be compiled
    :return errors: the compile errors
    """

    errors = []

    # code = 

    # stream_code = InputStream(code)

    # LEXER SPECIFICATION
    # lexer = pruebaLexer(stream_code)

    # print("Algo")

    code = FileStream(argv[1])

    # print(code)

    lexer = pruebaLexer(code)

    lexer.removeErrorListeners()  # To add custom error listener
    # TODO: ADD CUSTOM ERROR LISTENER lexer.addErrorListener()
    stream = CommonTokenStream(lexer)

    # PARSER SPECIFICATION
    parser = pruebaParser(stream)
    parser.removeErrorListeners()  # To add custom error listener
    # TODO: ADD CUSTOM ERROR LISTENER parser.addErrorListener()
    tree = parser.start()

    # SEMANTIC ANALYSIS
    visitor = CustomVisitor()

    visitor.visit(tree)
    # TODO: ADD TREE VISITING ALGORITHM syntax_tree = visitor.visit(tree)

    # Type handling
    # TODO: ADD TYPE HANDLING LOGIC
    # Update symbol table
    # Build types
    # Check types

    return errors


if __name__ == '__main__':
# def main(argv):
#     # global errors
    main(sys.argv)
#     print("FINISHED COMPILER EXECUTION")
