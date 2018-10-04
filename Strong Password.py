#!/bin/python3

import re

def minimumNumber(n, password):
    param = ['length','Digit','Lower','Upper','Special']
    count = 0

    if not re.search('[A-Z]',password):
        count += 1
    if not re.search('[a-z]',password):
        count += 1
    if not re.search('[0-9]',password):
        count += 1
    if not re.search('\W', password):
        count += 1

    if (len(password) + count) < 6:
        count = count + (6 - (len(password) + count))
    return count


if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
