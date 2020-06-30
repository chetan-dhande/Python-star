from tkinter import *
from tkinter.ttk import *
w=Tk()
c=Combobox(w)
c['values']=("Language","Java","Python","C#",".Net")
c.current(0)
d=Combobox(w,values=["Mango","Apple","Banana"],font="Times 15 bold italic",state="readonly")
c.pack()
d.pack()
w.mainloop()
