#!/bin/python3

import sys

def caesarCipher(s, k):
    # Complete this function
    res = ''
    if k > 26:
        k = k % 26
    for i in s:
        shift = ord(i) + k
        if i.islower():
            if shift > 122:
                shift = shift - 122 + 96
            res += chr(shift)
        elif i.isupper():
            if shift > 90:
                shift = shift - 90 + 64
            res += chr(shift)
        else:
            res += i
    return res

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
