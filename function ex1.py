import math
height=int(input("enter height:"))
width=int(input("enter width:"))
def paint(h,w,c=7):
    area=h*w
    paint_tin=area/c
    print(f"you need {math.ceil(paint_tin)} paint bottols")#1.7=2,3.1=4
#paint(height,width)
paint(w=width,h=height)