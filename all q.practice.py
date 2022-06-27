# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic4={}
# for i in dic1,dic2,dic3:
#     dic4.update(dic1)
#     dic4.update(dic2)
#     dic4.update(dic3)
# print(dic4)



# dict1={"name":"Raju", "marks":56}
# if "name" in dict1:
#     print("exist")                              #?
# else:
#     print("not  exist")




# my_dict = {'data1':100,'data2': -54,'data3': 247}
# sum=0
# for i in my_dict.values():
#     sum+=i
# print(sum)




# dic= {1: 'NAVGURUKUL',2: 'IN',  3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
# del dic[3]['A']
# print(dic)





# list1=['one','two','three','four','five']
# list2=[1,2,3,4,5,]
# list3={}
# for i in range(len(list1)):                                    #?
#     list3.update({list1[i]:list2[i]})
# print(str(list3))




# dic={'ball':'red','bat':4,'wickets':8,'ball':'green','bat':3}
# a={}
# for i in dic:
#     if i not in a:
#         a.update(dic)
# print(a)




# a=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
# b=[]
# for i in a:
#     for j in i.values():
#         if j not in b:
#             b.append(j)
# print(b) 





# num=int(input("enter the number"))
# a={}
# for i in range(num):
#     name=input("enter the nmae:-")
#     marks=int(input("enter the marks:-"))
#     for j in name,marks:
#         a.update({name:marks})
# print(a)





a=("MISSISSIPPI")
b={}
for i in a:
    if i in b:
        b[i]+=1                       #?
    else:
        b[i]=1
print(str(b))






# dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}
# count=0
# for i in dict1:
#     for j in dict1[i]:
#         count+=1
# print("count=",count)




# c=dict()
# a={}
# for i in range(1,16):
#     c=i*2
#     a.update({i:c})
# print(a)




# my_dict = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
# max=0
# dic={}
# for i in my_dict:
#     if my_dict[i]>max:
#         key1=i
#         max=my_dict[i]
# dic[key1]=max
# max1=0
# for i in my_dict:
#     if my_dict[i]>max1 and my_dict[i]!=max:
#         key2=i
#         max1=my_dict[i]
# dic[key2]=max1
# max2=0
# for i in my_dict:
#     if my_dict[i]>max2 and my_dict[i]!=max and my_dict[i]!=max1:
#         key3=i
#         max2=my_dict[i]
# dic[key3]=max
# print(dic.keys())



# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# for i in a:
#     for j in a:
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)




