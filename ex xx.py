#list_of_matrix=[[1,1,1],[1,1,1],[1,1,1]]
row1=[1,1,1]
row2=[1,1,1]
row3=[1,1,1]
list_of_matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("enter the number where you need to hide the money(row,column),")
#32
row_number=int(position[0])
column_number=int(position[1])
row_selected=list_of_matrix[row_number-1]
row_selected[column_number-1]='x'
print(f"{list_of_matrix[0]}\n{list_of_matrix[1]}\n{list_of_matrix[2]}")
#print(f"{row1}\n{row2}\n{row3}")