#P3: Given a string and a substring, find whether the substring is found in the string.
import re

fstring = "alphabets"
sstring = "alpha"
reg1 = re.search(sstring, fstring)
print(reg1)