from tkinter import *
r=Tk()
lbl1=Label(r,text="First Name :")
lbl2=Label(r,text="Last Name :")
lbl3=Label(r,text="User Name :")
lbl4=Label(r,text="Password :")

e1=Entry(r)
e2=Entry(r)
e3=Entry(r)
e4=Entry(r)

btn=Button(r,text="Submit")

lbl1.grid(row=0,column=0)
e1.grid(row=0,column=1)
lbl2.grid(row=1,column=0)
e2.grid(row=1,column=1)
lbl3.grid(row=2,column=0)
e3.grid(row=2,column=1)
lbl4.grid(row=3,column=0)
e4.grid(row=3,column=1)

btn.grid(row=4,column=1)

r.mainloop()