import os
f="ex.txt"
if os.path.exists(f):
    print(os.path.getsize(f))
    print(os.path.getctime(f))
    print(os.path.getmtime(f))
    print(os.path.getatime(f))
else:
    print("ERROR !")
