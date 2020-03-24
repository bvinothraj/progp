#P4: Given an array of integers, sort them in increasing order.
#Bubble sort
arr1 = [3,7,1,9,23,45,11,5]
print('before: ',arr1)
for j in range(1,len(arr1)):
    for i in range(0,len(arr1)-j):
        if arr1[i] > arr1[i+1]:
            arr1[i], arr1[i+1] = arr1[i+1], arr1[i]
print('after: ',arr1)

#quick sort
arr1 = [3,7,1,9,23,45,11,5]
start = 0
end = len(arr1)
pIndex = None

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

qsort(arr1, start, end)
print(arr1)
