def findindex(str1, achar):
    '''
    #Given a string and a character, find the index of the first occurence of the character.
    '''
    lstr1 = list(str1)
    lachar = list(achar)
    for i in range(len(lstr1)):
        if len(lachar) == 1:
            if achar == str1[i]:
                return i
        else:
            return 'Not valid substring'
    return 'Not found'