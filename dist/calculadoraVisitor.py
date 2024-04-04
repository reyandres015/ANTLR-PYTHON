# Generated from calculadora.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .calculadoraParser import calculadoraParser
else:
    from calculadoraParser import calculadoraParser

# This class defines a complete generic visitor for a parse tree produced by calculadoraParser.

class calculadoraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calculadoraParser#prog.
    def visitProg(self, ctx:calculadoraParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#printExpr.
    def visitPrintExpr(self, ctx:calculadoraParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#assign.
    def visitAssign(self, ctx:calculadoraParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#blank.
    def visitBlank(self, ctx:calculadoraParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#parens.
    def visitParens(self, ctx:calculadoraParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#MulDiv.
    def visitMulDiv(self, ctx:calculadoraParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#AddSub.
    def visitAddSub(self, ctx:calculadoraParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#unary.
    def visitUnary(self, ctx:calculadoraParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#id.
    def visitId(self, ctx:calculadoraParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#float.
    def visitFloat(self, ctx:calculadoraParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#int.
    def visitInt(self, ctx:calculadoraParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#unaryExpr.
    def visitUnaryExpr(self, ctx:calculadoraParser.UnaryExprContext):
        return self.visitChildren(ctx)



del calculadoraParser