grammar calculadoraPrimeroSuma;

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;

expr:   ('!'+|'-') expr             # unary
    |   expr '++'                   # increment
    |   expr '--'                   # decrement
    |   expr op=('+'|'-') expr      # AddSub
    |   expr op=('*'|'/') expr      # MulDiv
    |   FLOAT                       # float
    |   INT                         # int
    |   ID                          # id
    |   '(' expr ')'                # parens
    ;

NOT: '!';
INCREMENT: '++';
DECREMENT: '--';

MUL :   '*' ; // Asigna un nombre de token a '*' utilizado anteriormente en la gramática
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
TAN :   'tan' ;
ID  :   [a-zA-Z]+ ;      // Coincide con identificadores
INT :   [0-9]+ ;         // Coincide con enteros
FLOAT:  [0-9]+ '.' [0-9]+ ;    // Coincide con flotantes
NEWLINE:'\r'? '\n' ;     // Retorna nuevas líneas al analizador (es una señal de fin de declaración)
WS  :   [ \t]+ -> skip ; // Ignora los espacios en blanco
