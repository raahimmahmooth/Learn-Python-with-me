# stu_data={
#     "ram":{"roll_no":10,"age":20,"course":"python"},
#     "shaam":{"roll_no":12,"age":20,"course":"java"}
#
# }
# #print(stu_data)
# #print(stu_data["ram"])acces subscript
# #print(stu_data["ram"]["roll_no"])accsessing a subscrip in nested dict
# stu_data["ram"]["phone_no"]=90899990
# print(stu_data["ram"])
# print(stu_data["ram"].pop("phone_no"))
# #del stu_data["ram"]["phone_no"]
# print(stu_data["ram"])
#

#list within a dictionary
# travel_data={
#     "central":["matala","kandy","akurana","madawala"],
#     "easten":["gall","hambanthota","matara"]
# }
# print(travel_data)
# print(travel_data["central"])
#dictionary within a list
stu_data=[
    {"name":"ram",
     "roll_no":10,
     "age":20,
     "course":"python"
     },
    {
        "name":"sham"
        ,"roll_no":12
        ,"age":20,
         "course":"java",
        "phone_no":[900080,828288]
     }
 ]
print(stu_data[0])
print(stu_data[1])
print(stu_data[1]["phone_no"])

def add_new_student(name,rollno,age,course):
    new_student={}#create a empty dic and append to list just all
    new_student["name"]=name
    new_student["roll_no"] =rollno
    new_student["age"] = age
    new_student["course"] = course
    stu_data.append(new_student)
add_new_student(name="hari",rollno=39,age=20,course="c++")
print(stu_data)




