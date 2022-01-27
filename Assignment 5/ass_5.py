import os
file = open("input.txt","r")
precedence=['/','*','+','-']
vars = []
op = []

def getOp():
    maxpre = 4
    for i in op:
        if precedence.index(i) < maxpre:
            maxpre = precedence.index(i)
    # print('Max:',maxpre)
    op.remove(precedence[maxpre])
    return precedence[maxpre]


def getThreeAddrCode(line):
    s = 'A'
    ptr = 1
    while len(vars) > ptr:
        pos = line.find(getOp())
        # print(pos)
        newvar = line[pos-2:pos+3]
        # print(newvar)
        line = line.replace(newvar,s)
        print(s, " = ", newvar)
        # print("Line",line)
        i = ord(s[0])
        i += 1
        s = chr(i)
        ptr += 1


def findVar(line):
    line = line.split(' ')
    for i in line:
        if i not in precedence:
            vars.append(i)

def findOp(line):
    line = line.split(' ')
    for i in line:
        if i in precedence:
            op.append(i)

for line in file:
    line = line.replace('\n',' ')
    print("Given Expression: ", line)
    findVar(line)
    findOp(line)

getThreeAddrCode(line)
    # line = line.replace('b * c','A')
    # print(line)
# print(vars)
# print(op)
# getThreeAddrCode(line)