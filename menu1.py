from tkinter import *
r=Tk()

rootmenu=Menu(r)
r.configure(menu=rootmenu)

f=Menu(rootmenu)
e=Menu(rootmenu)
h=Menu(rootmenu)


rootmenu.add_cascade(label="file",menu=f)
f.add_command(label="new")
f.add_command(label="open")
f.add_command(label="save")
f.add_command(label="save as")
f.add_command(label="close")

rootmenu.add_cascade(label="Edit",menu=e)
e.add_command(label="cut")
e.add_command(label="copy")
e.add_command(label="paste")
e.add_command(label="select")
e.add_command(label="select all")

rootmenu.add_cascade(label="Help",menu=h)
h.add_command(label="about")



r.mainloop()