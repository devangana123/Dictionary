# Q5.
# Write a Python program to sort (ascending and descending) a dictionary by value.

# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}


dic={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
for i in dic:
    for j in dic:
        if dic[i]>dic[j]:
            dic[i],dic[j]=dic[j],dic[i]
print("Dictionary in descending order by value",dic)


dic={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
for i in dic:
    for j in dic:
        if dic[i]<dic[j]:
            dic[i],dic[j]=dic[j],dic[i]
print("Dictionary in ascending order by value",dic )