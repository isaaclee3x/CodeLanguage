from sly import Lexer

class ProgramLexer(Lexer):
    tokens = {PLUS,MINUS,TIMES,DIVIDE,EQCO,EQ,L,G,E,ASSIGN,INT,ID,IF,ELSE,PRINT,GRAMSYNTAX}
    literals = { '(', ')', '{', '}', ';' }

    ignore = ' \t'

    @_(r'\d+')
    def INT(self,t):
        t.value = int(t.value)
        return t

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if']        = IF
    ID['else']      = ELSE
    ID['show']      = PRINT
    ID['I']         = GRAMSYNTAX
    ID['declare']   = ASSIGN
    ID['plus']      = PLUS
    ID['minus']     = MINUS
    ID['times']     = TIMES
    ID['divide']    = DIVIDE
    ID['equals']    = EQCO
    ID['equal']     = EQ
    ID['less']      = L
    ID['greater']   = G
    ID['orr']       = GRAMSYNTAX
    ID['to']        = GRAMSYNTAX
    ID['is']        = GRAMSYNTAX

    # Line number tracking    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

if __name__ == '__main__':
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