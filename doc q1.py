# # Write a Python program to combine two dictionary adding values for common keys. 
# # d1 = {'a': 100, 'b': 200, 'c':300}
# # d2 = {'a': 300, 'b': 200, 'd':400}
# # Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d1:
#     if i in d2:
#         d2[i]=d1[i]+d2[i]
#     else:
#         d2[i]=d1[i]
# print(d2)



# num=int(input("enter the number:-"))
# if num!=1 and num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0 and num%11!=0 or num==2 or num==3 or num==5 or num==7 or num==11:
#     print("prime nunber")
# else:
#     print("not prime")


date=int(input("enter the day:-"))
month=int(input("enter the month"))
year=int(input("enter the year"))
if date!=31 and date!=29:
    print(date+1,"/",month,"/",year)
elif date==29 and month==2:
    print("1","/",month+1,"/",year)
elif date==31 and month==12: 
    print("1","/","1","/",year+1)
else:
    print("invalid") 
