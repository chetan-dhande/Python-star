from tkinter import *
r=Tk()
lbl=Label(r,text="User Name")
myentry=Entry(r,fg="yellow",bg="green",bd=20,font="Time 19 bold",cursor="star",relief=RIDGE)
lbl.pack()
myentry.pack()
r.mainloop()