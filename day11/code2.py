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
    colors = {(0,0):1}
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

    return(colors)

def get_dimensions(colors):
    max_x = max(colors,key=lambda item:item[0])[0]
    max_y = max(colors,key=lambda item:item[1])[1]
    min_x = min(colors,key=lambda item:item[0])[0]
    min_y = min(colors,key=lambda item:item[1])[1]
    return(max_x,max_y,min_x,min_y)

def print_matrix(colors,dim):
    x_offset = 0-dim[2]
    y_offset = 0-dim[3]
    mat = [[0 for x in range(0,dim[0]+x_offset+1)] for y in range(0,dim[1]+y_offset+1)]
    for _,point in enumerate(colors):
        mat[point[1]+y_offset][point[0]+x_offset]=colors[point]
    for i in reversed(mat):
        line = ''
        for j in i:
            if j == 0:
                line+=' '
            else:
                line+='\u2588'
        print(line)

if __name__ == "__main__":
    s = sp.Popen("./intcode.py",bufsize=1,stdin=sp.PIPE,stdout=sp.PIPE,text=True)
    colors = map_robot(s)
    dimensions = get_dimensions(colors)
    print_matrix(colors,dimensions)
