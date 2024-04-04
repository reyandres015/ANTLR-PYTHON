from antlr4 import *
from dist.calculadoraLexer import calculadoraLexer
from dist.calculadoraParser import calculadoraParser
from dist.calculadoraVisitor import calculadoraVisitor


class EvalVisitor(calculadoraVisitor):
    def __init__(self):
        self.memory = {}

    # Métodos visit aquí
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
        if ctx.op.type == calculadoraParser.MUL:
            return left * right
        else:
            return left / right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == calculadoraParser.ADD:
            return left + right
        else:
            return left - right

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitFloat(self, ctx):
        # Convertir el número de cadena a flotante
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
    # # Leer el contenido del archivo
    # with open("ejemplo.txt", "r") as file:
    #     contenido = file.read()

    # # Invertir la cadena
    # contenido_invertido = contenido[::-1]
    # contenido_invertido = contenido_invertido.replace(" ", "")

    # # Crear un archivo temporal con el contenido invertido
    # with open("ejemplo_invertido.txt", "w") as file:
    #     file.write(contenido_invertido)

    # # Crear un FileStream con el archivo invertido
    # input_stream_inverted = FileStream("ejemplo_invertido.txt")

    # # Crear el lexer utilizando el archivo invertido
    # lexer = calculadoraLexer(input_stream_inverted)

    input_stream = FileStream("ejemplo.txt")
    lexer = calculadoraLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = calculadoraParser(token_stream)
    tree = parser.prog()

    eval_visitor = EvalVisitor()
    eval_visitor.visit(tree)


if __name__ == '__main__':
    main()
