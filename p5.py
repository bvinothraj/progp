#Given a string and a character, find the index of the first occurence of the character.
str1 = "alphabets"
achar = 'e'

def findindex(str1, achar):
    lstr1 = list(str1)
    for i in range(len(lstr1)):
        if achar == str1[i]:
            return i
result = findindex(str1, achar)
print(result)
