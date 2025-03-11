def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(y,m):
    month_list=[31,28,31,30,31,30,31,30,31,30,31,30]
    if leap_year(y) and m==2:
        return 29
    else:
        return month_list[m-1]


year=int(input("enter year:"))
month=int(input("enter month:"))

result=days_in_month(year,month)
print(result)

