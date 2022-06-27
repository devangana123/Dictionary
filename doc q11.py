# # Q11.Write a Python script to merge two Python dictionaries

a={'divya':81,'kiran':13,'nilu':34,'ganga':56,'niku':67}
b={'one':1,'two':2,'three':3,'four':4,'five':5}
c={}
for i in a,b:
    c.update(a)
    c.update(b)
print(c)
