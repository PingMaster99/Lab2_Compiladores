# Generated from prueba.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pruebaParser import pruebaParser
else:
    from pruebaParser import pruebaParser

# This class defines a complete generic visitor for a parse tree produced by pruebaParser.

class pruebaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pruebaParser#start.
    def visitStart(self, ctx:pruebaParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#program.
    def visitProgram(self, ctx:pruebaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#classSpecification.
    def visitClassSpecification(self, ctx:pruebaParser.ClassSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#feature.
    def visitFeature(self, ctx:pruebaParser.FeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#formal.
    def visitFormal(self, ctx:pruebaParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#declaration.
    def visitDeclaration(self, ctx:pruebaParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#NewInstancia.
    def visitNewInstancia(self, ctx:pruebaParser.NewInstanciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#MenorIgualQue.
    def visitMenorIgualQue(self, ctx:pruebaParser.MenorIgualQueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#IfElse.
    def visitIfElse(self, ctx:pruebaParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#NotMenos.
    def visitNotMenos(self, ctx:pruebaParser.NotMenosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#True.
    def visitTrue(self, ctx:pruebaParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#While.
    def visitWhile(self, ctx:pruebaParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#String.
    def visitString(self, ctx:pruebaParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#False.
    def visitFalse(self, ctx:pruebaParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Integer.
    def visitInteger(self, ctx:pruebaParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Multiplicar.
    def visitMultiplicar(self, ctx:pruebaParser.MultiplicarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Dividir.
    def visitDividir(self, ctx:pruebaParser.DividirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Not.
    def visitNot(self, ctx:pruebaParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Parenthesis.
    def visitParenthesis(self, ctx:pruebaParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Asignacion.
    def visitAsignacion(self, ctx:pruebaParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Llaves.
    def visitLlaves(self, ctx:pruebaParser.LlavesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Identifier.
    def visitIdentifier(self, ctx:pruebaParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Sumar.
    def visitSumar(self, ctx:pruebaParser.SumarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#LlamadaFuncion.
    def visitLlamadaFuncion(self, ctx:pruebaParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Restar.
    def visitRestar(self, ctx:pruebaParser.RestarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#IgualQue.
    def visitIgualQue(self, ctx:pruebaParser.IgualQueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Let.
    def visitLet(self, ctx:pruebaParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#Void.
    def visitVoid(self, ctx:pruebaParser.VoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#LlamadaMetodoDeClase.
    def visitLlamadaMetodoDeClase(self, ctx:pruebaParser.LlamadaMetodoDeClaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#MenorQue.
    def visitMenorQue(self, ctx:pruebaParser.MenorQueContext):
        return self.visitChildren(ctx)



del pruebaParser