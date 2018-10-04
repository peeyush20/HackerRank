#!/bin/python3

import os
import sys


#
# Complete the pageCount function below.
#
def pageCount(n, p):

    k = 1
    count1 = 0
    while k < p:
        count1 += 1
        k = k + 2

    k = n
    count2 = 0
    while k >= p:
        count2 += 1
        k = k - 2

    return min(count1, count2)


if __name__ == '__main__':

    n = int(input())

    p = int(input())

    result = pageCount(n, p)
    print(result)
