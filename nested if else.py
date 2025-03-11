gender=str(input("enter your gender male or female"))

if gender == "male":
    print("your are allowed to go in")
    age = int(input("enter you age"))
    if age >= 18:
        print(" allowed")
    else:
        print("not allowed")
else:
    print("sorry you are a girl")

