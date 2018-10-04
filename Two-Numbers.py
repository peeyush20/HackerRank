s = "aab"
longest = 0
substring = ''

for i in range(0, len(s)):
    present = []
    if longest > len(s[i:]):
        break
    if substring == s[i:i+len(substring)]:
        i = i + len(substring)
    for j in range(i, len(s)):
        try:
            flag = present.index(s[j])
            break
        except ValueError as e:
            present.append(s[j])

    length = len(present)
    if length > longest:
        longest = length
        substring = s[i:j]


print(longest)
print(substring)