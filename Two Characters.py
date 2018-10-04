#!/bin/python3

import sys

def twoCharaters(s):
    options = []
    uni = set(list(s))

    for i in uni:
        for j in uni:
            if i == j:
                continue
            else:
                options.append(i+j)

    for j in options:
        tmp = ''
        tmp2 = ''
        print(j)
        for i in s:
            if j[0] != i:
                tmp += i
        for k in tmp:
            if j[1] != k:
                tmp2 += k
        print(tmp2)

if __name__ == "__main__":
    l = int(input().strip())
    s = input().strip()
    result = twoCharaters(s)
    print(result)
