#from tkinter import *
"""
    when button styling is there
"""

import tkinter as tk

root=tk.Tk() #creating window

def show():#fun() to get asve in database
    print("My Username:",e1.get())
    print("My Password:",e2.get())
    
    #only work like this
    """
        l2=tk.Label(root,text="PASSWORD:")
        l2.grid(row=1,column=0)
        e2=tk.Entry()
        e2.grid(row=1,column=1)
    """
    
    #can't work like this
    """
        l2=tk.Label(root,text="PASSWORD:").grid(row=1,column=0)
        e2=tk.Entry().grid(row=1,column=1)
    """
    

root.title("Wellcome to GUI")

"""
    PACK align element defalut
    GRID align according rows and col
    GEOMETRY align according northeast,southwest,east,west
    can't use any combination
    only one is in the function in gui
"""

l1=tk.Label(root,text="USERNAME:")
l1.grid(row=0,column=0)
e1=tk.Entry()
e1.grid(row=0,column=1)

l2=tk.Label(root,text="PASSWORD:")
l2.grid(row=1,column=0)
e2=tk.Entry()
e2.grid(row=1,column=1)

b1=tk.Button(root,text="LOGIN",bg="pink",fg="red",command=show).grid(row=2,column=1)

#types of button styling
"""
    b1=tk.Button(root,text="Relife style:Flat",relief=FLAT)
    b1=tk.Button(root,text="Relife style:Raised",relief=RAISED)
    b1=tk.Button(root,text="Relife style:Sunken",relief=SUNKEN)
    b1=tk.Button(root,text="Relife style:Groove",relief=GROOVE)
    b1=tk.Button(root,text="Relife style:Reidge",relief=RIDGE)
"""

#types of bit map
"""
    b1=tk.Button(root,text="error",relief=RAISED,bitmap="error")
    b1=tk.Button(root,text="hourglass",relief=RAISED,bitmap="hourglass")
    b1=tk.Button(root,text="info",relief=RAISED,bitmap="info")
    b1=tk.Button(root,text="question",relief=RAISED,bitmap="question")
    b1=tk.Button(root,text="warning",relief=RAISED,bitmap="warning")
"""

#types of cursor
"""
    b1=tk.Button(root,text="puls",relief=RAISED,cursor="puls")
    b1=tk.Button(root,text="heart",relief=RAISED,cursor="heart")
    b1=tk.Button(root,text="spray",relief=RAISED,cursor="spray")
    b1=tk.Button(root,text="clock",relief=RAISED,cursor="clock")
"""

root.mainloop()
