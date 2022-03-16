# Generated from c:\Users\IGNACIO\Desktop\CompiladoresTarea1\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete generic visitor for a parse tree produced by marzoParser.

class marzoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by marzoParser#program.
    def visitProgram(self, ctx:marzoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#suma.
    def visitSuma(self, ctx:marzoParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#division.
    def visitDivision(self, ctx:marzoParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#multiplicacion.
    def visitMultiplicacion(self, ctx:marzoParser.MultiplicacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#smaller.
    def visitSmaller(self, ctx:marzoParser.SmallerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#smallereq.
    def visitSmallereq(self, ctx:marzoParser.SmallereqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#equals.
    def visitEquals(self, ctx:marzoParser.EqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#letras.
    def visitLetras(self, ctx:marzoParser.LetrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#greatereq.
    def visitGreatereq(self, ctx:marzoParser.GreatereqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#primaria.
    def visitPrimaria(self, ctx:marzoParser.PrimariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#resta.
    def visitResta(self, ctx:marzoParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#greater.
    def visitGreater(self, ctx:marzoParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#if.
    def visitIf(self, ctx:marzoParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#asignacion.
    def visitAsignacion(self, ctx:marzoParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#declaracion.
    def visitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#print.
    def visitPrint(self, ctx:marzoParser.PrintContext):
        return self.visitChildren(ctx)



del marzoParser