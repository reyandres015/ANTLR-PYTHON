from antlr4 import *
from dist.calculadoraPrimeroSumaLexer import calculadoraPrimeroSumaLexer
from dist.calculadoraPrimeroSumaParser import calculadoraPrimeroSumaParser
from dist.calculadoraPrimeroSumaVisitor import calculadoraPrimeroSumaVisitor


class EvalVisitor(calculadoraPrimeroSumaVisitor):
    def __init__(self):
        self.memory = {}

    # Métodos visit
    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return value

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitAssign(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == calculadoraPrimeroSumaParser.MUL:
            return left * right
        else:
            return left / right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == calculadoraPrimeroSumaParser.ADD:
            return right + left
        else:
            return right - left

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitFloat(self, ctx):
        return float(ctx.FLOAT().getText())

    def visitId(self, ctx):
        var_name = ctx.ID().getText()
        if var_name in self.memory:
            return self.memory[var_name]
        return 0

    def visitBool(self, ctx):
        if ctx.getText() == 'true':
            return True
        else:
            return False

    def visitUnary(self, ctx):
        if ctx.getChild(0).getText() == '!':
            return not self.visit(ctx.expr())
        elif ctx.getChild(0).getText() == '-':
            return -self.visit(ctx.expr())

    def visitIncrement(self, ctx):
        return self.visit(ctx.expr()) + 1
    def visitDecrement(self, ctx):
        return self.visit(ctx.expr()) - 1


def main():
    input_stream = FileStream("ejemplo.txt")
    lexer = calculadoraPrimeroSumaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = calculadoraPrimeroSumaParser(token_stream)
    tree = parser.prog()

    eval_visitor = EvalVisitor()
    eval_visitor.visit(tree)


if __name__ == '__main__':
    main()
