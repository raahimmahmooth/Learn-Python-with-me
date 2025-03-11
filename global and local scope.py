# a=10
# def display():
#     print(a)
#
#     b=15
#     def show():
#         print(b)
#     show()
#
# display()
# print(a)
#
# #no block scope
# a,b=3,3
# if a==b:
#     c=a+b
# print(c)
#
# d=99
# d=d*1
# def katu():
#     global d
#     d=d+1
#     d=d*2
#     print(d)
#
# katu()
# d=d*2
# print(d)
# def display():
#     a=20
#     def show():
#         global a
#         a=30
#     print(f"value before calling show():{a}")
#     show()
#     print(f"value after calling show():{a}")
# display()
# print(a)

name="raahim"
def disname():
    global name
    name=name+" mahmooth"
print(name)
disname()
print(name)

