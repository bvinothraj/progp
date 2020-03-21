#P2: Count number of vowels in a string
vowels = ['a','e','i','o','u']
str1 = 'alphabets'
obj1 = {}.fromkeys(vowels, 0)
for i in list(str1):
    if i in obj1:
        obj1[i] += 1
print(str(obj1))