#!/bin/python3

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    #
    # Write your code here.
    #
    sum = []
    count = 0
    while count <5:
        tmp = 0
        for i in range(len(arr)):
            if i == count:
                continue
            else:
                tmp += arr[i]
        sum.append(tmp)
        count += 1
    print(str(min(sum)) + " "+str(max(sum)))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)