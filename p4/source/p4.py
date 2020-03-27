'''
P4: Given an array of integers, sort them in increasing order.
'''

def qsort(arr1, start, end):
    if (start < end):
        pIndex = partition(arr1, start, end-1)
        qsort(arr1, start, pIndex)
        qsort(arr1, pIndex+1, end)

def partition(arr1, start, end):
    pviot = arr1[end]
    pIndex = start
    for i in range(start, end):
        if arr1[i] <= pviot:
            arr1[i],arr1[pIndex] = arr1[pIndex],arr1[i]
            pIndex += 1
    arr1[pIndex],arr1[end] = arr1[end],arr1[pIndex]
    return pIndex