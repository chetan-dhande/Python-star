from tkinter import *
r=Tk()

rootmenu=Menu(r)
r.configure(menu=rootmenu)

f=Menu(rootmenu)
rootmenu.add_cascade(label="file",menu=f)
f.add_command(label="new")
f.add_command(label="open")
r.mainloop()