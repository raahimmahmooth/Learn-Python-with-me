a=5
print(id(a))
b=5
print(id(b))
print(a is b)
c='raahim'
d='mahmooth'
e='raahim'
#a=8
x=5
print(id(x))
print(id(b))
print(a is b)
print(c is d)
print(c is not d)
print(c is e)
#case 1
e=8
print(id(a))
e=10
print(id(a))
print(a is a)
#case 2
name="raahim"
print(id(name))
name="aliya"

print(id(name))
print(name is name)
z=10
print(id(z))
z=2
print(id(z))
print(z is z)
