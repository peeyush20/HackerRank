#!/bin/python3

import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
    for i in range(n):
        for j in range(n):
            if j >= (n - i - 1):
                print('#',end='')
            else:
                print(' ',end='')
        print()

if __name__ == '__main__':
    n = int(input())

    staircase(n)
