number=input("enter the numbers:")
number_list=number.split(" ")

count=0
for numbers in number_list:
    count=count+1
#print(count)

for i in range(count):
    number_list[i]=int(number_list[i])
print(number_list)

#max
maximum=number_list[0]
for number in number_list:
    if number > maximum:
        maximum=number
print(f"max is:{maximum}")



