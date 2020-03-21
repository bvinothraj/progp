#P4: Given an array of integers, sort them in increasing order.
arr1 = [3,7,1,9,23,45,11,5]
print('before: ',arr1)
for j in range(1,len(arr1)):
    for i in range(0,len(arr1)-j):
        if arr1[i] > arr1[i+1]:
            arr1[i], arr1[i+1] = arr1[i+1], arr1[i]
print('after: ',arr1)