# Generated from calculadoraPrimeroMult.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .calculadoraPrimeroMultParser import calculadoraPrimeroMultParser
else:
    from calculadoraPrimeroMultParser import calculadoraPrimeroMultParser

# This class defines a complete generic visitor for a parse tree produced by calculadoraPrimeroMultParser.

class calculadoraPrimeroMultVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calculadoraPrimeroMultParser#prog.
    def visitProg(self, ctx:calculadoraPrimeroMultParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#printExpr.
    def visitPrintExpr(self, ctx:calculadoraPrimeroMultParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#assign.
    def visitAssign(self, ctx:calculadoraPrimeroMultParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#blank.
    def visitBlank(self, ctx:calculadoraPrimeroMultParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#parens.
    def visitParens(self, ctx:calculadoraPrimeroMultParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#MulDiv.
    def visitMulDiv(self, ctx:calculadoraPrimeroMultParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#AddSub.
    def visitAddSub(self, ctx:calculadoraPrimeroMultParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#decrement.
    def visitDecrement(self, ctx:calculadoraPrimeroMultParser.DecrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#increment.
    def visitIncrement(self, ctx:calculadoraPrimeroMultParser.IncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#unary.
    def visitUnary(self, ctx:calculadoraPrimeroMultParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#id.
    def visitId(self, ctx:calculadoraPrimeroMultParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#float.
    def visitFloat(self, ctx:calculadoraPrimeroMultParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraPrimeroMultParser#int.
    def visitInt(self, ctx:calculadoraPrimeroMultParser.IntContext):
        return self.visitChildren(ctx)



del calculadoraPrimeroMultParser