# # Q16.Write a Python program to map two lists into a dictionari


number=[1,2,3,4,5]
num_name=['one','two','three','four','five']
new_dic={}
for i in range(len(number)):
    new_dic.update({num_name[i]:number[i]})
print(new_dic)