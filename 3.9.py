print("displaying the sum till you want from 0")
n=int(input("Enter a num:"))
b=0
if(n>0):
    while(n>0):
        b=b+n
        n-=1
else:
    print("Not a natural num")
print(b)
