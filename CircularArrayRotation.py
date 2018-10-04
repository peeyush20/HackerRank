#!/bin/python3
import sys

def circularArrayRotation(a, k, m):
    # Complete this function

    new = a[::]
    res = []

    for i in range(len(a)):
        if i + k >= len(a):
            tmp = (i + k) - len(a)
            if tmp >= len(a):
                div = int(tmp / len(a))
                tmp = tmp - div * len(a)
            new[tmp] = a[i]
        else:
            new[i + k] = a[i]
    # print(new)

    for i in m:
        res.append(new[i])
    return res


if __name__ == "__main__":
    n, k, q = input().strip().split(' ')
    n, k, q = [int(n), int(k), int(q)]
    a = list(map(int, input().strip().split(' ')))
    m = []
    m_i = 0
    for m_i in range(q):
        m_t = int(input().strip())
        m.append(m_t)
    result = circularArrayRotation(a, k, m)
    print("\n".join(map(str, result)))

   
