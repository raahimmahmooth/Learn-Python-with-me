from itertools import count

yourname=str(input("enter your name:"))
loversname=str(input("enter your partners name:"))
combine=yourname.lower()+loversname.lower()
t=combine.count('t')
r=combine.count('r')
u=combine.count('u')
e=combine.count('e')

true=100-(t+r+u+e)

l=combine.count('l')
o=combine.count('o')
v=combine.count('v')
e=combine.count('e')

love=100-(l+o+v+e)
love_score=(true+love)/2

print(f"your love score is {love_score} %")



