set1={1,2,3,4,5,6}
set2={5,6,7,8,9,10}
set3={11,12,13,14,15}
#print(set1.union(set2))
#print(set1.union(set2,set3))
#print(set1.union((1,2,4,9,8,78)))passed a tuple value
#print(set1.union([1,2,4,9,8,78]))passed list value as argument
#print(set1 | set2)#union in operotors
#print(set1 | set2 |set3)
#print(set1 | set2 |[2,3,4,5,])error
##update

#set1.update(set2) it does not return anything
#print(set1)

#set1 |= set2 it does not return anything
#print(set1)

#set1.update(["raahim",5,6,77,00,88])it does not return anything
#print(set1)

#intersection

#print(set1.intersection(set2))

#print(set1 & set2)it will return avalue

#print(set1.intersection_update(set2)) it does not return any values

#set1.intersection_update(set2)
#print(set1)

#difference
#print(set1.difference(set2))

#print(set1-set2)
#to modify
#set1.difference_update(set2)
#print(set1)

#print(set1.symmetric_difference(set2))
#set1.symmetric_difference_update(set2)
#print(set1)

#print(set1 ^ set2)
#print(set1.symmetric_difference([4,5,6,7,8,9,0]))


#print(set1 disjoin set2)

#subset
