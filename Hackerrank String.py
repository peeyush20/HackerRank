#!/bin/python3

import sys


def hackerrankInString(s):
    # Complete this function
    orig = 'hackerrank'
    count = 0

    for i in orig:
        curr = s.find(i)
        if curr == -1:
            return 'NO'
        else:
            count += 1
            s = s[curr +1:]
    if count != len(orig):
        return 'NO'
    return 'YES'


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)
