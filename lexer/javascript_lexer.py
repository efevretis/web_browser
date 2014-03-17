import ply.lex as lex

tokens = (
    'ANDAND',   # &&
    'COMMA',    # ,
    'DIVIDE',   # /
    'ELSE',     # else
    'EQUAL',    # =
    'EQUALEQUAL',   # ==
    'FALSE',    # false
    'FUNCTION', # function
    'GE',       # >=
    'GT',       # >
    'IDENTIFIER',   # identifier names
    'IF',       # if
    'LBRACE',   # {
    'LE',       # <=
    'LPAREN',   # (
    'LT',       # <
    'MINUS',    # -
    'NOT',      # !
    'NUMBER',   # [0-9]+
    'OROR',     # ||
    'PLUS',     # +
    'RBRACE',   # }
    'RETURN',   # return
    'RPAREN',   # )
    'SEMICOLON',    # ;
    'STRING',   # "hello"
    'TIMES',    # *
    'TRUE',     # true
    'VAR',      # var
)

states = (
    ('javascriptcomment', 'exclusive'),
)

def t_javascriptcomment(token):
    r'\/\*'
    token.lexer.begin('javascriptcomment')

def t_javascriptcomment_end(token):
    r'\*\/'
    token.lexer.lineno += token.value.count('\n')
    token.lexer.begin('INITIAL')

def t_javascriptcomment_error(token):
    token.lexer.skip(1)

def t_eolcomment(token):
    r'//.*'
    pass

t_ignore = ' \t\v\r'
t_javascriptcomment_ignore = ' \t\v\r'


def t_newline(token):
    r'\n'
    token.lexer.lineno += 1

def t_error(token):
    print "JavaScript Lexer: Illegal Character " + token.value[0]
    return token.lexer.skip(1)

def t_NOT(token):
    r'!'
    return token

def t_ANDAND(token):
    r'&&'
    return token

def t_OROR(token):
    r'\|\|'
    return token

def t_DIVIDE(token):
    r'/'
    return token

def t_TIMES(token):
    r'\*'
    return token

def t_PLUS(token):
    r'\+'
    return token

def t_MINUS(token):
    r'-'
    return token

def t_EQUALEQUAL(token):
    r'=='
    return token

def t_EQUAL(token):
    r'='
    return token

def t_COMMA(token):
    r','
    return token

def t_SEMICOLON(token):
    r';'
    return token

def t_LBRACE(token):
    r'{'
    return token

def t_RBRACE(token):
    r'}'
    return token

def t_LPAREN(token):
    r'\('
    return token

def t_RPAREN(token):
    r'\)'
    return token

def t_LE(token):
    r'<='
    return token

def t_LT(token):
    r'<'
    return token

def t_GE(token):
    r'>='
    return token

def t_GT(token):
    r'>'
    return token

def t_FALSE(token):
    r'false'
    return token

def t_TRUE(token):
    r'true'
    return token

def t_IF(token):
    r'if'
    return token

def t_ELSE(token):
    r'else'
    return token

def t_VAR(token):
    r'var'
    return token

def t_FUNCTION(token):
    r'function'
    return token

def t_RETURN(token):
    r'return'
    return token


lexer = lex.lex()

def test_lexer(input_string):
    lexer.input(input_string)
    while True:
        tok = lexer.token() # get the next token
        if not tok:
            break
        else:
            print tok

input1 = """ - !  && () * , / ; { || } + < <= = == > >= else false function if return true var"""
print test_lexer(input1)

input2 = """
if //else
=/*=*/=
true /* false
*/ return"""
print test_lexer(input2)
