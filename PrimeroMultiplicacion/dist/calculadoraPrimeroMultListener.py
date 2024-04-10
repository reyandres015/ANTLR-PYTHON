# Generated from calculadoraPrimeroMult.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .calculadoraPrimeroMultParser import calculadoraPrimeroMultParser
else:
    from calculadoraPrimeroMultParser import calculadoraPrimeroMultParser

# This class defines a complete listener for a parse tree produced by calculadoraPrimeroMultParser.
class calculadoraPrimeroMultListener(ParseTreeListener):

    # Enter a parse tree produced by calculadoraPrimeroMultParser#prog.
    def enterProg(self, ctx:calculadoraPrimeroMultParser.ProgContext):
        pass

    # Exit a parse tree produced by calculadoraPrimeroMultParser#prog.
    def exitProg(self, ctx:calculadoraPrimeroMultParser.ProgContext):
        pass


    # Enter a parse tree produced by calculadoraPrimeroMultParser#printExpr.
    def enterPrintExpr(self, ctx:calculadoraPrimeroMultParser.PrintExprContext):
        pass

    # Exit a parse tree produced by calculadoraPrimeroMultParser#printExpr.
    def exitPrintExpr(self, ctx:calculadoraPrimeroMultParser.PrintExprContext):
        pass


    # Enter a parse tree produced by calculadoraPrimeroMultParser#assign.
    def enterAssign(self, ctx:calculadoraPrimeroMultParser.AssignContext):
        pass

    # Exit a parse tree produced by calculadoraPrimeroMultParser#assign.
    def exitAssign(self, ctx:calculadoraPrimeroMultParser.AssignContext):
        pass


    # Enter a parse tree produced by calculadoraPrimeroMultParser#blank.
    def enterBlank(self, ctx:calculadoraPrimeroMultParser.BlankContext):
        pass

    # Exit a parse tree produced by calculadoraPrimeroMultParser#blank.
    def exitBlank(self, ctx:calculadoraPrimeroMultParser.BlankContext):
        pass


    # Enter a parse tree produced by calculadoraPrimeroMultParser#parens.
    def enterParens(self, ctx:calculadoraPrimeroMultParser.ParensContext):
        pass

    # Exit a parse tree produced by calculadoraPrimeroMultParser#parens.
    def exitParens(self, ctx:calculadoraPrimeroMultParser.ParensContext):
        pass


    # Enter a parse tree produced by calculadoraPrimeroMultParser#MulDiv.
    def enterMulDiv(self, ctx:calculadoraPrimeroMultParser.MulDivContext):
        pass

    # Exit a parse tree produced by calculadoraPrimeroMultParser#MulDiv.
    def exitMulDiv(self, ctx:calculadoraPrimeroMultParser.MulDivContext):
        pass


    # Enter a parse tree produced by calculadoraPrimeroMultParser#AddSub.
    def enterAddSub(self, ctx:calculadoraPrimeroMultParser.AddSubContext):
        pass

    # Exit a parse tree produced by calculadoraPrimeroMultParser#AddSub.
    def exitAddSub(self, ctx:calculadoraPrimeroMultParser.AddSubContext):
        pass


    # Enter a parse tree produced by calculadoraPrimeroMultParser#decrement.
    def enterDecrement(self, ctx:calculadoraPrimeroMultParser.DecrementContext):
        pass

    # Exit a parse tree produced by calculadoraPrimeroMultParser#decrement.
    def exitDecrement(self, ctx:calculadoraPrimeroMultParser.DecrementContext):
        pass


    # Enter a parse tree produced by calculadoraPrimeroMultParser#increment.
    def enterIncrement(self, ctx:calculadoraPrimeroMultParser.IncrementContext):
        pass

    # Exit a parse tree produced by calculadoraPrimeroMultParser#increment.
    def exitIncrement(self, ctx:calculadoraPrimeroMultParser.IncrementContext):
        pass


    # Enter a parse tree produced by calculadoraPrimeroMultParser#unary.
    def enterUnary(self, ctx:calculadoraPrimeroMultParser.UnaryContext):
        pass

    # Exit a parse tree produced by calculadoraPrimeroMultParser#unary.
    def exitUnary(self, ctx:calculadoraPrimeroMultParser.UnaryContext):
        pass


    # Enter a parse tree produced by calculadoraPrimeroMultParser#id.
    def enterId(self, ctx:calculadoraPrimeroMultParser.IdContext):
        pass

    # Exit a parse tree produced by calculadoraPrimeroMultParser#id.
    def exitId(self, ctx:calculadoraPrimeroMultParser.IdContext):
        pass


    # Enter a parse tree produced by calculadoraPrimeroMultParser#float.
    def enterFloat(self, ctx:calculadoraPrimeroMultParser.FloatContext):
        pass

    # Exit a parse tree produced by calculadoraPrimeroMultParser#float.
    def exitFloat(self, ctx:calculadoraPrimeroMultParser.FloatContext):
        pass


    # Enter a parse tree produced by calculadoraPrimeroMultParser#int.
    def enterInt(self, ctx:calculadoraPrimeroMultParser.IntContext):
        pass

    # Exit a parse tree produced by calculadoraPrimeroMultParser#int.
    def exitInt(self, ctx:calculadoraPrimeroMultParser.IntContext):
        pass



del calculadoraPrimeroMultParser