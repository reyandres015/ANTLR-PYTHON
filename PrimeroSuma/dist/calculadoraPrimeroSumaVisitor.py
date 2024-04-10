# Generated from calculadoraPrimeroSuma.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .calculadoraPrimeroSumaParser import calculadoraPrimeroSumaParser
else:
    from calculadoraPrimeroSumaParser import calculadoraPrimeroSumaParser

# This class defines a complete generic visitor for a parse tree produced by calculadoraPrimeroSumaParser.

class calculadoraPrimeroSumaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calculadoraPrimeroSumaParser#prog.
    def visitProg(self, ctx:calculadoraPrimeroSumaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroSumaParser#printExpr.
    def visitPrintExpr(self, ctx:calculadoraPrimeroSumaParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroSumaParser#assign.
    def visitAssign(self, ctx:calculadoraPrimeroSumaParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroSumaParser#blank.
    def visitBlank(self, ctx:calculadoraPrimeroSumaParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroSumaParser#parens.
    def visitParens(self, ctx:calculadoraPrimeroSumaParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroSumaParser#AddSub.
    def visitAddSub(self, ctx:calculadoraPrimeroSumaParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroSumaParser#MulDiv.
    def visitMulDiv(self, ctx:calculadoraPrimeroSumaParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroSumaParser#decrement.
    def visitDecrement(self, ctx:calculadoraPrimeroSumaParser.DecrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroSumaParser#increment.
    def visitIncrement(self, ctx:calculadoraPrimeroSumaParser.IncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroSumaParser#unary.
    def visitUnary(self, ctx:calculadoraPrimeroSumaParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroSumaParser#id.
    def visitId(self, ctx:calculadoraPrimeroSumaParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroSumaParser#float.
    def visitFloat(self, ctx:calculadoraPrimeroSumaParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroSumaParser#int.
    def visitInt(self, ctx:calculadoraPrimeroSumaParser.IntContext):
        return self.visitChildren(ctx)



del calculadoraPrimeroSumaParser