from rply import LexerGenerator

def get_lexer(filename = "tokens.txt",variables = []):
    lexer = LexerGenerator()
    with open(filename,"r") as f:
        raw = [i.split() for i in f.read().splitlines() if (not i.startswith("//")) and (not len(i) == 0)]

    for i in variables:
        lexer.add("VAR",i)

    for i in raw:
        if i[0] == "IGNORE":
            lexer.ignore(i[1])
        else:
            lexer.add(i[0],i[1])
    
    return lexer.build()