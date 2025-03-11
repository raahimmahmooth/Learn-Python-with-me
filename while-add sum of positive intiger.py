total=0
number=int(input("enter a positive number"))
while number != -1:
    total+=number
    number = int(input("enter a positive number or -1 to quit:"))
else:
    print("total is:",total)