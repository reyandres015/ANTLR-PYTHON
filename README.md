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
