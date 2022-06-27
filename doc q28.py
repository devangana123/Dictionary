# Q28.Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}


# num_list = [1, 2, 3, 4]
# new_dic=new={}
# for name in num_list:
#     new[name]={}
#     new=new[name]
# print(new_dic)


# num_list=[1,2,3,4,5,6,7]
# new_dic=new={}
# for i in num_list:
#     new[i]={}
#     new=new[i]
# print(new_dic)


# num=[1,2,3,4,5,6,7]
# b={}
# i=len(num)-1
# while i>=0:
#     b={num[i]:b}
#     i=i-1
# print(b)

# a=["rice","floar","carry"]
# i=0
# while i<len(a):
#     print(i,a[i])
#     i+=1 


# a={'a':{'b':45},'c':10,'d':35,'f':{'e':10}}
# sum=0
# for i in a:
#     if type(a[i])==dict:
#         for j in a[i]:
#             sum=sum+a[i][j]
#     else:
#         sum=sum+a[i]
# print(sum)



# num1=int(input("enter "))
# i=1
# b=[]
# while i<=num1:
#     b.append(i)
#     i+=1
# i=0
# c={}
# while i<len(b):
#     if b[i]%2==0:
#         c.update({b[i]:"true"}) 
#     else:
#         c.update({b[i]:"False"})
#     i+=1
# print(c)




# num=int(input("enter the number:-"))
# a={}
# for i in range(1,num+1):
#     key=i
#     value=i%2==0
#     z={key:value}
#     a.update(z)
# print(a)




# a={"a":{"b":45}:"c":10,"d":35,"f":{"e":10}}