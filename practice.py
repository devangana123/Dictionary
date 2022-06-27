# # if we want the only value from dictionary
# d={"brand":"suzuki","model":"drize","year":2020}
# x=d.values()
# print(x)

# # if we want the only keys from dictionary
# d={"brand":"suzuki","model":"drize","year":2020}
# x=d.keys()
# print(x)

# # if we have to accessing the each keys from dictionary
# d={"brand":"suzuki","model":"drize","year":2020}
# for i in d:
#     print(i)

# # if we have to accessing the each values from dictionary
# d={"brand":"suzuki","model":"drize","year":2020}
# for i in d:
#     print(d[i])

# # if we have to get only specific values from dictionary
# d={"brand":"suzuki","model":"drize","year":2020}
# x=d["model"]
# print(x)


# # if else revesion
# month=input("enter the month:-")
# if month=="november" or month=="december" or month=="january" or month=="february":
#     print("winter")
# elif month=="march" or month=="aprel" or month=="may" or month=="june":
#     print("summer")
# else:
#     print("rainy season")

# city_population = {
#     "NewYorkCity":8550405,
#     "LosAngeles":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Vancouver":631486, 
#     "Boston":667137
# }

# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))

# Dict = {
#        'ball' : 'green',
#        'Ball': 'red'}
# print(Dict['ball'])
# print(Dict['Ball'])
# print(Dict['bat'])

# list1=[1,3,4,6,7,9,8,6,4,2]
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i]<=list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)


# Q28.Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}


# a={'a':1,'b':2,'c':3}
# b=[]
# c=[]
# for i in a.keys():
#     b.append(i)
# for  j in a.values():
#     c.append(j)
# print(b)
# print(c)

# a=int(input("enter the number:-"))
# b={}
# for i in range(a):
#     key=input("enter the keys:-")
#     value=input("enter the value:-")
#     for j in key,value:
#         b.update({key:value})
# print(b)

# c=[1,2,3,4]
# i=len(c)-1
# b={}
# while i>=0:
#     b={c[i]:b}
#     i=i-1
# print(b)



# a=[1,1,1,2,2,3,3,3,4,4,5]
# b={}
# c=0
# for i in range(len(a)):
#     if i in b:
#         c=c+1
#         if c==2:
#             b.update({a[i]})
# print(b)


# b={}
# i=0
# c=0
# while i<len(a):
#     if a[i] in b:
#         c+=1
#     i=i+1
#     if c==2:
#         b.update({a[i]})
# print(b)


# b="monika"
# a=[]
# i=0
# while i<len(b):
#     a.append(b[i])
#     i=i+1
# print(a)
    
# num=int(input("enter anything:-"))
# if num%3==0 and num%5==0:
#     print("navgurukul")
# elif num%3==0:
#     print("nav")
# elif num%5==0:
#     print("gurukul")
# else:
#     print(num)



# import json

# dict1 ={
#     "emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     },
#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#     },
# }
# out_file = open("myfile.json", "w")
  
# json.dump(dict1, out_file, indent = 4)
  
# out_file.close()


# import json

# a={'lalalala': 3}
# mystring = json.dumps(a)
# print(mystring)



# a=["a","b","c","d"]
# b=[100,200,300,400]
# i=0
# p=-1
# c={}
# while i<len(a):
#     c.update({a[i]:b[p]})
#     p=p-1
#     i=i+1
# print(c)


# a=["a","b","c","d"]
# b=[100,200,300,400]
# p=-1
# c={}
# for i in range(len(a)):
#     c.update({a[i]:b[p]})
#     p=p-1
# print(c)    



# a=["name","age"]
# b=["Divya",16]
# c={}
# i=0
# while i<len(a):
#     c.update({a[i]:b[i]})
#     i=i+1
# print(c)    


# a=["name","age"]
# b=["Divya",16]
# c={}
# for i in range(len(a)):
#     c.update({a[i]:b[i]})
# print(c)    




# a={"one":{1:2,3:4},"two":{1:3,4:5}}
# b={}
# for i in a:
#     for j in a.values():
#         # if j==2:
#             b.update({i:j})              #{"one":2,"two":3}
#             # b.update(b)
#         # pass
# print(b)



# a={"one":{1:2,3:4},"two":{1:3,4:5}}
# b={}
# b["one"] = a["one"][1]
# b["two"] = a["two"][1]
# print(b)



