n=int(input("Enter a num:"))
rm=0
m=n
while(n>0):
    r=n%10
    rm=rm*10+r
    n=n//10
print("rev:",rm)
if m==rm:
    print ("the num is pailandrom")
else:
    print("it is not pailandrom")
