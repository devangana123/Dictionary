list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
list1.extend(list2)
i=0
b=[]
while i<len(list1):
    if list1[i] not in b:
        b.append(list1[i])
    i=i+1
print(b)

# new_list = [1, 2, 5, 10, 12, 13, 16, 20]