# # Q14.Write a Python program to multiply all the items in a dictionary.

a={'w': 5, '3': 7, 'r': 6, 'e': 3, 's': 1, 'o': 8, 'u': 9, 'c': 1}
multiply=1
for x in a:
    multiply=multiply*a[x]
print(multiply)