from grammar.pruebaVisitor import pruebaVisitor
from grammar.pruebaParser import pruebaParser

"""
Custom visitor to generate syntax tree
"""

from antlr4 import *

class CustomVisitor(pruebaVisitor):

    tableSymbol = []

    def iterTable(self, table, dictionary):
        for i in dictionary:
            if i not in table:
                table.append(dictionary)
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
        
        nameClass = ctx.TYPE()[0].getText()
        listFeatures = []
        for i in ctx.feature():
            feature = self.visit(i)
            listFeatures.append(feature)

        print(ctx.TYPE()[0].getPayload().line)
        line = ctx.TYPE()[0].getPayload().line
        print(ctx.TYPE()[0].getPayload().column)
        column = ctx.TYPE()[0].getPayload().column
        # print(features)
        entryTableSymbol.append({"id":nameClass, "parent":parent, "line":line, "column":column, "sizeMemory":None, "positionMemory":None})
        # print(entryTableSymbol)
        self.iterTable(self.tableSymbol, entryTableSymbol)
        # print()
        # print(dir(ctx.TYPE()))
        # print()
        # print(dir(ctx.TYPE(0)))
        # print()
        # print(nameClass)
        # print(len(ctx.TYPE()))
        print(self.tableSymbol)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#feature.
    def visitFeature(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#formal.
    def visitFormal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#declaration.
    def visitDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#NewInstancia.
    def visitNewInstancia(self, ctx):
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#While.
    def visitWhile(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#String.
    def visitString(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#False.
    def visitFalse(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Integer.
    def visitInteger(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Multiplicar.
    def visitMultiplicar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Dividir.
    def visitDividir(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Not.
    def visitNot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Parenthesis.
    def visitParenthesis(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Asignacion.
    def visitAsignacion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Llaves.
    def visitLlaves(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Identifier.
    def visitIdentifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Sumar.
    def visitSumar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#LlamadaFuncion.
    def visitLlamadaFuncion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Restar.
    def visitRestar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#IgualQue.
    def visitIgualQue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Let.
    def visitLet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Void.
    def visitVoid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#LlamadaMetodoDeClase.
    def visitLlamadaMetodoDeClase(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#MenorQue.
    def visitMenorQue(self, ctx):
        return self.visitChildren(ctx)



del pruebaParser