#!/usr/bin/env python3

def read_input():
    with open("input.txt") as inp:
        prog = inp.readline()
    return prog.split(',')

def init(prog):
    prog[1] = 12
    prog[2] = 2
    return prog

def get_value(pos,mode):
    if mode == '0':
        val = prog[prog[pos]]
    else:
        val = prog[pos]
    return val


def add_store(prog,pos,mode1,mode2):
    val1 = get_value(pos+1,mode1)
    val2 = get_value(pos+2,mode2)
    prog[prog[pos+3]]=val1+val2

def mul_store(prog,pos,mode1,mode2):
    val1 = get_value(pos+1,mode1)
    val2 = get_value(pos+2,mode2)
    prog[prog[pos+3]]=val1*val2

def input_op(prog,pos):
    read = input("Input:")
    prog[prog[pos+1]] = int(read)

def output(prog,pos,mode):
    print("Output:",get_value(pos+1,mode))

def run_prog(prog):
    pos = 0
    print(str(prog[pos]).zfill(5))
    while prog[pos] != 99:
        op = str(prog[pos]).zfill(5)
        try:
            if op[-2:] == '01':
                add_store(prog,pos,op[2],op[1])
                pos+=4
            elif op[-2:] == '02':
                mul_store(prog,pos,op[2],op[1])
                pos+=4
            elif op[-2:] == '03':
                input_op(prog,pos)
                pos+=2
            elif op[-2:] == '04':
                output(prog,pos,op[2])
                pos+=2
        except Exception as e: 
            print(e)
            print('Exception!!!!')
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
    run_prog(prog)
