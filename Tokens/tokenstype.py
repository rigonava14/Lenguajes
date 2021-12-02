import enum
class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3 
    ##KEYWORDS
    LABEL = 101
    GOTO = 102 
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    DIME = 112
    ESCANEA =113
    TEXTO = 114
    ENFRENTE = 115
    DETRAS = 116
    IZQUIERDA = 117
    DERECHA = 118
    ABAJO = 119
    ARRIBA = 120
    ENTORNO = 121
    OBJETO = 122
    COSA = 123
    PERSONA = 124
    SI = 125
    MIENTRAS = 126
    
    ##OPERADORES
    EQ= 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211
     
