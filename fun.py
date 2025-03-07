def add(a,b):
    s=a+b
    print("ADDITION=",s)
def sub(a,b):
    s=a-b
    print("SUBSTRACTION=",s)
def mul(a,b):
    s=a*b
    print("MULTIPLICATION=",s)
def div(a,b):
    s=a/b
    print("DIVISION=",s)
print("MENU\n1.ADDITION\n2.SUBSTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.EXIT")
c=int(input("Enter your choice:"))
if(c<5 and c>=1):
    a=int(input("Enter num:"))
    b=int(input("Enter num:"))
    if(c==1):
        add(a,b)
    elif(c==2):
        sub(a,b)
    elif(c==3):
        mul(a,b)
    else:
        div(a,b)
elif(c==5):
    print("THE PROGRAM IS TERMINATED")
else:
    print("INVALID INPUT")
print("End of program")
