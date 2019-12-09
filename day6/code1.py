#!/usr/bin/env python

from math import floor

def read_input():
    with open("input.txt") as inp:
        orbits = inp.readlines()
    return orbits

def map_orbits(orbits):
    maps = {}
    maps2 = {}
    for orbit in orbits:
        cm, ob = orbit.rstrip().split(')')
        #maps[ob] = [cm]
        if cm in maps2:
            maps2[cm] = maps2[cm]+[ob]
        else:
            maps2[cm] = [ob]

    maps['COM'] = []
    update_maps(maps,maps2,'COM')
    print(maps)
    print(maps2)
    return maps

def update_maps(maps,maps2,cm):
    if not cm in maps2:
        return 
    else:
        for ob in maps2[cm]:
            maps[ob] = [cm] + maps[cm]
            update_maps(maps,maps2,ob)
        return  

def count_orbits(maps):
    val = 0
    for k in maps:
        val += len(maps[k])
    print(val)

if __name__ == "__main__":
    orbits = read_input()
    maps = map_orbits(orbits)
    count_orbits(maps)
