import sys
from grammar.pruebaVisitor import pruebaVisitor
from grammar.pruebaParser import pruebaParser

"""
Custom visitor to generate syntax tree
"""

from antlr4 import *

# REF: https://docs.microsoft.com/en-us/cpp/cpp/integer-limits?view=msvc-170
# REF: https://www.javatpoint.com/java-string-max-size

MAX_SIZE_BOOL = 24
MAX_SIZE_STRING = 2147483647 
MAX_SIZE_INT = 2147483647 

class CustomVisitor(pruebaVisitor):

    tableSymbol = []

    def iterTable(self, table, dictionary):
        if dictionary not in table:
            table.append(dictionary)
            print(self.tableSymbol, "\n\n\n\n\n")
            for i in table:
                print(i)
            print("Len Table", len(self.tableSymbol))
        else:
            False
        

    # Visit a parse tree produced by pruebaParser#start.
    def visitStart(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#classSpecification.
    def visitClassSpecification(self, ctx):
        entryTableSymbol = []
        if len(ctx.TYPE()) > 1:
            parent = ctx.TYPE()[1].getText()
        else:
            parent = None
        
        text = ctx.TYPE()[0].getText()
        listFeatures = []
        for i in ctx.feature():
            feature = self.visit(i)
            listFeatures.append(feature)

        line = ctx.TYPE()[0].getPayload().line
        column = ctx.TYPE()[0].getPayload().column
        # print(features)
        entryTableSymbol.append({"id":text, "parent":parent, "line":line, "column":column, "sizeMemory":None, "positionMemory":None})
        # print(entryTableSymbol)
        self.iterTable(self.tableSymbol, entryTableSymbol)
        # print()
        # print(dir(ctx.TYPE()))
        # print()
        # print(dir(ctx.TYPE(0)))
        # print()
        # print(nameClass)
        # print(len(ctx.TYPE()))
        
        # print(self.tableSymbol)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#feature.
    def visitFeature(self, ctx):
        entryTableSymbol = []
        parent = None
        text = ctx.ID().getText()
        function_name = ctx.TYPE().getText()
        line = ctx.ID().symbol.line
        column = ctx.ID().symbol.column
        # print("Llamada a metodo", text, function_name, line, column)
        entryTableSymbol.append({"id":text, "parent":parent, "type":function_name, "line":line, "column":column, "sizeMemory":None, "positionMemory":None})
        self.iterTable(self.tableSymbol, entryTableSymbol)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#formal.
    def visitFormal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#declaration.
    def visitDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#NewInstancia.
    def visitNewInstancia(self, ctx):
        text = ctx.TYPE().getText()
        line = ctx.NEW().symbol.line
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#MenorIgualQue.
    def visitMenorIgualQue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#IfElse.
    def visitIfElse(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#NotMenos.
    def visitNotMenos(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#True.
    def visitTrue(self, ctx):
        entryTableSymbol = []
        parent = None
        text = ctx.TRUE().getText()
        line = ctx.TRUE().symbol.line
        column = ctx.TRUE().symbol.column
        # TODO: CHECK
        size = 24 # sys.getsizeof(bool(ctx.TRUE().getText()))  # Python bool is 24 bytes
        positionMemory = id(str(ctx.TRUE().getText()))
        # print("String", text, line, column, size)
        # Tabla simbolos
        entryTableSymbol.append({"id":text, "parent":parent, "line":line, "column":column, "sizeMemory":size, "positionMemory":positionMemory})
        self.iterTable(self.tableSymbol, entryTableSymbol)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#While.
    def visitWhile(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#String.
    def visitString(self, ctx):
        entryTableSymbol = []
        parent = None
        text = ctx.STR().getText()
        line = ctx.STR().symbol.line
        column = ctx.STR().symbol.column
        # TODO: CHECK
        size = len(text.encode('utf-8'))
        positionMemory = id(str(ctx.STR().getText()))
        # print("String", text, line, column, size)
        # Tabla simbolos
        entryTableSymbol.append({"id":text, "parent":parent, "line":line, "column":column, "sizeMemory":size, "positionMemory":positionMemory})
        self.iterTable(self.tableSymbol, entryTableSymbol)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#False.
    def visitFalse(self, ctx):
        entryTableSymbol = []
        parent = None
        text = ctx.FALSE().getText()
        line = ctx.FALSE().symbol.line
        column = ctx.FALSE().symbol.column
        # TODO: CHECK
        size = 24 # sys.getsizeof(bool(ctx.FALSE().getText()))  # Python bool is 24 bytes
        positionMemory = id(str(ctx.FALSE().getText()))
        # print("String", text, line, column, size)
        # Tabla simbolos
        entryTableSymbol.append({"id":text, "parent":parent, "line":line, "column":column, "sizeMemory":size, "positionMemory":positionMemory})
        self.iterTable(self.tableSymbol, entryTableSymbol)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Integer.
    def visitInteger(self, ctx):
        entryTableSymbol = []
        parent = None
        text = ctx.INT().getText()
        line = ctx.INT().symbol.line
        column = ctx.INT().symbol.column
        # TODO: Check
        size = 24   # Python int is 24 bytes
        positionMemory = id(int(ctx.INT().getText()))
        # print("Integer", text, line, column, size)
        entryTableSymbol.append({"id":text, "parent":parent, "line":line, "column":column, "sizeMemory":size, "positionMemory":positionMemory})
        self.iterTable(self.tableSymbol, entryTableSymbol)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Multiplicar.
    def visitMultiplicar(self, ctx):
        entryTableSymbol = []
        parent = None
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        line = ctx.MULT().symbol.line
        column = ctx.MULT().symbol.column
        # entryTableSymbol.append({"id":text, "parent":parent, "line":line, "column":column, "sizeMemory":size, "positionMemory":None})
        # self.iterTable(self.tableSymbol, entryTableSymbol)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Dividir.
    def visitDividir(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        line = ctx.DIV().symbol.line
        column = ctx.DIV().symbol.column
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Not.
    def visitNot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Parenthesis.
    def visitParenthesis(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Asignacion.
    def visitAsignacion(self, ctx):
        entryTableSymbol = []
        parent = None
        expression = self.visit(ctx.expr())
        text = ctx.ID().getText()
        line = ctx.ASSIGNMENT().symbol.line
        column = ctx.ASSIGNMENT().symbol.column
        # print("assignment", expression, text, line, column)
        entryTableSymbol.append({"id":text, "parent":parent, "line":line, "column":column, "sizeMemory":None, "positionMemory":None})
        self.iterTable(self.tableSymbol, entryTableSymbol)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Llaves.
    def visitLlaves(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Identifier.
    def visitIdentifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Sumar.
    def visitSumar(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        line = ctx.ADD().symbol.line
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#LlamadaFuncion.
    def visitLlamadaFuncion(self, ctx):
        # function_name = ctx.ID().getText()
        # line = ctx.ID().symbol.line
        # arguments = []
        # for expression in ctx.expr():
        #     # Appending arguments
        #     arguments.append(self.visit(expression))
        print("Llamada a Funcion") #, function_name, line, arguments)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Restar.
    def visitRestar(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        line = ctx.MINUS().symbol.line
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#IgualQue.
    def visitIgualQue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Let.
    def visitLet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Void.
    def visitVoid(self, ctx):
        print("void")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#LlamadaMetodoDeClase.
    def visitLlamadaMetodoDeClase(self, ctx):
        function_name = ctx.ID().getText()
        text = ctx.TYPE().getText()
        line = ctx.ID().symbol.line
        column = ctx.ID().symbol.column
        arguments = []
        for expression in ctx.expr():
            # Appending arguments
            arguments.append(self.visit(expression))
        print("Llamada a metodo", text, function_name, line, column)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#MenorQue.
    def visitMenorQue(self, ctx):
        return self.visitChildren(ctx)

    

del pruebaParser