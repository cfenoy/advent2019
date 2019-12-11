#!/usr/bin/env python3

rel_base = 0

def read_input():
    with open("input.txt") as inp:
        prog = inp.readline().rstrip()
    return prog.split(',')

def init(prog):
    prog[1] = 12
    prog[2] = 2
    return prog

def get_value(pos,mode):
    global rel_base
    if mode == '0':
        try:
            val = prog[prog[pos]]
        except:
            val = 0
    elif mode == '1':
        val = prog[pos]
    else:
        val = prog[rel_base+prog[pos]]
    return val

def get_addr(pos,mode):
    global rel_base
    if mode == '2':
        addr = rel_base+prog[pos]
    else:
        addr = prog[pos]
    return addr


def add_store(prog,pos,mode1,mode2,mode3):
    val1 = get_value(pos+1,mode1)
    val2 = get_value(pos+2,mode2)
    addr = get_addr(pos+3,mode3)
    prog[addr]=val1+val2

def mul_store(prog,pos,mode1,mode2,mode3):
    val1 = get_value(pos+1,mode1)
    val2 = get_value(pos+2,mode2)
    addr = get_addr(pos+3,mode3)
    prog[addr]=val1*val2

def input_op(prog,pos,mode):
    global rel_base
    read = input()
    addr = get_addr(pos+1,mode)
    prog[addr] = int(read)

def output(prog,pos,mode):
    print(get_value(pos+1,mode))

def jump_if_true(prog,pos,mode1,mode2):
    val1 = get_value(pos+1,mode1)
    val2 = get_value(pos+2,mode2)
    if val1 != 0:
        newpos = val2
    else:
        newpos = pos+3
    return newpos

def jump_if_false(prog,pos,mode1,mode2):
    val1 = get_value(pos+1,mode1)
    val2 = get_value(pos+2,mode2)
    if val1 == 0:
        newpos = val2
    else:
        newpos = pos+3
    return newpos

def less_than(prog,pos,mode1,mode2,mode3):
    val1 = get_value(pos+1,mode1)
    val2 = get_value(pos+2,mode2)
    addr = get_addr(pos+3,mode3)
    if val1 < val2:
        prog[addr] = 1
    else:
        prog[addr] = 0

def equals(prog,pos,mode1,mode2,mode3):
    val1 = get_value(pos+1,mode1)
    val2 = get_value(pos+2,mode2)
    addr = get_addr(pos+3,mode3)
    if val1 == val2:
        prog[addr] = 1
    else:
        prog[addr] = 0

def adjust_rel_base(prog,pos,mode1):
    global rel_base
    val1 = get_value(pos+1,mode1)
    rel_base+=val1

def run_prog(prog):
    pos = 0
    while prog[pos] != 99:
        op = str(prog[pos]).zfill(5)
        try:
            if op[-2:] == '01':
                add_store(prog,pos,op[2],op[1],op[0])
                pos+=4
            elif op[-2:] == '02':
                mul_store(prog,pos,op[2],op[1],op[0])
                pos+=4
            elif op[-2:] == '03':
                input_op(prog,pos,op[2])
                pos+=2
            elif op[-2:] == '04':
                output(prog,pos,op[2])
                pos+=2
            elif op[-2:] == '05':
                pos = jump_if_true(prog,pos,op[2],op[1])
            elif op[-2:] == '06':
                pos = jump_if_false(prog,pos,op[2],op[1])
            elif op[-2:] == '07':
                less_than(prog,pos,op[2],op[1],op[0])
                pos+=4
            elif op[-2:] == '08':
                equals(prog,pos,op[2],op[1],op[0])
                pos+=4
            elif op[-2:] == '09':
                adjust_rel_base(prog,pos,op[2])
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
    prog = {k:v for k,v in enumerate(list(map(lambda x: int(x), prog)))}
    run_prog(prog)
