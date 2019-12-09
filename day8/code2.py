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
    ones = len(np.where(zero_layer == '1')[0])
    twos = len(np.where(zero_layer == '2')[0])
    print(ones*twos)

def render_image(image):
    final_image = []
    for i in range(0,WIDTH*HEIGHT):
        color = 2
        for layer in image:
            if layer[i] == '2':
                continue
            else:
                color = layer[i]
                break
        final_image.append(color)
    for i in range(0, len(final_image), WIDTH):
        line = ''
        for j in final_image[i:i+WIDTH]:
            if j == '0':
                line+=' '
            else:
                line+='\u2588'
        print(line)


if __name__ == "__main__":
    image = read_input()
    layers = split_input(image)
    render_image(layers)
