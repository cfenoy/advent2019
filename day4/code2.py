#!/usr/bin/env python

from math import floor

def read_input():
    with open("input.txt") as inp:
         return inp.readline().rstrip().split('-')

def increasing(num):
    num=str(num)
    for i in range(1,len(num)):
        if num[i]<num[i-1]:
            return None
    return(num)

def double(num):
    num=str(num)
    duplicates = 1
    for i in range(1,len(num)):
        if num[i]==num[i-1]:
            duplicates += 1
        elif duplicates == 2:
            return num
        else:
            duplicates = 1
    if duplicates == 2:
        return num

def generate_numbers(start,end):
    numbers = []
    for i in range(start,end):
        if increasing(i) and double(i):
            numbers.append(i)
    return(numbers)


if __name__ == "__main__":
    start,end = read_input()
    start = int(start)
    end = int(end)
    numbers=generate_numbers(start,end)
    print(len(numbers))
