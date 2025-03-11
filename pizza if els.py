print("pizza ordering system")
bill=0
pizza_type=int(input("what is the pizza type\n1)small pizza\n2)medium pizza\n3)large pizza\nplzz choose a number!!  :"))
if pizza_type == 1:
    bill=bill+100
    print("small pizza is small 100rs")
elif pizza_type == 2:
    bill=bill+200
    print("small pizza is small 200rs")
elif pizza_type == 3:
    bill=bill+300
    print("small pizza is small 300rs")
else:
    print("invalid pizza option has chooses")

want_pepper=str(input("do you want to add pepper('y','Y'):"))
if want_pepper == 'Y' or want_pepper == 'y':
    if pizza_type == 1:
        bill=bill+30
    else:
        bill=bill+50

extra_cheese=str(input("do you want to add chees('y','Y'):"))
if extra_cheese == 'y' or extra_cheese == 'Y':
    bill=bill+20
print(f"your total bill is {bill} rs enjoy you meal!!\n good bye come again")




