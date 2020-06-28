from tkinter import*
root=Tk()
root.configure(background="blue")

myframe=Frame(root,bg="yellow",width=500,height=300)
myframe.pack()

newframe=Frame(root,bg="red",width=500,height=300)
newframe.pack(side=RIGHT)

mylabel=Label(newframe,text="Welcome to DADAR")

mylabel.pack()
root.mainloop()

