#def add(*args,a):#(1,2,3,4,5,,6,7,4)#dd() missing 1 required keyword-only argument: 'a'
print(" arbitary posisional argumant")
def add(a,*args):#(1,2,3,4,5,,6,7,4
    c=0
    for i in args:
        c=c+i
    print(f"sum is:{c}")
add(3,3,2,1,2,3)
add(1,2,3,4,5,6,4,3,3,3,3)

print("\n")
print(" arbitary keyword  argumant")
def my_info(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)

my_info(name="raahim",age=20,school="st anthonyes college")
#my_info(name="raahim",age=20,school="st anthonyes college",12,23)error positional argument follows keyword argument
my_info(1,2,3,4,name="raahim",age=20,school="st anthonyes college")

