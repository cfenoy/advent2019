#!/usr/bin/env python3
from pprint import pprint

def read_input():
    with open("input.txt") as inp:
        wire1 = inp.readline().rstrip().split(',')
        wire2 = inp.readline().rstrip().split(',')
    return wire1,wire2

def process_wire(wire):
    posy = 0
    posx = 0
    positions = []
    for move in wire:
        direction,amount = (move[0],int(move[1:]))
        if direction == 'R':
            for i in range(0,amount):
                positions.append((posx+1,posy))
                posx+=1
        elif direction == 'L':
            for i in range(0,amount):
                positions.append((posx-1,posy))
                posx-=1
        elif direction == 'U':
            for i in range(0,amount):
                positions.append((posx,posy-1))
                posy-=1
        elif direction == 'D':
            for i in range(0,amount):
                positions.append((posx,posy+1))
                posy+=1
    return positions

def print_matrix(matrix):
    print('\n'.join([''.join(['{:1}'.format(item) for item in row])
        for row in matrix]))

def find_closest(crosses,p1,p2):
    dist = []
    for cross in crosses:
        print(p1.index(cross)+1)
        print(p2.index(cross)+1)
        dist.append(p1.index(cross)+p2.index(cross)+2)
    return min(dist)

if __name__ == "__main__":
    wire1,wire2 = read_input()	
    positions1 = process_wire(wire1)
    positions2 = process_wire(wire2)
    print(find_closest(set(positions1).intersection(positions2),positions1,positions2))
