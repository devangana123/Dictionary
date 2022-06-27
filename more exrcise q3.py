name=input("enter the name:-")
if name>='a' and name<='z' or name>='A' and name<='Z':
    sp_chr=input("enter the special character:-")
    if sp_chr=='@' or '#' or '$':
        num=int(input("enter the number:-"))
        if num>0:
            a=str(name+sp_chr+str(num))
            if len(a)==16:
                print(a,"it is the strong password")
            else:
                print("it is the weak password")
        else:
            print("it is not the number")
    else:
        print("it is not special character")
else:
    print("it is not letters")
    