from math import *
import re
import readchar
import sys

def evaluate(expression):
    expression = "a=" + expression
    ldict = {}
    exec(expression,globals(),ldict)
    a = ldict['a']
    return a

class interpreter:
    def __init__(self,file):
        self.program,self.raw = self.read(file)
        self.variables = self.get_variables()
        self.run()

    def run(self):
        memory = []
        counter = 1
        while counter < len(self.program):
            line = self.program[counter]
            try:
                if " yoink " in line:
                    split_line = line.split(" yoink ")
                    if split_line[0].isdigit():
                        assign_to = int(split_line[0])
                    elif split_line[0] in self.variables:
                        assign_to = self.variables.index(split_line[0])
                    else:
                        index = "".join(e for e in split_line[0] if e.isalpha())
                        if index in self.variables:
                            index = self.variables.index(index)
                        for i in range(split_line[0].count('[')):
                            while index > len(memory) - 1:
                                memory.append(0)
                            index = memory[index]
                        assign_to = index

                    temp = split_line[1]
                    split_line[1] = ""
                    switch = True
                    for i in temp:
                        if i == "[" and switch:
                            split_line[1] = split_line[1] + " " + i
                            switch = False
                        elif i == "]" and not switch:
                            split_line[1] = split_line[1] + i + " "
                            switch = True
                        else:
                            split_line[1] = split_line[1] + i

                    split_line = split_line[1].split(' ')
                    output = []
                    for temp in split_line:
                        if temp.isdigit():
                            output.append(temp)
                        elif temp in self.variables:
                            output.append(str(self.variables.index(temp)))
                        elif temp.count('[') > 0:
                            index = "".join(e for e in temp if e.isalpha())
                            if index in self.variables:
                                index = self.variables.index(index)
                            index = int(index)
                            while index > len(memory) - 1:
                                memory.append(0)
                            for i in range(temp.count('[')):
                                index = memory[index]
                            output.append(str(index))
                        else:
                            output.append(temp)

                    value = ""
                    for i in output:
                        value = value + " " + i

                    value = value[1:]
                    value = evaluate(value)
                    while assign_to > len(memory) - 1:
                        memory.append(0)
                    memory[assign_to] = value

                elif line[0:5] == "yeet ":
                    split_line = line.split(" ")
                    if split_line[1].isdigit():
                        output = int(split_line[1])
                    elif split_line[1] in self.variables:
                        output = self.variables.index(split_line[1])
                    else:
                        index = "".join(e for e in split_line[1] if e.isalpha())
                        if index in self.variables:
                            index = self.variables.index(index)
                        index = int(index)
                        while index > len(memory) - 1:
                            memory.append(0)
                        for i in range(split_line[1].count('[')):
                            index = memory[index]
                        output = index
                    while output > len(memory) - 1:
                        memory.append(0)
                    print(chr(int(memory[output])),end="")

                elif line [0:5] == "yote ":
                    split_line = line.split(" ")[::-1]
                    if split_line[0].isdigit():
                        output = int(split_line[0])
                    elif split_line[0] in self.variables:
                        output = self.variables.index(split_line[0])
                    else:
                        index = "".join(e for e in split_line[0] if e.isalpha())
                        if index in self.variables:
                            index = self.variables.index(index)
                        index = int(index)
                        while index > len(memory) - 1:
                            memory.append(0)
                        for i in range(split_line[0].count('[')):
                            index = memory[index]
                        output = index
                    while output > len(memory) - 1:
                        memory.append(0)
                    memory[output] = ord(readchar.readchar().decode())

                elif " yeequals " in line or " yeeter " in line or " yoinker " in line:
                    jumps = line.split("; ")
                    temp = ""
                    switch = True
                    for i in jumps[0]:
                        if i == "[" and switch:
                            temp = temp + " " + i
                            switch = False
                        elif i == "]" and not switch:
                            temp = temp + i + " "
                        else:
                            temp = temp + i
                    jumps = jumps[1:]
                    split_line = temp.split(" ")
                    output = ""
                    for i in split_line:
                        if i in self.variables:
                            index = self.variables.index(i)
                            while index > len(memory) - 1:
                                memory.append(0)
                            output = output + " " + str(memory[index])
                        elif "[" in i:
                            index = "".join(e for e in i if e.isalpha())
                            if index in self.variables:
                                index = self.variables.index(index)
                            index = int(index)
                            while index > len(memory) - 1:
                                memory.append(0)
                            for e in range(i.count('[')):
                                index = memory[index]
                            output = output + " " + str(memory[index])
                        elif i == "yeequals":
                            output = output + " == "
                        elif i == "yeeter":
                            output = output + " > "
                        elif i == "yoinker":
                            output = output + " < "
                        else:
                            output = output + " " + i
                    output = output[1:]
                    jump_to = jumps[not evaluate(output)]
                    if not jump_to in self.program:
                        sys.exit()
                    counter = 0
                    while not self.program[counter] == jump_to:
                        counter += 1
            except:
                self.throw(line)
            counter += 1

    def throw(self,line):
        print("")
        print("")
        print("#################################################")
        print("ERROR IN LINE",self.raw.index(line)+1)
        print("   " + line)
        sys.exit()

    def get_variables(self):
        variables = self.program[0].split(';')
        return variables

    def read(self,file):
        output = []
        raw = []
        with open(file,'r') as f:
            for line in f.read().splitlines():
                if not line == "":
                    output.append(line)
                raw.append(line)
        return output,raw

args = sys.argv[:]
try:
    interpreter(args[1])
except:
    pass
