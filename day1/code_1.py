#!/usr/bin/env python

from math import floor

def read_input():
    with open("input.txt") as inp:
        modules = inp.readlines()
    return modules

def compute_fuel(modules):
    fuel = 0
    for mod in modules:
        fuel += floor(mod/3)-2
    return int(fuel)

if __name__ == "__main__":
    modules = read_input()
    mod = map(lambda x: int(x), modules)
    print(compute_fuel(mod))
