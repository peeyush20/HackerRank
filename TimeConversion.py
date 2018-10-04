import sys

def timeConversion(s):
    zone = s[-2:]
    hour_colon = s.index(':')
    h = s[:hour_colon]

    if zone == 'AM' and h == '12':
        hour = '00'
    elif zone == 'PM' and h == '12':
        hour = '12'
    elif zone == 'AM':
        return s[:len(s) - 2]
    else:
        hour_colon = s.index(':')
        h = s[:hour_colon]
        hour = 12 + int(h)

    op=str(hour)+s[hour_colon:len(s)-2]
    return op

s = input().strip()
result = timeConversion(s)
print(result)