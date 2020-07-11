from tkinter import *
window=Tk()
window.title("Welcome to Impetus Consultrainer")
def clicked():
    res="Welcome "+txt.get()+" to mumbai"
    lbl.configure(text=res)
    Label(window,text="Welcome to Dadar").grid(row=3,column=0)
lbl=Label(window,text="Hello")
txt=Entry(window)
btn=Button(window,text="Click Me",command=clicked)

lbl.grid(row=0,column=0)
txt.grid(row=1,column=0)
btn.grid(row=2,column=0)

window.mainloop()