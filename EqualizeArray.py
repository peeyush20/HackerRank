#!/bin/python3

from collections import Counter

def equalizeArray(arr):
    # Complete this function
    d = {}
    count = 0
    d = dict(Counter(arr))
    #print(d)
    m = (max(d, key=d.get))
    for i in arr:
        if i != m:
            count += 1
    return count

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)
