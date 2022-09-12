grammar prueba;

/*
YAPL Syntax
*/
start:
    program
    ;

program:
    classSpecification ';' program
    | EOF
    ;

classSpecification:
    CLASS TYPE (INHERITS TYPE)? '{' (feature ';')* '}'
    ;

feature:
    ID '(' (formal (',' formal)*)* ')' ':' TYPE '{' expr '}'
    | ID ':' TYPE ( ASSIGNMENT expr )?
    ;

formal:
    ID ':' TYPE
    ;

declaration:
    ID ':' TYPE ( ASSIGNMENT expr )?
    ;

expr:
    ID ASSIGNMENT expr                                                                        # Asignacion
    | expr ('@' TYPE)? '.' ID '(' ( expr (',' expr)* )* ')'                                   # LlamadaMetodoDeClase
    | ID '(' ( expr (',' expr)* )* ')'                                                        # LlamadaFuncion
    | IF expr THEN expr ELSE expr FI                                                          # IfElse
    | WHILE expr LOOP expr POOL                                                               # While
    | '{' (expr ';') + '}'                                                                    # Llaves
    | LET declaration (',' declaration)* IN expr                                              # Let
    | NEW TYPE                                                                                # NewInstancia
    | ISVOID expr                                                                             # Void
    | expr ADD expr                                                                           # Sumar
    | expr MINUS expr                                                                         # Restar
    | expr MULT expr                                                                          # Multiplicar
    | expr DIV expr                                                                           # Dividir
    | '~' expr                                                                                # NotMenos
    | expr LT expr                                                                            # MenorQue
    | expr LE expr                                                                            # MenorIgualQue
    | expr EQ expr                                                                            # IgualQue
    | NOT expr                                                                                # Not
    | '('expr')'                                                                              # Parenthesis
    | ID                                                                                      # Identifier
    | INT                                                                                     # Integer
    | STR                                                                                     # String
    | TRUE                                                                                    # True
    | FALSE                                                                                   # False
    ;


/*
Reserved words
*/

CLASS: C L A S S;
ELSE: E L S E ;
TRUE: 'true';
FALSE: 'false';
FI: F I ;
IF: I F ;
IN: I N ;
INHERITS: I N H E R I T S;
ISVOID: I S V O I D ;
LOOP: L O O P ;
POOL: P O O L ;
THEN: T H E N ;
WHILE: W H I L E ;
NEW: N E W ;
NOT: N O T ;
LET: L E T ;


/*
TYPES
*/
INT: [0-9]+;
ID: [a-z]([a-zA-Z0-9]|'_')*;
TYPE: [A-Z]([a-zA-Z0-9]|'_')*;
SELF: 'self';
SELF_TYPE: 'SELF_TYPE';
STR: '"' .*? '"';


/*
ASSIGNATIONS & OPERATORS
*/
ASSIGNMENT: '<-' ;
ADD: '+' ;
MINUS: '-' ;
MULT: '*' ;
DIV: '/' ;
LT: '<' ;
LE: '<=' ;
EQ: '=' ;


/*
Case insensitive fragments
*/
fragment A: [Aa];
fragment B: [Bb];
fragment C: [Cc];
fragment D: [Dd];
fragment E: [Ee];
fragment F: [Ff];
fragment G: [Gg];
fragment H: [Hh];
fragment I: [Ii];
fragment J: [Jj];
fragment K: [Kk];
fragment L: [Ll];
fragment M: [Mm];
fragment N: [Nn];
fragment O: [Oo];
fragment P: [Pp];
fragment Q: [Qq];
fragment R: [Rr];
fragment S: [Ss];
fragment T: [Tt];
fragment U: [Uu];
fragment V: [Vv];
fragment W: [Ww];
fragment X: [Xx];
fragment Y: [Yy];
fragment Z: [Zz];

/*
COMMENTS
*/
START_COMMENT: '(*';
END_COMMENT: '*)';
COMMENT: START_COMMENT (COMMENT | .)*? END_COMMENT -> skip;
LINE_COMMENT: '--' (~ '\n')* '\n'? -> skip;

/*
WHITESPACES
*/
WHITESPACE: [ \t\r\n\f\\] + -> skip;




