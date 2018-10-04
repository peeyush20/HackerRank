#!/bin/python3

import sys

def jumpingOnClouds(c):
    # Complete this function
    step = 0
    current = 0
    while current < len(c) - 2:
        step = step + 1
        if c[current + 2] == 0:
            current = current + 2
        else:
            current = current + 1

    if current == len(c) -2:
        step = step+1
    return step


if __name__ == "__main__":
    n = int(input().strip())
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c)
    print(result)
