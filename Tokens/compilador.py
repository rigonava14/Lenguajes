import token
from window import Ui_MainWindow
from lex import * 
from tokenstype import * 
import sintaxys
#pyuic5 -x window.ui -o window.py
from PyQt5 import QtWidgets
from window import *
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,editor,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self,editor)
        self.editor =editor

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    editor = QtWidgets.QPlainTextEdit()
    editor.setStyleSheet("""QPlainTextEdit{
        color: #ccc;
        background-color: #2b2b2b;
        family-font 'consolas';
    }""")
    file=open('./Tokens/code.see')
    editor.setPlainText(file.read())
    pintar = sintaxys.PythonHighlighter(editor.document())
    window = MainWindow(editor)
    window.show()
    app.exec_()

def main():
    #input = "IF+-123123 algo-THEN"
    file = open('./Tokens/code.see')
    input = file.read()
    lexer = Lexer(input)
    token = lexer.getToken()
    cont=0
    while token.kind != TokenType.EOF:
        print("Token Type : {} , Content: {}".format(token.kind, token.text))
        token = lexer.getToken()
        cont +=1
    print("Number of tokens found: {}".format(cont))

#main()
