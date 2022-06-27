# dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# my_dic={}
# for i in range(len(dic)):
#     max=0
#     for i in dic:
#         if dic[i]>max:
#             max=dic[i]
#             h=i
#     my_dic.update({h:max})
#     dic.pop(h)
# print(my_dic)

# dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# for i in dic:
#     for j in dic:
#         if dic[i]>dic[j]:
#             dic[i],dic[j]=dic[j],dic[i]
# print(dic)

# for i in dic:
#     for j in dic:
#         if dic[i]<dic[j]:
#             dic[i],dic[j]=dic[j],dic[i]
# print(dic)


# dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# for x,y in dic.items():
#     print(x,y)

# a=int(input("enter the number:-"))
# if a>=1000:
#     print(a//1000)
# elif a>=500:
#     print(a%1000//5000)
# elif a>200:
#     print(a%500//200)
# elif a>100:
#     print(a%200//100)
# elif a>50:
#     print(a%100//50)
# else:
#     print("")


amount=int(input("enter the number"))
if amount>=10 or amount<=50:
    print("note of 10 rupees:-",amount//10)
    if amount>=50 or amount<=100:
        print("note of 50 rupees:-",amount//50)
        if amount>=100 or amount<=200:
            print("note of 100 rupees:-",amount//100 )
            if amount>=200 or amount<=500:
                print("note of 200 rupees:-",amount//200)
                if amount>=500 or amount<=2000:
                    print("note of 500 rupees:-",amount//500)
                    if amount>=2000:
                        print("note of 2000 rupees:-",amount//2000)
                    else:
                        print("")
                else:
                    print("")
            else:
                print("")
        else:
            print("")
    else:
        print("")
else:
    print("")

