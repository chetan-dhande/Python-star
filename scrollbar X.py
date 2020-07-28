from tkinter import *
r=Tk()

s=Scrollbar(r,orient=HORIZONTAL)
s.pack(side=BOTTOM,fill=X)
mylist=Listbox(r,yscrollcommand=s.set)

for i in range(100):
    mylist.insert(END,"Number "+str(i))
    mylist.pack()
    s.configure(command=mylist.xview)

r.mainloop()