n=1
while(n<=1000):
    d=n
    c=0
    e=n
    while(e>0):
        a=e%10
        b=a*a*a
        c=b+c
        e=e//10
    if(d==c):
        print(c,"Is an armstrong num")
    n+=1
n=int(input("Enter a num:"))
a=b=c=0
e=n
while(e>0):
        a=e%10
        b=a*a*a
        c=b+c
        e=e//10
if(n==c):
        print(c,"Is an armstrong num")
