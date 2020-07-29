from tkinter import *
r=Tk()

s=Scrollbar(r,orient=VERTICAL)
s.pack(side=RIGHT,fill=Y)
mylist=Listbox(r,yscrollcommand=s.set)

for i in range(100):
    mylist.insert(END,"Number "+str(i))
    mylist.pack()
    s.configure(command=mylist.yview)

r.mainloop()