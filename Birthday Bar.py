#!/bin/python3

import sys


def solve(n, s, d, m):
    # Complete this function

    count = 0
    tmp = m

    for i in range(len(s)):
        su = 0
        if (i + m) <= len(s):
            for j in range(i,tmp):
                su += s[j]
            if su == d:
                count += 1
            tmp = tmp + 1
    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
