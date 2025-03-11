import random

#a=random.randint(2,9)
#a=random.randrange(2,9)
#a=random.randbytes(3)
#a=random.random()
#a=random.uniform(5,9)
l=[3,2,8,9,0,8,3,4,33,44,22,33,45,56,65,39,97]
print(random.choice(l))
random.shuffle(l)
print(l)
