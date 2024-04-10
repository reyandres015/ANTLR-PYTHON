# ANTLR-Python
<div style='width:100%; display:flex; justify-content:space-around; margin-bottom:20px;'>
<img class="lozad" data-src="https://avatars0.githubusercontent.com/u/80584?s=280&v=4" src="https://avatars0.githubusercontent.com/u/80584?s=280&v=4" alt="ANTLR">
<img class="lozad" data-src="https://pluspng.com/img-png/python-logo-png-python-logo-png-and-vector-logo-img-4096x4553.png" src="https://pluspng.com/img-png/python-logo-png-python-logo-png-and-vector-logo-img-4096x4553.png" alt="Python Logo PNG - 180358" width="250">
</div>


Con la calculadora realizada en ANTLR y teniendo como lenguaje objetivo python, realizar las pruebas necesarias sobre: Asociatividad, Precedencia de Operadores, Operadores U-narios. Defina el tipo de datos bool para usar operadores U-narios.

## Precedencia de operadores
La precedencia de operadores hace referencia a permitir que la suma se realice primero que la multiplicación o viceversa. Esto se realiza simplemente cambiando el orden en que se declaran las reglas de las expresiones.

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

## Asociatividad


Para realizar el cambio simplemente se evaluo recursivamente primero el hijo derecho y luego el izquierdo, lo que cambia la asociatividad a derecha.

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

## Operadores unarios

'!' -> negación

'-' -> operador cambio de signo

'++' Incremento

'--' Decrecimiento


# How run this calculator?

En este proyecto se dispuso de un directorio para cada opción de precedencia ('PrimeroMultiplicacion', 'PrimeroSuma')

Para cada directorio existen dos archivos de python los cuales hacen referencia a las asociatividades (derecha, izquierda).


## Step 1: Install python runtime

```bash
pip3 install antlr4-python3-runtime
```

## Step 2: use `.g4` to generate parser and lexer 
Nos dirijimos a la carpeta 'PrimeroMultiplicacion'
```bash
cd PrimeroMultiplicacion
```
```bash
antlr4 -Dlanguage=Python3 calculadoraPrimeroMult.g4 -visitor -o dist 
```
Nos devolvemos a la carpeta raiz del proyecto
```bash
cd ..
```
Nos dirijimos a la carpeta 'PrimeroSuma'
```bash
cd PrimeroSuma
```
```bash
antlr4 -Dlanguage=Python3 calculadoraPrimeroSuma.g4 -visitor -o dist 
```
Use `-visitor` to generate Visitor Class
Use `-o` to specify output path.

## Step 3: Modify ejemplo.txt

En este archivo de texto están las operaciones que queremos realizar en la calculadora.
```bash
nano ejemplo.txt
```

## Step 4: Execute python file
Para seleccionar el archivo correcto a ejecutar se debe:

1. Seleccionar la carpeta de acuerdo a la Precedencia seleccionada.

#### Precedencia para la multiplicación

```bash
cd PrimeroMultiplicacion
```
#### Precedencia para la suma

```bash
cd PrimeroSuma
```
2. Dependiendo de la asociativdad que se requiera se debe ejecutar un archivo de python diferente.

#### Asociatividad por derecha

```bash
python3 asociatividadDerecha.py
```
#### Asociatividad por izquierda

```bash
python3 asociatividadIzquierda.py
```

# Integrantes

- Nicolas Bautista 🧑‍💻
- Sara Romero 🧑‍💻
- Angie Ruiz 🧑‍💻
- Ricardo Rey 🧑‍💻
