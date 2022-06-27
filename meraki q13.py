my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
max=0
dic={}
for i in my_dict:
    if my_dict[i]>max:
        key1=i
        max=my_dict[i]
dic[key1]=max
max1=0
for i in my_dict:
    if my_dict[i]>max1 and my_dict[i]!=max:
            key2=i
            max1=my_dict[i]
dic[key2]=max1
max2=0
for i in my_dict:
    if  my_dict[i]>max2 and my_dict[i]!=max and my_dict[i]!=max1:
            key3=i
            max2=my_dict[i]
dic[key3]=max2
print(dic.keys())    



# name=["rani","divya","anisha","guddu","golu"]
# i=0
# b=[]
# while i<len(name):
#     if i%2==0:
#         a=(name[i])
#         b.append(a)
#     i=i+1
# print(b)