def green(name,dept="msc"):
#def green(dept="msc", name):error=always non deafult argument shoud follow
    print(f"hi {name}")
    print(f"are you from {dept} department")
green("raahim","it")#positional arguments
green(dept="it",name="raahhim")#keyword argumant order can be colapsed
#green(dept="cs","kavindu")#error
green("kavindu",dept="cs")#mix argumant but position argumant should be first
green("raahim")#default argument

#arbiteri  positional argument
def add(*numbers):#(1,2,3,4,5,,6,7,4)
    c=0
    for i in numbers:
        c=c+i
    print(f"print sum is:{c}")
add(3,3,2,1,2,3)
