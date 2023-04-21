import aster as aster
from rply import ParserGenerator
from rply.token import Token

def get_parser(filename="tokens.txt"):
    with open(filename,"r") as f:
        tokens = [i.split()[0] for i in f.read().splitlines() if (not i.startswith("//")) and (not len(i) == 0)]
    if "IGNORE" in tokens:
        tokens.remove("IGNORE")
    tokens.append("VAR")
    pg = ParserGenerator(tokens, precedence=[
    ('left', ['MINUS', 'PLUS']),
    ('left', ['STAR', 'SLASH']),
    ('left', ['PERCENT'])
    ])

    @pg.production('program : line')
    def program(p):
        return aster.Program(p[0],lineno=p[0].lineno)

    @pg.production('program : program line')
    def program(p):
        return p[0].add(p[1])

    @pg.production('line : assign|comparison|jump|input|output')
    def pass_line(p):
        return p[0]
    
    @pg.production('assign : reference YOINK expression')
    @pg.production('assign : YFLOAT reference YOINK expression')
    def get_assign(p):
        if len(p) == 3:
            return aster.Assign(p[0],p[2],p[1].source_pos)
        else:
            return aster.Assign(aster.Float(p[1],p[0].source_pos),p[3],p[0].source_pos)
    
    @pg.production('comparison : expression YEEQUALS expression SEMI_COLON JUMP SEMI_COLON JUMP')
    @pg.production('comparison : expression YEETER expression SEMI_COLON JUMP SEMI_COLON JUMP')
    @pg.production('comparison : expression YOINKER expression SEMI_COLON JUMP SEMI_COLON JUMP')
    def get_comparison(p):
        return aster.Comparison(p[1],p[0],p[2],p[4],p[6],p[1].source_pos)
    
    @pg.production('jump : JUMP')
    def get_jump(p):
        return aster.Jump(p[0],p[0].source_pos)
    
    #@pg.production('float_ref : YFLOAT OPEN_PAREN reference CLOSE_PAREN')
    #def ref_as_float(p):
    #    return aster.Float(p[2],p[0].source_pos)

    @pg.production('expression : YFLOAT OPEN_PAREN expression CLOSE_PAREN')
    def expr_as_float(p):
        return aster.Float(p[2],p[0].source_pos)
    
    @pg.production('input : YOTE reference')
    def get_input(p):
        return aster.Input(p[1],p[0].source_pos)
    
    @pg.production('output : YEET reference')
    def get_output(p):
        return aster.Output(p[1],p[0].source_pos)
    
    @pg.production('output : YEET YINT reference')
    def get_output(p):
        return aster.OutputInt(p[2],p[0].source_pos)
    
    @pg.production('output : YEET YFLOAT reference')
    def get_output(p):
        return aster.OutputFloat(p[2],p[0].source_pos)
    
    @pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
    def pass_expression(p):
        return p[1]
    
    @pg.production('expression : expression PLUS expression')
    @pg.production('expression : expression MINUS expression')
    @pg.production('expression : expression STAR expression')
    @pg.production('expression : expression SLASH expression')
    @pg.production('expression : expression PERCENT expression')
    def binop(p):
        return aster.BinOP(p[1],p[0],p[2],p[1].source_pos)
    
    @pg.production('expression : reference|char|number')
    def pass_all(p):
        return p[0]
    
    @pg.production('reference : OPEN_SQUARE reference CLOSE_SQUARE')
    def get_reference(p):
        return aster.Reference(p[1],p[0].source_pos)
    
    @pg.production('reference : var')
    def pass_var(p):
        return p[0]
    
    @pg.production('var : VAR')
    def get_var(p):
        return aster.Var(p[0],p[0].source_pos)
    
    @pg.production('number : NUMBER')
    def get_number(p):
        if len(p) == 1:
            return aster.Number(p[0],p[0].source_pos)
        
    #@pg.production('number : MINUS number')
    #def negative(p):
    #    if len(p) == 2:
    #        return aster.Number(Token("NUMBER","-"+p[1].value.value),p[0].source_pos)
        
    @pg.production('char : CHAR')
    def get_char(p):
        return aster.Char(p[0],p[0].source_pos)
        
    @pg.error
    def error_handler(token):
        print("ERROR:", token, token.source_pos)
        exit()

    out = pg.build()
    #print(out.lr_table.sr_conflicts)
    return out
    