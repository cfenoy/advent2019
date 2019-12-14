#!/usr/bin/env python3

import subprocess as sp
import numpy as np
import os, fcntl
import time

def turn_left(vec):
    return (-vec[1],vec[0])

def turn_right(vec):
    return (vec[1],-vec[0])


def map_robot(proc):
    screen = []
    score = 0
    while proc.poll() is None :
        x = int(proc.stdout.readline().rstrip())
        y = int(proc.stdout.readline().rstrip())
        tile_id = int(proc.stdout.readline().rstrip())
        if x == -1:
            score = tile_id
            proc.stdin.write('-1\n')
            break
        screen.append([x,y,tile_id])
    screen = np.array(screen)
    xmax = np.amax(screen[:,0])
    ymax = np.amax(screen[:,1])

    f_screen = np.zeros(shape=(ymax+1,xmax+1),dtype=(int,int))

    for i in screen:
        f_screen[i[1]][i[0]] = i[2]


    fl = fcntl.fcntl(proc.stdout, fcntl.F_GETFL)
    fcntl.fcntl(proc.stdout, fcntl.F_SETFL, fl | os.O_NONBLOCK)
    np.set_printoptions(linewidth=180)

    
    print("Num blocks:",len(np.where(f_screen == 2)[0]))
    blocks = len(np.where(f_screen == 2)[0])
    while blocks > 0:
        x = proc.stdout.readline().rstrip()
        if x == '':
            ball = np.where(f_screen == 4)[1][0]
            paddle = np.where(f_screen == 3)[1][0]
            if ball == paddle:
                proc.stdin.write('0\n')
            elif ball < paddle:
                proc.stdin.write('-1\n')
            else:
                proc.stdin.write('1\n')
            time.sleep(0.002)
            continue
        else:
            x = int(x)
        y = int(proc.stdout.readline().rstrip())
        tile_id = int(proc.stdout.readline().rstrip())
        if x == -1:
            score = tile_id
            continue
        f_screen[y][x] = tile_id
        blocks = len(np.where(f_screen == 2)[0])

    proc.stdout.readline()
    proc.stdout.readline()
    score = int(proc.stdout.readline())

    return score


if __name__ == "__main__":
    s = sp.Popen("./intcode.py",bufsize=1,stdin=sp.PIPE,stdout=sp.PIPE,text=True)
    score = map_robot(s)
    print("Score:",score)
