# str1=input("enter the number")
str1=("MISSISSIPPI")
b={}
for i in str1:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(str(b))
