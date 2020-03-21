#Given a string and a character, find the index of the first occurence of the character.
import re

str1 = "alphabets"
achar = 'a'
result = str1.find(achar)
print(result)

#result = re.search(achar, str1)
#print(result.regs[0][0])