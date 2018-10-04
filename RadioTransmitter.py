#!/bin/python3

import sys


def hackerlandRadioTransmitters(x, k):
    # Complete this function

    #x = [2,4,5,6,7,9,11,12]
    y = list(range(max(x) +1))
    #y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    left = 0
    for i in range(len(y)):
        if i in x:
            coverage = []
            print(i)
            right = i + k
            if not i - k < 0:
                left = i - k
            for a in range(i,right + 1):
                if a in x:
                    coverage.append(a)
            for b in range(left,i):
                if b in x:
                    coverage.append(b)
            print(coverage)




if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    x = list(map(int, input().strip().split(' ')))
    result = hackerlandRadioTransmitters(x, k)
    print(result)
