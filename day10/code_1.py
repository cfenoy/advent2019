#!/usr/bin/env python3

def read_input():
    asteroids = []
    with open("input.txt") as inp:
        for i,line in enumerate(inp):
            asteroids.append(list(line.rstrip()))
    return asteroids

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
                
                #blocks.add((float(i-ti)/(j-tj)))
                blocks.add(((ti-i)/(tj-j),ti-i<0,tj-j<0))
                if(debug):
                    print((ti-i)/(tj-j),ti-i<0,tj-j<0)

    return(len(blocks))


def compute_total_views(asteroids):
    total_views = []
    max_views = 0
    for i in range(0,len(asteroids)):
        total_views.append([])
        for j in range(0,len(asteroids[i])):
            if asteroids[i][j] == '#':
                views = compute_view(asteroids,i,j)
                if views > max_views:
                    max_views = views
                total_views[i].append(str(views))
            else:
                total_views[i].append('.')

    for line in total_views:
        print(line)

    print(max_views)


def compute_fuel(modules):
    fuel = 0
    for mod in modules:
        fuel += floor(mod/3)-2
    return int(fuel)

if __name__ == "__main__":
    asteroids = read_input()
    print(asteroids)
    compute_total_views(asteroids)
    #print("\n".join(''.join(asteroids)))
