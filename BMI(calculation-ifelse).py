weight=int(input("enter the KG:"))
height=float(input("enter the cm:"))
#(BMI)=weight*weight/height
BMI=weight**2/height
print(BMI)
if BMI < 16.0:
    print("Underweight(severe thinness)")
elif 16.0 <= BMI <= 16.9:
    print("Underweight(moderate thinness)")
elif 17.0 <= BMI <= 18.4:
    print("mid thinness")
elif 18.5 <= BMI <= 24.9:
    print("normal range")
elif 25.0 <= BMI <= 29.9:
    print("pre_obese")
elif 30.0 <= BMI <= 34.9:
    print("class 1")
elif 35.0 <= BMI <= 39.9:
    print("class 2")
else:
    print("class 3")
