N=int(input("Enter the amount of your bill:"))
if(N>=10000):
    print("Amount before 10% discount:",N)
    n=N*(10/100)
    p=N-n
    print("Amount after 10% discount:",p)
else:
    print("Amount before 7% discount:",N)
    n=N*(7/100)
    p=N-n
    print("Amount after 7% discount:",p)
