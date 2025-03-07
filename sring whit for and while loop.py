S1="USA NORTH AMERICA"
S2="USA SOUTH AMERICA"

print(S1)
print(S2)
print("\nThe difference is:")
for i in S1:
    if i in S2:
        print(i,end="")
