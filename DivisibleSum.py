#!/bin/python3

def divisibleSumPairs(n, k, ar):
    # Complete this function
    res = 0
    for i in range(len(ar)):
        for j in range(len(ar)):
            if i >= j:
                continue
            else:
                if (ar[i] + ar[j]) % k == 0:
                    res += 1
    return res


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
