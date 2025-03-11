import random
#print("enter the names to randomly identify who will pay the bill,split name with(,):")
#names=[input(""),input(""),input(""),input(""),input("")]
#random.shuffle(names)
#last_choice=random.choice(names)
#print(names)
#print(f"{last_choice} your turn pay the bill machan")
names=input("enter name with a (,)spliit:")
names_list=names.split(",")
print(names_list)
#acces the list
length=len(names_list)
random_choice=random.randint(0,length-1)#index start with 0 but legth starts with 1


print(f"{names_list[random_choice]} your turn pay the bill machan")
