import ply.lex as lex

tokens = (
    'LANGLE',   # <
    'LANGLESLASH',  # </
    'RANGLE',   # >
    'EQUAL',    # =,
    'STRING',   # "hello"
    'WORD',     # Welcome!
)

states = (
    ('htmlcomment', 'exclusive'),   # exclusive indicates when its a htmlcomment dont do anything else
)

t_ignore = ' ' # shortcut for whitespace

def t_htmlcomment(token):
    r'<!--'
    token.lexer.begin('htmlcomment')    # enter the htmlcomment mode exclusively

def t_htmlcomment_end(token):
    r'-->'
    # add the linenos if it were multi line comments
    token.lexer.lineno += token.value.count('\n')
    token.lexer.begin('INITIAL')    # go back to parsing the regular tokens

def t_htmlcomment_error(token):
    # anything in between the html comments
    token.lexer.skip(1)     # like pass but gathers everything in between in one token to keep track of line nos

def t_error(token):
    print "Illegal character '%s'" %token.value[0]
    token.lexer.skip(1)

def t_newline(token):
    r'\n'
    token.lexer.lineno += 1
    pass

def t_LANGLESLASH(token):
    r'</'
    return token

def t_LANGLE(token):
    r'<'
    return token

def t_RANGLE(token):
    r'>'
    return token

def t_EQUAL(token):
    r'='
    return token

def t_STRING(token):
    r'"[^"]*"'
    #remove the quotes from the string before storing them
    token.value = token.value[1:-1]
    return token

def t_WORD(token):
    r'[^ <>\n]+'
    return token


#webpage = '"This" is <b>my</b> webpage!'
#webpage = """Tricky "string" <i>output</i>!"""
#webpage =   """
#            Line1
#            Line2
#            """
webpage = "Hello <!-- comment here --> all"
html_lexer = lex.lex()
html_lexer.input(webpage)

# print the tokens parsed by the html_lexer
while True:
    tok = html_lexer.token() # get the next token
    if not tok:
        break
    else:
        print tok
