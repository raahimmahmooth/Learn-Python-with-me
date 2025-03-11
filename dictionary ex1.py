from http.cookiejar import join_header_words

stu_marks={
    "raahim":98,
    "nimal":74,
    "linoshen":55,
    "ikrem":23
}
#print(stu_marks)
stu_grades={}
for student in stu_marks:
    marks=stu_marks[student]
    if marks >75:
        stu_grades[student]="A+"
    elif marks >65:
        stu_grades[student]="B+"
    elif marks >50:
        stu_grades[student]="c+"
    else:
        stu_grades[student]="d+"
print(stu_grades)
