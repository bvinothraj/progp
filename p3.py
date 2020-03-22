#P3: Given a string and a substring, find whether the substring is found in the string.
fstring = "alphabets"
sstring = "lph"
start = 0

def findsubstring(fstring, sstring):
    flstring = list(fstring)
    slstring = list(sstring)
    if len(flstring) >= len(slstring):
        for j in range(len(flstring)):
            if slstring[0] == flstring[j]:
                start = j
                ss = fstring[start:start+len(slstring)]
                if ss == sstring:
                    return "found"
        return "not found"

result = findsubstring(fstring, sstring)
print(result)
