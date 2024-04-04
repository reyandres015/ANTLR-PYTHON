# Generated from calculadora.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .calculadoraParser import calculadoraParser
else:
    from calculadoraParser import calculadoraParser

# This class defines a complete listener for a parse tree produced by calculadoraParser.
class calculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by calculadoraParser#prog.
    def enterProg(self, ctx:calculadoraParser.ProgContext):
        pass

    # Exit a parse tree produced by calculadoraParser#prog.
    def exitProg(self, ctx:calculadoraParser.ProgContext):
        pass


    # Enter a parse tree produced by calculadoraParser#printExpr.
    def enterPrintExpr(self, ctx:calculadoraParser.PrintExprContext):
        pass

    # Exit a parse tree produced by calculadoraParser#printExpr.
    def exitPrintExpr(self, ctx:calculadoraParser.PrintExprContext):
        pass


    # Enter a parse tree produced by calculadoraParser#assign.
    def enterAssign(self, ctx:calculadoraParser.AssignContext):
        pass

    # Exit a parse tree produced by calculadoraParser#assign.
    def exitAssign(self, ctx:calculadoraParser.AssignContext):
        pass


    # Enter a parse tree produced by calculadoraParser#blank.
    def enterBlank(self, ctx:calculadoraParser.BlankContext):
        pass

    # Exit a parse tree produced by calculadoraParser#blank.
    def exitBlank(self, ctx:calculadoraParser.BlankContext):
        pass


    # Enter a parse tree produced by calculadoraParser#parens.
    def enterParens(self, ctx:calculadoraParser.ParensContext):
        pass

    # Exit a parse tree produced by calculadoraParser#parens.
    def exitParens(self, ctx:calculadoraParser.ParensContext):
        pass


    # Enter a parse tree produced by calculadoraParser#MulDiv.
    def enterMulDiv(self, ctx:calculadoraParser.MulDivContext):
        pass

    # Exit a parse tree produced by calculadoraParser#MulDiv.
    def exitMulDiv(self, ctx:calculadoraParser.MulDivContext):
        pass


    # Enter a parse tree produced by calculadoraParser#AddSub.
    def enterAddSub(self, ctx:calculadoraParser.AddSubContext):
        pass

    # Exit a parse tree produced by calculadoraParser#AddSub.
    def exitAddSub(self, ctx:calculadoraParser.AddSubContext):
        pass


    # Enter a parse tree produced by calculadoraParser#unary.
    def enterUnary(self, ctx:calculadoraParser.UnaryContext):
        pass

    # Exit a parse tree produced by calculadoraParser#unary.
    def exitUnary(self, ctx:calculadoraParser.UnaryContext):
        pass


    # Enter a parse tree produced by calculadoraParser#id.
    def enterId(self, ctx:calculadoraParser.IdContext):
        pass

    # Exit a parse tree produced by calculadoraParser#id.
    def exitId(self, ctx:calculadoraParser.IdContext):
        pass


    # Enter a parse tree produced by calculadoraParser#float.
    def enterFloat(self, ctx:calculadoraParser.FloatContext):
        pass

    # Exit a parse tree produced by calculadoraParser#float.
    def exitFloat(self, ctx:calculadoraParser.FloatContext):
        pass


    # Enter a parse tree produced by calculadoraParser#int.
    def enterInt(self, ctx:calculadoraParser.IntContext):
        pass

    # Exit a parse tree produced by calculadoraParser#int.
    def exitInt(self, ctx:calculadoraParser.IntContext):
        pass


    # Enter a parse tree produced by calculadoraParser#unaryExpr.
    def enterUnaryExpr(self, ctx:calculadoraParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by calculadoraParser#unaryExpr.
    def exitUnaryExpr(self, ctx:calculadoraParser.UnaryExprContext):
        pass



del calculadoraParser