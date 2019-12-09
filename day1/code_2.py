#!/usr/bin/env python

from math import floor

def read_input():
    with open("input2.txt") as inp:
        modules = inp.readlines()
    return modules

def compute_fuel(modules):
    fuel = 0
    for mod in modules:
        fuel_mod = floor(mod/3)-2
        fuel += compute_extra_fuel(fuel_mod)
    return int(fuel)

def compute_extra_fuel(fuel):
    total_fuel = fuel
    while fuel > 0:
        new_fuel = floor(fuel/3)-2
        if new_fuel > 0:
            total_fuel+=new_fuel
            fuel=new_fuel
        else:
            fuel = 0
    return total_fuel

if __name__ == "__main__":
    modules = read_input()
    mod = map(lambda x: int(x), modules)
    fuel = compute_fuel(mod)
    print("Final fuel: ",fuel)
