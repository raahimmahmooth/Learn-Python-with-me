count=1
#while count <=5:print(count);count+=1
while count <= 5:
    print(count)
    count+=1
   # if count == 4:
    #    break
else:
    print("in the else block")
print("out of the loop")
#user contolling the loop bcz we dont know how numbers will be inputed
number=int(input("enter a number:"))
while number != -1:
    number = int(input("enter a number:"))
    print(number)
else:
    print("in the else block")
print("out of the the loop")