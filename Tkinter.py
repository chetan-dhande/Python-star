from tkinter import *
r=Tk()
r.configure(background="orange")
fname=Label(r,text="first name",fg="yellow",bg="green")
lname=Label(r,text="last name",bg="green")
address=Label(r,text="address",bd=10)
id=Label(r,text="id",padx=70)
dob=Label(r,text="Date of birth",padx=60)

fname.pack()
lname.pack()
id.pack()
address.pack()
dob.pack()
r.mainloop()