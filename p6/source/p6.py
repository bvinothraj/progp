
def reverseString(str1):
    '''
    #P6: Given an input string, reverse the string without using any in-built function.
    '''
    str1_list = list(str1)
    str1_length = len(str1_list)
    str1_new = []
    for i in range(str1_length - 1, -1, -1):
        str1_new.append(str1_list[i])
    return ''.join(str1_new)