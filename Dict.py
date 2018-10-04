import string

sentence = 'Jim quickly realized that the beautiful gowns are expensive'
alphabet = string.ascii_letters

count_letters = {}
#write your code here!
for i in sentence:
    if i in alphabet:
        if i not in count_letters.keys():
            count_letters[i] = 1
        else:
            current_count = count_letters[i]
            count_letters[i] = current_count + 1
print(count_letters)
