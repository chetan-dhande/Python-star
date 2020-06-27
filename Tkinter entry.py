from tkinter import *
r=Tk()
r.configure(background="orange")
fname=Label(r,text="User name",fg="yellow",bg="green")
e1=Entry(r)
lname=Label(r,text="Password",bg="green")
e2=Entry(r,show="k")
address=Label(r,text="confirm password",bd=10)
e3=Entry(r,state=DISABLED)
fname.pack()
e1.pack
lname.pack()
e2.pack
address.pack()
e3.pack
r.mainloop()