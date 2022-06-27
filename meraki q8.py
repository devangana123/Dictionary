# # Take input of name and marks of 10 students and store to a dictionary.
# # Output :-{'sonu':85,'Kartik':90,'Deepak':96,'Aman':76,'Somesh':60,'Umesh':85,'Amarpal':70,'Roshan':57,'Riyaz':98,'Shabid':56}

num=int(input("enter the number:-"))
a={}
for i in range(num):
    name=input("enter the name:-")
    marks=int(input("enter the marks:-"))
    for j in name,marks:
        a.update({name:marks})
print(a)
