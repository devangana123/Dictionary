dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
for i in dic:
    for j in dic:
        if dic[i]<dic[j]:
            dic[i],dic[j]=dic[j],dic[i]
print(dic)


# user_choice=input("enter the user choice:-")
# computer_choice=input("enter the computer choice:-")
# if user_choice=="scissor" and computer_choice=="paper":
#     print("user win and computer lose")
# elif user_choice=="rock" and computer_choice=="scissor":
#     print("user win and computer lose")
# elif user_choice=="paper" and computer_choice=="scissor":
#     print("user lose and computer win")
# elif user_choice=="Scissor" and computer_choice=="paper":
#     print("user win and computer lose")
# else:
#     print("cancelled")


# phy="physics"
# che="chemistry"
# bio="biology"
# cmp="computer"
# mth="math"
# sub=input("enter the subject:: phy::che::bio::cmp::mth: ")
# if sub==phy:
#     phy2=int(input("enter your marks: "))
#     phy3=int(input("out of: "))
#     if phy2>=0 or phy3>=0:
#         print(phy2/phy3*100)
# elif sub==che:
#     che2=int(input("enter your marks: "))
#     che3=int(input("out of: "))
#     if che2>=0 or che3>=0:
#         print(che2/che3*100)
# elif sub==bio:
#     bio2=int(input("enter your marks: "))
#     bio3=int(input("out of: "))
#     if bio2>=0 or bio3>=0:
#         print(bio2/bio3*100)
# elif sub==cmp:
#     cmp2=int(input("enter your marks: "))
#     cmp3=int(input("out of: "))
#     if cmp2>=0 or cmp3>=0:
#         print(cmp2/cmp3*100)
# elif sub==mth:
#     mth2=int(input("enter your marks: "))
#     mth3=int(input("out of: "))
#     if mth2>=0 or mth3>=0:
#         print(mth2/mth3*100)
# else:
#     print("invalid entry")

