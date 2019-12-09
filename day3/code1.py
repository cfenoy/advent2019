#!/usr/bin/env python3
from pprint import pprint

def read_input():
    with open("input.txt") as inp:
        wire1 = inp.readline().rstrip().split(',')
        wire2 = inp.readline().rstrip().split(',')
    return wire1,wire2

def max_dim(wire):
    u,d,l,r=(0,0,0,0)
    mu,md,ml,mr=(0,0,0,0)
    for move in wire:
        direction,amount = (move[0],int(move[1:]))
        if direction == 'R':
            r += amount
            if r>mr:
                mr=r
            l-=amount
            print("Right:",amount)
        elif direction == 'L':
            l += amount
            if l>ml:
                ml=l
            r-=amount
            print("Left:", amount)
        elif direction == 'U':
            u += amount
            if u>mu:
                mu=u
            d-=amount
            print("Up:", amount)
        elif direction == 'D':
            d += amount
            if d>md:
                md=d
            u-=amount
            print("Down:", amount)
    return(mu,md,ml,mr)

def process_wire2(wire):
    posy = 0
    posx = 0
    positions = []
    for move in wire:
        direction,amount = (move[0],int(move[1:]))
        if direction == 'R':
            for i in range(0,amount):
                print("posx:",posx,"posy:",posy)
                positions.append((posx+1,posy))
                posx+=1
                print(i)
            print("Right:",amount)
        elif direction == 'L':
            for i in range(0,amount):
                print("posx:",posx,"posy:",posy)
                positions.append((posx-1,posy))
                posx-=1
                print(i)
            for i in range(0,amount):
                print(i)
            print("Left:", amount)
        elif direction == 'U':
            for i in range(0,amount):
                print("posx:",posx,"posy:",posy)
                positions.append((posx,posy-1))
                posy-=1
                print(i)
            for i in range(0,amount):
                print(i)
            print("Up:", amount)
        elif direction == 'D':
            for i in range(0,amount):
                print("posx:",posx,"posy:",posy)
                positions.append((posx,posy+1))
                posy+=1
                print(i)
            for i in range(0,amount):
                print(i)
            print("Down:", amount)
    return positions

def process_wire(wire,opoint,matrix):
    posy = opoint[0]
    posx = opoint[1]
    for move in wire:
        direction,amount = (move[0],int(move[1:]))
        if direction == 'R':
            for i in range(0,amount):
                print("posx:",posx,"posy:",posy)
                matrix[posy][posx+1] = 1
                posx+=1
                print(i)
            print("Right:",amount)
        elif direction == 'L':
            for i in range(0,amount):
                print("posx:",posx,"posy:",posy)
                matrix[posy][posx-1] = 1
                posx-=1
                print(i)
            for i in range(0,amount):
                print(i)
            print("Left:", amount)
        elif direction == 'U':
            for i in range(0,amount):
                print("posx:",posx,"posy:",posy)
                matrix[posy-1][posx] = 1
                posy-=1
                print(i)
            for i in range(0,amount):
                print(i)
            print("Up:", amount)
        elif direction == 'D':
            for i in range(0,amount):
                print("posx:",posx,"posy:",posy)
                matrix[posy+1][posx] = 1
                posy+=1
                print(i)
            for i in range(0,amount):
                print(i)
            print("Down:", amount)

def print_matrix(matrix):
    print('\n'.join([''.join(['{:1}'.format(item) for item in row])
        for row in matrix]))

def sum_matrix(X,Y):
    result = [[X[i][j] + Y[i][j]  for j in range
        (len(X[0]))] for i in range(len(X))]
    return result

def distance(c,o):
    print(c,o)
    print(abs(c[0]-o[0])+abs(c[1]-o[1]))
    return abs(c[0]-o[0])+abs(c[1]-o[1])

def find_closest2(crosses):
    dist = []
    for cross in crosses:
        dist.append(abs(cross[0])+abs(cross[1]))
    return min(dist)

def find_closest(opoint,matrix):
    crosses = [(index, row.index(2)) for index, row in enumerate(matrix) if 2 in row]
    print("Crosses:",crosses)
    dist = []
    for cross in crosses:
        dist.append(distance(cross,opoint))
    return min(dist)


if __name__ == "__main__":
    wire1,wire2 = read_input()	
    print(wire1,wire2)
    mu1,md1,ml1,mr1 = max_dim(wire1)
    mu2,md2,ml2,mr2 = max_dim(wire2)
    mu,md,ml,mr = (max(mu1,mu2)*2,max(md1,md2)*2,max(ml1,ml2)*2,max(mr1,mr2)*2)
    print(mu,md,ml,mr)
    print("matrix size:",mu+md, ml+mr)
    opoint = (int((mu+md)/2),int((ml+mr)/2))
    print(opoint)
    #matrix1 = [[0 for x in range(ml+mr+1)] for y in range(mu+md+1)]
    #matrix2 = [[0 for x in range(ml+mr+1)] for y in range(mu+md+1)]
    #matrix1[opoint[0]][opoint[1]]=1
    #matrix2[opoint[0]][opoint[1]]=1
    positions1 = process_wire2(wire1)
    print("MATRIX2")
    positions2 = process_wire2(wire2)
    print(positions1)
    print(positions2)
    print(find_closest2(set(positions1).intersection(positions2)))
    exit()
    matrix1[opoint[0]][opoint[1]]=0
    matrix2[opoint[0]][opoint[1]]=0
    #print_matrix(matrix1)
    #print()
    #print_matrix(matrix2)
    #print()
    result = sum_matrix(matrix1,matrix2)
    #print_matrix(matrix1)
    #print(find_closest(opoint,matrix1))
    print(find_closest(opoint,result))
