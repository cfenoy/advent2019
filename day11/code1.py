#!/usr/bin/env python3

import subprocess as sp

def turn_left(vec):
    return (-vec[1],vec[0])

def turn_right(vec):
    return (vec[1],-vec[0])


def map_robot(proc):
    positions=set((0,0))
    position=(0,0)
    direction = (0,1)
    colors = {(0,0):0}
    while not proc.poll():
        if position in colors:
            color = colors[position]
        else:
            color = 0
        proc.stdin.write('%d\n' % color)
        color = proc.stdout.readline().rstrip()
        if not color:
            break
        color = int(color)
        turn = proc.stdout.readline().rstrip()
        positions.add(position)
        if turn == '0':
            direction = turn_left(direction)
        else:
            direction = turn_right(direction)
        colors[position] = color
        position = (position[0]+direction[0],position[1]+direction[1])

    print(len(colors))

if __name__ == "__main__":
    s = sp.Popen("./intcode.py",bufsize=1,stdin=sp.PIPE,stdout=sp.PIPE,text=True)
    map_robot(s)
