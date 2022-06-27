def harshad(num):
    n=num
    rem=0
    sum=0
    while num>0:
        rem=num%10
        sum=sum+rem
        num=num//10
        if n%sum==0:
            return True
        else:
            return False
a=harshad(int(input("enter the number:-")))
print(a)