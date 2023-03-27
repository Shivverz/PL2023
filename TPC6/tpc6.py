import ply.lex as lex

# List of token names
tokens = (
    'ID',
    'NUM',
    'OP',
    'ATRIB',
    'TYPE',
    'PRINT',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'SEMICOLON',
    'LOOP',
    'CONDITION',
    'FUNCNAME',
    'PROGNAME',
    'EXP',
    'COMMENT',
)

# Regular expression rules for simple tokens
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_OP = r'[+\-*/]'
t_ATRIB = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_COMMA = r','
t_SEMICOLON = r';'


# Regular expression rules with actions
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_LOOP(t):
    r'(for|while)'
    return t


def t_CONDITION(t):
    r'(if|else|elif)'
    return t


def t_EXP(t):
    r'[^\s\(\)\{\}\+\-\*/=;,\[\]]+'
    return t


def t_FUNCNAME(t):
    r'function'
    return t


def t_PROGNAME(t):
    r'program'
    return t


def t_COMMENT(t):
    r'//.*'
    pass


# Reserved words
reserved = {
    'int': 'TYPE',
    'print': 'PRINT',
    'return': 'RETURN',
}

# Ignored characters
t_ignore = ' \t\n'


# Error handling rule
def t_error(t):
    print(f"Invalid character '{t.value[0]}'")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test the lexer on example code
code = """
int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
"""


code2 = """
int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
    int max = a[0]
    for i in [1..9]{
        if max < a[i] {
            max = a[i];
        }
    }
    print(max);
}
"""

lexer.input(code)

# Print the list of tokens
for token in lexer:
    print(token.type, token.value)
