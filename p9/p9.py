def findDuplicates(arr1):
    '''
    P9: Given an array of elements, find the duplicates in the array.
    '''
    obj = {}
    n_obj = {}
    for i in arr1:
        if i in obj:
            n_obj[i] = 0
        else:
            obj[i] = 0
    return list(n_obj.keys())