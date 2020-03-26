def findsubstring(fstring, sstring):
    '''
    #P3: Given a string and a substring, find whether the substring is found in the string.
    '''
    flstring = list(fstring)
    slstring = list(sstring)
    start = 0

    if len(flstring) >= len(slstring):
        for j in range(len(flstring)):
            if slstring[0] == flstring[j]:
                start = j
                ss = fstring[start:start+len(slstring)]
                if ss == sstring:
                    return True
        return False
    else:
        return 'Not valid substring'
