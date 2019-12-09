#!/usr/bin/env python3

def read_input():
    with open("input1.txt") as inp:
        prog = inp.readline()
    return prog.split(',')

def init(prog):
    prog[1] = 12
    prog[2] = 2
    return prog

def add_store(prog,pos):
    prog[prog[pos+3]]=prog[prog[pos+1]]+prog[prog[pos+2]]

def mul_store(prog,pos):
    prog[prog[pos+3]]=prog[prog[pos+1]]*prog[prog[pos+2]]

def run_prog(prog):
    pos = 0
    while prog[pos] != 99:
        try:
            if prog[pos] == 1:
                add_store(prog,pos)
            elif prog[pos] == 2:
                mul_store(prog,pos)
            pos+=4
        except:
            return -1
    return prog[0]

def find_inputs(prog):
    test_prog = prog.copy()
    for i in range(0,100):
        for j in range(0,100):
            test_prog[1]=i
            test_prog[2]=j
            result = run_prog(test_prog)
            if result == 19690720:
                return i*100+j
            test_prog = prog.copy()

if __name__ == "__main__":
    prog = read_input()
    prog = list(map(lambda x: int(x), prog))
    print(find_inputs(prog))
