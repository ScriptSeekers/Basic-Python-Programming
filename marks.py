def marks(phy,chem,bio,math):
    total=phy+chem+bio+math
    percent=(total/400)*100
    print("Total marks:",total)
    print("Percent:",percent,"%")
print("Enter your marks")
a=int(input("Enter your marks in PHYSICS:"))
b=int(input("Enter your marks in CHEMESTRIY:"))
c=int(input("Enter your marks in BIOLOGY:"))
d=int(input("Enter your marks in MATHS:"))
marks(a,b,c,d)
