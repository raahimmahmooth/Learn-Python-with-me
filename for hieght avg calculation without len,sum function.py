#dont use len(),sum()
heights=input("enter the heights of people ill calculate the avg(,):")
#144 144 113 111 111
height_list=heights.split(" ")
#lenth without using length funtion
count=0
for height in height_list:
    count=count+1
#convert the string into intiger
print(count)
for i in range(count):#0 1 2 3 4
    height_list[i]=int(height_list[i])
print(height_list)

#calculate the sum
sum=0
for person in height_list:
    sum=sum+person
#print(sum)
avg=sum/count
print(round(avg))


