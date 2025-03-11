#assume 1year=365days,56weeks,12 months
age=int(input("enter your age:"))
calculate_days=age*365
calculate_weeks=age*52
calculate_month=age*12
#method 1
print(f"if i live for {age} years i wil live for:\n{age*365}days\n{age*52}weeks\n{age*12}month")
print(f"if i live for {age} years i wil live for:\n{calculate_days}days\n{calculate_weeks}weeks\n{calculate_month}month")