#!/bin/python3

import os
import sys


#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    sum1 = 0
    sum2 = 0

    for i in range(len(a)):
        sum1 += a[i][i]

    j = 0
    for i in range(len(a) - 1, -1, -1):
        sum2 += a[i][j]
        j = j + 1

    return abs(sum1 - sum2)

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)
    print(result)