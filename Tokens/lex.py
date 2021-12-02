import sys
from token import Token
from tokenstype import *
from token import *

class Lexer: 
    def __init__(self, input) -> None:
        self.source=input
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    def nextChar(self):
        self.curPos+=1;
        if self.curPos >= len(self.source):
            self.curChar = '\0'
        else: 
            self.curChar = self.source[self.curPos]
    
    ##anticipa el caracter que sigue
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos + 1]

    #muestra el error si hay tokens invalidos
    def abort(self, message):
        sys.exit("Error de Lexico" + message)

    #saltarse los espacios en blanco
    def skipWhiteSpace(self):
        while self.curChar == ' ' or self.curChar== '\t' or self.curChar == '\r':
            self.nextChar()

    #skip comments
    def skipComments(self):
        if self.curChar == '/':
            while self.curChar != '\n':
                self.nextChar()
    
    #obtiene el token siguiente
    def getToken(self):
        self.skipWhiteSpace()
        self.skipComments()
        token=None
        #checar primero si el primer caracter +=
        if self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)
        elif self.curChar == '=':
            if self.peek()== '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(self.curChar, TokenType.EQEQ)
            else:
                token = Token(self.curChar, TokenType.EQ)

        elif self.curChar == '>':
            if self.peek()== '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(self.curChar, TokenType.GTEQ)
            else:
                token = Token(self.curChar, TokenType.GT)

        elif self.curChar == '<':
            if self.peek()== '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(self.curChar, TokenType.LTEQ)
            else:
                token = Token(self.curChar, TokenType.LT)
        elif self.curChar == '!':
            if self.peek()== '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(self.curChar, TokenType.NOTEQ)
            else:
                self.abort("se esperaba un != y escribiste un !"+self.peek())

        elif self.curChar == '\"':
            startPos = self.curPos
            while self.curChar != '\"':
                if self.curChar == '\r' or self.curChar == '\t' or self.curChar == '\n' or self.curChar == '\\' or self.curChar == '%':
                    self.abort("caracter no valido en el string")
                self.nextChar()

            tokenText = self.source[startPos: self.curPos]
            token = Token(tokenText, TokenType.STRING)

        elif self.curChar.isdigit():
            startPos=self.curPos
            while self.peek().isdigit():
                self.nextChar()
            if self.peek() == '.':
                self.nextChar()
                if not self.peek().isdigit():
                    self.abort("caracter no valido en el numero")

                while self.peek().isdigit():
                    self.nextChar()
            tokenText = self.source[startPos: self.curPos+1]
            token = Token(tokenText, TokenType.NUMBER)
        
        elif self.curChar.isalpha():
            startPos=self.curPos
            while self.peek().isalnum():
                self.nextChar()
            tokenText = self.source[startPos: self.curPos+1]
            keyword = Token.checkIfKeyword(tokenText)
            if keyword==None:
                token = Token(tokenText, TokenType.IDENT)
            else:
                token = Token(tokenText, keyword)
        elif self.curChar == '\n':
            token = Token(self.curChar, TokenType.NEWLINE)
        elif self.curChar == '\0':
            token = Token(self.curChar, TokenType.EOF)
        else: 
            self.abort("Token desconocido"+ self.curChar)

        self.nextChar()
        return token;




            
            
    