dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
a={}
for i in dic:
    if i in a:
        pass
    else:
        a.update(dic)
print(a)    

