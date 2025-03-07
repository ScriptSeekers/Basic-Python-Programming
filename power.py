def cp(base, exponent):
    POWER=base ** exponent
    return POWER
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))
result = cp(base, exponent)
print("The result of ",base," raised to the power of ",exponent,"is:",result)
