from tkinter import *
r=Tk()
def display():
    selection="value ="+str(var.get())
    label.configure(text=selection)

var=IntVar()
s=Scale(r,variable=var,orient=HORIZONTAL)
s.pack(anchor=CENTER)

button=Button(r,text="Get Scale Value",command=display)
button.pack(anchor=CENTER)

label=Label(r)
label.pack()
r.mainloop()