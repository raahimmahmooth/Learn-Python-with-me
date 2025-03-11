height=int(input("enter you height:"))
bill=0
if height >= 3:
    print("you can ride")
    age=int(input("enter you age:"))
    if age < 9:
        bill=150
        print("it cost 150RS")
    #can use if also
    elif age < 18:
        bill=250
        print("it cost 250RS")
    elif age < 20:
        bill=350
        print("it cost 350RS")
    else:
        bill=500
        print("it cost 500RS")

    want_pic = str(input("do you want a piz Y,y/N,n:"))
    if want_pic == 'y' or want_pic == 'Y':
       bill = bill + 50
       print(f"your total is {bill}")
else:
     print ("insufficent height!!")
print("bye")
