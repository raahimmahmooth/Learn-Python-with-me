# #multiple return value n single function
# import statistics
# def mean_meadium_mode(list1):
#     return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
# print(mean_meadium_mode([3,45,3,222,34,2,3]))
# result=mean_meadium_mode([3,45,3,222,34,2,3])
# print(result)
# a,b,c=mean_meadium_mode([1,2,34,5,6,7,44,2])
# print(f"m:{a}\nm:{b}\nm:{c}")
#multiple return statement in single function
def add(a,b):
    if a==0 and b==0:
        return
    else:
        return a+b


var1=int(input("enter num1"))
var2=int(input("enter num2"))
result=add(var1,var2)
print(result)