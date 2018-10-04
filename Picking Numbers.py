#!/bin/python3

import sys


def pickingNumbers(a):
    # Complete this function
    d = {}
    for i in a:
        cu = d.get(i, 0)
        d[i] = 1 + cu

    s = 0
    for i in d:
        tmp = d.get(i) + d.get(i+1,0)
        if tmp > s:
            s = tmp
    return s

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(a)
    print(result)