from rply.token import Token

class Program:
    def __init__(self,line,lineno):
        self.lines = [line]
        self.lineno = lineno
    
    def add(self,line):
        self.lines.append(line)
        return self
    
    def eval(self):
        out = ""
        for line in self.lines:
            out += "\t" + line.eval()
        return out

class BinOP:
    def __init__(self,op,left,right,lineno):
        self.op = op
        self.left = left
        self.right = right
        self.lineno = lineno
    
    def eval(self):
        return self.left.eval() + " " + self.op.value + " " + self.right.eval()

class Comparison:
    def __init__(self,op,left,right,jump_true,jump_false,lineno):
        self.op = op
        self.left = left
        self.right = right
        self.jump_true = jump_true
        self.jump_false = jump_false
        self.lineno = lineno

    def eval(self):
        if self.op.name == "YEEQUALS":
            op = " == "
        elif self.op.name == "YEETER":
            op = " > "
        elif self.op.name == "YOINKER":
            op = " < "
        else:
            print("FUCK")
            exit()
        out = "if (" + self.left.eval() + op + self.right.eval() + "){ goto JUMP" + self.jump_true.value + ";}else{ goto JUMP" + self.jump_false.value + ";}\n"
        return out

class Assign:
    def __init__(self,reference,expression,lineno):
        self.reference = reference
        self.expression = expression
        self.lineno = lineno

    def eval(self):
        return self.reference.eval() + " = " + self.expression.eval() + ";\n"

class Jump:
    def __init__(self,name,lineno):
        self.name = name
        self.lineno = lineno
    
    def eval(self):
        return "JUMP" + self.name.value + ":\n"

class Input:
    def __init__(self,expression,lineno):
        self.expression = expression
        self.lineno = lineno

class Output:
    def __init__(self,expression,lineno):
        self.expression = expression
        self.lineno = lineno

    def eval(self):
        return 'printf("%c",(char)' + self.expression.eval() + ");\n"
    
class OutputInt:
    def __init__(self,expression,lineno):
        self.expression = expression
        self.lineno = lineno

    def eval(self):
        return 'printf("%d",(int)' + self.expression.eval() + ");\n"
    
class OutputFloat:
    def __init__(self,expression,lineno):
        self.expression = expression
        self.lineno = lineno

    def eval(self):
        return 'printf("%f",(float)' + ".".join(self.expression.eval().split(".")[:-1]) + ".asFloat" + ");\n"

class Reference:
    def __init__(self,base,lineno):
        self.base = base
        self.lineno = lineno

    def eval(self):
        return "arr[" + self.base.eval() + "].asInt"

class Var:
    def __init__(self,name,lineno):
        self.name = name
        self.lineno = lineno

    def eval(self):
        return self.name.value + ".asInt"

class Number:
    def __init__(self,value,lineno):
        self.value = value
        self.lineno = lineno

    def eval(self):
        return self.value.value

class Char:
    def __init__(self,value,lineno):
        self.value = value
        self.lineno = lineno
    
    def eval(self):
        if self.value.value == "'\s'":
            return "' '"
        return self.value.value

class Float:
    def __init__(self,value,lineno):
        self.value = value
        self.lineno = lineno
    
    def eval(self):
        if isinstance(self.value,Number):
            return self.value.eval()
        if isinstance(self.value,Char):
            return "(float)" + self.value.eval()
        else:
            return ".".join(self.value.eval().split(".")[:-1]) + ".asFloat"