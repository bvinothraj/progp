#P7: Given an array of integers, which may contain duplicates, create an array without duplicates.
arr1 = [3,7,1,9,3,45,5,5]
n_obj = {}
#dup_arr1 = []

for i in arr1:
    n_obj[i] = 0
print(list(n_obj.keys()))


'''
def list_without_duplicates(arr1):
    n_obj = {}.fromkeys(arr1, 0)
    return list(n_obj.keys())

print(list_without_duplicates(arr1))
'''