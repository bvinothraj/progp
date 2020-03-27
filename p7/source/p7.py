def createMyList(arr1):
    '''
    #P7: Given an array of integers, which may contain duplicates, create an array without duplicates.
    '''
    n_obj = {}
    for i in arr1:
        n_obj[i] = 0
    return list(n_obj.keys())