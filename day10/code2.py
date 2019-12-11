#!/usr/bin/env python3

import math

def read_input():
    asteroids = []
    with open("input.txt") as inp:
        for i,line in enumerate(inp):
            asteroids.append(list(line.rstrip()))
    return asteroids

def compute_angle(point,origin):
    ref = [1,0]
    vector = [point[0]-origin[0],point[1]-origin[1]]
    length = math.hypot(vector[0],vector[1])
    norm = [vector[0]/length,vector[1]/length]
    dotprod = norm[0]*ref[0]+norm[1]*ref[1]
    diffprod = norm[0]*ref[1]-norm[1]*ref[0]
    angle = math.atan2(dotprod,diffprod)
    if angle < 0:
        return math.degrees(2*math.pi+angle)
    return math.degrees(angle)

def compute_distance(point,origin):
    return math.hypot(point[0]-origin[0],point[1]-origin[1])


def compute_orders(asteroids,i,j):
    asteroid_h = {}
    ast_list = []
    for ti in range(0,len(asteroids)):
        for tj in range(0,len(asteroids[ti])):
            if ti == i and tj == j:
                continue
            if asteroids[ti][tj] == '#':
                angle=compute_angle([tj,ti],[j,i])
                distance=compute_distance([tj,ti],[j,i])
                if not angle in asteroid_h:
                    asteroid_h[angle] = []
                asteroid_h[angle].append([distance,tj,ti])

    for _,k in enumerate(asteroid_h):
        asteroid_h[k] = sorted(asteroid_h[k], key=lambda x: x[0])

    while ( len(asteroid_h) ):
        for i in sorted(asteroid_h):
            ast_list.append(asteroid_h[i].pop(0))
            if asteroid_h[i] == []:
                del(asteroid_h[i])

    return(ast_list[199][1]*100+ast_list[199][2])



def compute_view(asteroids,i,j):
    blocks = set()
    same_row,same_col = 0,0

    debug=False
    if i==-1 and j==1:
        debug=True

    for ti in range(0,len(asteroids)):
        for tj in range(0,len(asteroids[ti])):
            if ti == i and tj == j:
                continue
            if asteroids[ti][tj] == '#':
                if ti == i and tj < j:
                    blocks.add((0,-1))
                    continue
                elif ti == i and tj > j:
                    blocks.add((0,1))
                    continue
                if tj == j and ti < i:
                    blocks.add((-1,0))
                    continue
                elif tj == j and ti > i:
                    blocks.add((1,0))
                    continue
                
                blocks.add(((ti-i)/(tj-j),ti-i<0,tj-j<0))

    return(len(blocks))


def compute_total_views(asteroids):
    total_views = []
    max_views = 0
    station = ()
    for i in range(0,len(asteroids)):
        total_views.append([])
        for j in range(0,len(asteroids[i])):
            if asteroids[i][j] == '#':
                views = compute_view(asteroids,i,j)
                if views > max_views:
                    max_views = views
                    station=(i,j)
                total_views[i].append(str(views))
            else:
                total_views[i].append('.')

    return(station)


def compute_fuel(modules):
    fuel = 0
    for mod in modules:
        fuel += floor(mod/3)-2
    return int(fuel)

if __name__ == "__main__":
    asteroids = read_input()
    i,j = compute_total_views(asteroids)
    print(compute_orders(asteroids,i,j))
