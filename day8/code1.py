#!/usr/bin/env python3

WIDTH=25
HEIGHT=6

import numpy as np
import math

def read_input():
    with open("input.txt") as inp:
        image = inp.readline().rstrip()
    return image

def split_input(image):
    processed = []
    layers = []
    for i in range(0, len(image), WIDTH*HEIGHT):
        layers.append(image[i:i+WIDTH*HEIGHT])
        print(image[i:i+WIDTH*HEIGHT])
    return layers

def find_solution(layers):
    zero_layer = []
    num_zeros = math.inf
    for i in layers:
        layer = np.array(list(i))
        zeros = np.where(layer == '0')[0]
        if len(zeros) < num_zeros:
            num_zeros = len(zeros)
            zero_layer = layer
        print(len(zeros))
    print(num_zeros)
    ones = len(np.where(zero_layer == '1')[0])
    twos = len(np.where(zero_layer == '2')[0])
    print(zero_layer)
    print(ones)
    print(twos)
    print(ones*twos)

if __name__ == "__main__":
    image = read_input()
    #mod = map(lambda x: int(x), modules)
    #print(image)
    layers = split_input(image)
    find_solution(layers)
