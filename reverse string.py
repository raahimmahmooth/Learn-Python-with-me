

def check_prime(number):
    is_prime=True
    for i in range(2,number):
        if number == 1:
            is_prime==False
        if number%i == 0:
            is_prime=False
    if is_prime ==True:
        print("it's a prime")
    else:
        print("it is not a prime")
n=int(input("enter a  number"))
check_prime(n)