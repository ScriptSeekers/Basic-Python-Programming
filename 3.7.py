n=int(input("Enter a num:"))
m=n
b=0
while(n>0):
    a=n%10
    b=b+a**3
    n=n//10
if (m==b):
    print("Armstrong")
else:
    print("not Armsrong")

