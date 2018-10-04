#!/bin/python3

import os
import sys

#
# Complete the climbingLeaderboard function below.


def climbingLeaderboard(scores, alice):
    i = 0
    res = []
    #print(scores)
    while i < len(alice):
        scores.append(alice[i])
        scores = sorted(scores,reverse=True)
        #print(scores)
        ind = scores.index(alice[i])
        s = set(scores[:ind + 1])
        #print(s)
        di = len(scores[:ind + 1]) - len(s)
        #print(di)

        #print('Index ' + str(ind))
        res.append(abs(ind - di) + 1)
        i += 1
    return res

if __name__ == '__main__':

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)
    print('\n'.join(map(str, result)))