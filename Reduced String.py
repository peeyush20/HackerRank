#!/bin/python3

import sys

def super_reduced_string(s):
    # Complete this function
    l = list(s)
    out = []
    res = ''
    for i in range(len(l) - 1):
        if i not in out:
            if l[i] == l[i + 1]:
                out.append(i)
                out.append(i + 1)

    for i in range(len(s)):
        if i not in out:
            res += s[i]

    if len(res) == len(s):
        return res
    elif res == '':
        return 'Empty String'
    else:
        return super_reduced_string(res)

s = input().strip()
result = super_reduced_string(s)
print(result)
