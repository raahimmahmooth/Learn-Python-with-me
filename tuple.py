tuple1=(12,6,-8,"raahim",9,0,23,6)
tuple2=(12,6,-8,"raahim",9,0,23,6)
print(len(tuple2))
print(type(tuple1))
print((tuple1[1:5]))#4=legth print till 4-1:3index
print((tuple1[::5]))

tuple3=(tuple1,tuple2)#nested tuple
print(tuple3)
print(len(tuple3))#len=2
tuple3= tuple1 + tuple2#concatenated tuple
print(tuple3)
print(len(tuple3))#len=16
print(tuple3.count("raahim"))
print(tuple3.index("raahim"))


multi=(10,)*10
print(multi)



list1=[1,2,3]
print(tuple(list1))
