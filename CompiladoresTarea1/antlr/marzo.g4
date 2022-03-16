grammar marzo;

program : expression*statement*expression*statement;

expression : 
    expression '+' expression #suma
    | Numero                  #primaria
    | Variable                #letras
    | expression '-' expression #resta
    | expression '/' expression #division
    | expression '*' expression #multiplicacion
    | expression '>' expression #greater
    | expression '<' expression #smaller
    | expression '>=' expression #greatereq
    | expression '<=' expression #smallereq
    | expression '==' expression #equals
    ;
    
    

statement:
    'if' expression 'then' statement  'else' statement   #if
    | expression'=' expression #asignacion
    | 'int' expression         #declaracion
    | 'print('expression')' #print
    ;

Numero : [0-9]+;

Variable : [a-z]+;

WS : [ \t\n\r]+ -> skip ;