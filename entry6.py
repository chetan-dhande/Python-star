from tkinter import *
Next = Tk()

Calculator_Frame = Frame(Next)
Calculator_Frame.place(x=450, y=220)


def clicked1():

    res1 = (((int(txt1.get())-int(txt2.get()))/int(txt1.get()))+int(txt3.get()))*int(txt3.get())
    Label(Calculator_Frame,text=res1).grid(row=3,column=1)


lbl1 = Label(Calculator_Frame,text="NLL")
lbl2 = Label(Calculator_Frame,text="Vavg")
lbl3 = Label(Calculator_Frame,text="Vrms")
lbl4 = Label(Calculator_Frame,text="C.F.")
lbl5 = Label(Calculator_Frame,text="Power")
lbl1.grid(row=0,column=0)
lbl2.grid(row=1,column=0)
lbl3.grid(row=1,column=2)
lbl4.grid(row=2,column=0)
lbl5.grid(row=2,column=2)

txt1=Entry(Calculator_Frame)
txt2=Entry(Calculator_Frame)
txt3=Entry(Calculator_Frame)
txt4=Entry(Calculator_Frame)

txt1.grid(row=1,column=1)
txt2.grid(row=1,column=3)
txt3.grid(row=2,column=1)
txt4.grid(row=2,column=3)

btn1=Button(Calculator_Frame,text="Calculate",command=clicked1)
btn1.grid(row=3,column=0)


def clicked2():
    res2 = int(txt5.get())/int(txt6.get())
    Label(Calculator_Frame,text=res2).grid(row=8,column=1)


lbl6 = Label(Calculator_Frame,text="Efficiency")
lbl7 = Label(Calculator_Frame,text="O/P")
lbl8 = Label(Calculator_Frame,text="I/P")
lbl6.grid(row=5,column=0)
lbl7.grid(row=6,column=0)
lbl8.grid(row=7,column=0)

txt5=Entry(Calculator_Frame)
txt6=Entry(Calculator_Frame)
txt5.grid(row=6,column=1)
txt6.grid(row=7,column=1)

btn2=Button(Calculator_Frame,text="Calculate",command=clicked2)
btn2.grid(row=8,column=0)


def clicked3():
    res3 = ((int(txt10.get())-int(txt11.get()))/int(txt11.get()))*100
    Label(Calculator_Frame,text=res3).grid(row=8,column=3)


lbl9 = Label(Calculator_Frame,text="Regulation")
lbl10 = Label(Calculator_Frame,text="V1")
lbl11 = Label(Calculator_Frame,text="E1")
lbl9.grid(row=5,column=2)
lbl10.grid(row=6,column=2)
lbl11.grid(row=7,column=2)

txt10=Entry(Calculator_Frame)
txt11=Entry(Calculator_Frame)
txt10.grid(row=6,column=3)
txt11.grid(row=7,column=3)

btn3=Button(Calculator_Frame,text="Calculate",command=clicked3)
btn3.grid(row=8,column=2)


def clicked4():
    res4 = ((int(txt12.get())*310)/(235+int(txt13.get())))
    Label(Calculator_Frame, text=res4).grid(row=13, column=1)


lbl12 = Label(Calculator_Frame, text="Resistance")
lbl13 = Label(Calculator_Frame, text="Rt")
lbl14 = Label(Calculator_Frame, text="T")
lbl12.grid(row=10, column=0)
lbl13.grid(row=11, column=0)
lbl14.grid(row=12, column=0)

txt12 = Entry(Calculator_Frame)
txt13 = Entry(Calculator_Frame)
txt12.grid(row=11, column=1)
txt13.grid(row=12, column=1)

btn4 = Button(Calculator_Frame, text="Calculate", command=clicked4)
btn4.grid(row=13, column=0)


def clicked5():
    res5 = (int(txt5.get())+int(txt6.get()))/2
    Label(Calculator_Frame, text=res5).grid(row=13, column=3)


lbl15 = Label(Calculator_Frame, text="oil BDV")
lbl16 = Label(Calculator_Frame, text="oil 1")
lbl17 = Label(Calculator_Frame, text="oil 2")
lbl5.grid(row=10, column=2)
lbl16.grid(row=11, column=2)
lbl17.grid(row=12, column=2)

txt14 = Entry(Calculator_Frame)
txt15 = Entry(Calculator_Frame)
txt14.grid(row=11, column=3)
txt15.grid(row=12, column=3)

btn5 = Button(Calculator_Frame, text="Calculate", command=clicked5)
btn5.grid(row=13, column=2)

Next.mainloop()