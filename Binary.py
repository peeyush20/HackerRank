def binary(num):
    r = ''
    while num >= 1:
        r += str(num % 2)
        num = int(num / 2)
    r = r[::-1]

    #print(r)
    max_length = 0
    for i in r.split('0'):
        if len(i) > max_length:
            max_length = len(i)
    return max_length

n = int(input())
print(binary(n))