from sly import Lexer

class ProgramLexer(Lexer):
    tokens = {NUMBERS, ID, PLUS, MINUS, MULTIPLY, DIVIDE, EQCO, ASSIGN, LE, LT, GE, GT, IF, ELSE, PRINT, WHILE, FOR}
    literals = { '(', ')', '{', '}', ';' }
    ignore = " \t"

    PLUS = r'\+'
    MINUS = r'-'
    MULTIPLY = r'\*'
    DIVIDE = r'/'
    EQCO = r'=='
    ASSIGN = r'='
    LE = r'<='
    LT = r'<'
    GE = r'>='
    GT = r'>'

    @_(r'\d+')
    def NUMBER(self,t):
        t.value = int(t.value)
        return t

    ID = r'[a-zA-Z][a-zA-Z0-9]*'
    ID['if'] = IF
    ID['else'] = ELSE
    ID['print'] = PRINT
    ID['while'] = WHILE
    ID['for'] = FOR

    ignore_comment = r'\#.*'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

    
if __name__ == "__main__":
    lexer = ProgramLexer()
    env = {}
    while True:
        try:
            text = input("basic > ")
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
