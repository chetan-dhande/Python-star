from tkinter import *
r=Tk()
r.configure(background="orange")
fname=Button(r,text="first name",fg="yellow",bg="green")
lname=Button(r,text="last name",fg="blue",bg="green")
address=Button(r,text="Address",bd=10)
id=Button(r,text="ID",padx=70)
dob=Button(r,text="Date of Birth",padx=50)
fname.pack()
lname.pack()
id.pack()
address.pack()
dob.pack()
r.mainloop()