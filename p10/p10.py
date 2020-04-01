import math

def reverse_myList(arr1):
    '''
    P10: Given an array of integers, reverse the array in-place 
    (without using another temp array, original array will be modified)
    '''
    i = 0
    j = len(arr1)-1
    for i in range(math.ceil(len(arr1)/2)):
        arr1[i], arr1[j] = arr1[j], arr1[i]
        i += 1
        j -= 1
    return arr1
