#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the separateNumbers function below.
def separateNumbers(s):
    i = 0
    result = (True, s[0])

    while i < len(s) - 1:
        if int(s[i + 1]) - int(s[i]) == 1:
            pass
        else:
            result = (False, 0)
            break
        i += 1

    print(result)
    if result == (True, s[0]):
        print(str(result[0]) + " " + str(result[1]))
    else:
        print("NO")


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
