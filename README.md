# ANTLR-Python
<div style='width:100%; display:flex; justify-content:space-around; margin-bottom:20px;'>
<img class="lozad" data-src="https://avatars0.githubusercontent.com/u/80584?s=280&v=4" src="https://avatars0.githubusercontent.com/u/80584?s=280&v=4" alt="ANTLR">
<img class="lozad" data-src="https://pluspng.com/img-png/python-logo-png-python-logo-png-and-vector-logo-img-4096x4553.png" src="https://pluspng.com/img-png/python-logo-png-python-logo-png-and-vector-logo-img-4096x4553.png" alt="Python Logo PNG - 180358" width="250">
</div>


Con la calculadora realizada en ANTLR y teniendo como lenguaje objetivo python, realizar las pruebas necesarias sobre: Asociatividad, Precedencia de Operadores, Operadores U-narios. Defina el tipo de datos bool para usar operadores U-narios.

## Asociatividad

La calculadora implementada puede realizar las operaciones con una asociatividad tanto por izquierda como por derecha. Para realizar el cambio simplemente hay que evaluar recursivamente primero el hijo derecho y luego el izquierdo, lo que cambia la asociatividad a derecha.

#### Recursividad a la derecha

```python
def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == calculadoraParser.ADD:
            return right + left
        else:
            return right - left
```

#### Recursividad a la izquierda
```python
def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == calculadoraParser.ADD:
            return left + right
        else:
            return left - right
```



## Precedencia de operadores
En la calculadora implementada se puede cambiar la jerarquia de calculo de los operadores. Es decir, permitir que la suma se realice primero que la multiplicación. Esto se realiza simplemente cambiando el orden en que se declaran las reglas de las expresiones.

#### Primero suma
```antrl
expr:   ('!'+|'-') expr             # unary
    |   expr op=('+'|'-') expr      # AddSub
    |   expr op=('*'|'/') expr      # MulDiv
    |   FLOAT                       # float
    |   INT                         # int
    |   ID                          # id
    |   '(' expr ')'                # parens
    ; 
```

#### Primero multiplicación
```antrl
expr:   ('!'+|'-') expr             # unary
    |   expr op=('*'|'/') expr      # MulDiv
    |   expr op=('+'|'-') expr      # AddSub
    |   FLOAT                       # float
    |   INT                         # int
    |   ID                          # id
    |   '(' expr ')'                # parens
    ; 
```

## Operadores unarios

'!' -> negación

'-' -> operador cambio de signo

'++' Incremento

'--' Decrecimiento


# How run this calculator?

## Step 1: Install python runtime

```bash
pip3 install antlr4-python3-runtime
```

## Step 2: use `.g4` to generate parser and lexer 

```bash
antlr4 -Dlanguage=Python3 calculadora.g4 -visitor -o dist 
```
Use `-visitor` to generate Visitor Class
Use `-o` to specify output path.

## Step 3: Create ejemplo.txt

En este archivo de texto están las operaciones que queremos realizar en la calculadora.
```bash
touch ejemplo.txt
```

## Step 4: Execute python file

```bash
python3 main.py
```

- Nicolas Bautista
- Sara Romero
- Angie Ruiz
- Ricardo Rey
