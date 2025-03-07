#Normal slicing method
a="ScriptSeekers"
print(a[::])
print(a[::-1])
print(a[-1:0:-1])
print(a[:4])
print(a[3:])
print(a[:-1])
print(" ")

#ConCatination
a="Script"
b="Seekers"
print(a+b)
print("")

#printing Multipal time
a="hello\n"
print(a*2)

#Searching
a="Information Thecnology"
print("Thecnology" in a)
print("Arpit" in a)
print("Vishwakarma" not in a)
print("")

#string operation
A="ABCD"
a="abcd"
print(A==a)
print(A<a)
print(A>a)
print(A!=a)
print("")

#spliting
a="C ,C++ ,JAVASCREIPT ,HTML ,CSS"
print(a.split())
print("")

#string testing
s="ABC123"
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.isupper())
print(s.islower())
print(s.isspace())
print("")

#searching sub string
S="SCRIPTSEEKERS"
print(S.startswith("SCR"))
print(S.endswith("ERS"))
print(S.find("S"))
print(S.rfind("SEE"))
print(S.count("S" or "E"))
