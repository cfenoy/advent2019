#!/usr/bin/env python3

import numpy as np
import re

def read_input():
    moons = []
    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.rstrip()
            pos = np.array(re.findall("(-?[0-9]+)+",line))
            pos = pos.astype(np.float)
            vel = np.zeros(3)
            moons.append({"pos":pos,"vel":vel})
    return moons

def compute_diff(a,b):
    if a > b:
        return -1
    elif a == b:
        return 0
    else:
        return 1

def compute_pos_and_vel(moons,st_x,ix,st_y,iy,st_z,iz):
    vels = []
    for i in range(0,len(moons)):
        vel = moons[i]["vel"]
        for j in range(0,len(moons)):
            if i == j :
                continue
            for k in range(0,len(moons[i]["pos"])):
                if moons[i]["pos"][k] > moons[j]["pos"][k]:
                    vel[k] += -1
                elif moons[i]["pos"][k] < moons[j]["pos"][k]:
                    vel[k] += 1
        vels.append(vel)
    if (not np.any(np.array(vels)[:,0])) and not st_x:
        ix += 1
        st_x = True
    elif not st_x:
        ix += 1
    if (not np.any(np.array(vels)[:,1])) and not st_y:
        iy += 1
        st_y = True
    elif not st_y:
        iy += 1
    if (not np.any(np.array(vels)[:,2])) and not st_z:
        iz += 1
        st_z = True
    elif not st_z:
        iz += 1

    for i in range(0,len(moons)):
        moons[i]["pos"]+=moons[i]["vel"]

    return st_x,ix,st_y,iy,st_z,iz

def iterate(iterations,moons):
    _moons = moons.copy()
    st_x = 0
    st_y = 0
    st_z = 0
    ix,iy,iz=0,0,0
    for i in range(0,iterations):
        st_x,ix,st_y,iy,st_z,iz = compute_pos_and_vel(_moons,st_x,ix,st_y,iy,st_z,iz)
        if st_x and st_y and st_z:
            print("Steps",np.lcm.reduce([ix*2,iy*2,iz*2]))
            return
    print("Energy:",compute_energy(_moons))

def compute_energy(moons):
    energy = 0
    for i in moons:
        pot = np.sum(np.absolute(i["pos"]))
        kin = np.sum(np.absolute(i["vel"]))
        energy+=pot*kin
    return(energy)

import timeit

if __name__ == "__main__":
    moons = read_input()
    iterate(1000,moons)
    moons = read_input()
    iterate(10003000,moons)
