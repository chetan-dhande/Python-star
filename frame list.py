from tkinter import *
r=Tk()
mylist=Listbox(r)
mylist.insert(1,"python")
mylist.insert(2,"java")
mylist.insert(3,"android")
mylist.pack()

e1=Entry(r,bd=6)
e1.pack()

def insert_element():
    mylist.insert(4,e1.get())

def display():
    d=mylist.curselection()
    print(mylist.get(d))
    Label(r,text="You selected"+str(mylist.get(d))).pack()

btn1=Button(r,text="insert",command=insert_element)
btn1.pack()

btn2=Button(r,text="display",command=display)
btn2.pack()

r.mainloop()
