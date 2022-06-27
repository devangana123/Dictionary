student=int(input("enter the count of student"))
cost=int(input("enter the cost of student"))
a=student*cost
if a<=50000:
    print(a,"it is the ammount we are under the budget")
else:
    print(a,"it is the ammount we are not in budget")           