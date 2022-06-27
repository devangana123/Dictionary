a=[10,15,4,23,0]
# print("unsorted list",a)
for j in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            print(a)
        else:
            print(a)
    print()
print("sorted list",a)



# num=int(input("enter the number"))
# a=[]
# print("enter the values:")
# for k in range(num):
#     a.append(int(input()))
# print("unsorted list",a)
# for j in range(len(a)-1):
#     for i in range(len(a)-1):
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
#             print(a)
#         else:
#             print(a)
#     print()
# print("sorted list",a)



# num=int(input("enter the number"))
# a=[]
# print("enter the values:")
# for k in range(num):
#     a.append(int(input()))
# print("unsorted list",a)
# for j in range(len(a)-1):
#     for i in range(len(a)-1):
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
            
# print("sorted list",a)



# a=[10,15,4,23,0]
# print("unsorted list",a)
# for j in range(len(a)):
#     for i in range(len(a)-1):
#         if a[j]>a[i]:
#             a[j],a[i]=a[i],a[j]
# print("sorted list",a)