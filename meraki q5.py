list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
a={}
for i in range(len(list1)):
    a.update({list1[i]:list2[i]})
print(a)