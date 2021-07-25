from sly import Parser
from lexer import ProgramLexer

class ProgramParser(Parser):
    tokens = ProgramLexer.tokens

    literals = {'(',')','{','}','[',']'}

    @_('')
    def empty(self,p):
        pass
    

if __name__ == '__main__':
    lexer = ProgramLexer()
    parser = ProgramParser()

    while True:
        try:
            text = input('program > ')
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except EOFError:
            break