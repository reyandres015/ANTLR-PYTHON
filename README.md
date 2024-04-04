# ANTLR-Python

Con la calculadora realizada en ANTLR y teniendo como lenguaje objetivo python, realizar las pruebas necesarias sobre: Asociatividad, Precedencia de Operadores, Operadores U-narios. Defina el tipo de datos bool para usar operadores U-narios.

## Asociatividad

La calculadora implementada puede realizar las operaciones con una asociatividad tanto por izquierda como por derecha.

## Precencia de operadores
En la calculadora implementada se puede cambiar la jerarquia de calculo de los operadores. Es decir, permitir que la suma se realice primero que la multiplicación. Esto se realiza simplemente cambiando el orden en que se declaran las reglas de las expresiones.

### Primero suma
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

### Primero multiplicación
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


# Calculator Execute

## Step 1: Install python runtime

```bash
pip3 install antlr4-python3-runtime
```

## Step 2: use `.g4` to generate parser and lexer 

```bash
antlr4 -Dlanguage=Python3 Calculantlr.g4 -visitor -o dist 
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
