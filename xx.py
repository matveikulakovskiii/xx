from tkinter import *
from math import *
import numpy as np
import matplotlib.pyplot as plt 



def lahenda():
    if ent.get()=="": 
        ent.configure(bg="red")
    else:
        ent.configure(bg="lightblue")
    if ent2.get()=="": 
        ent2.configure(bg="red")
    else:
        ent2.configure(bg="lightblue")
    if ent3.get()=="": 
        ent3.configure(bg="red")
    else:
        ent3.configure(bg="lightblue")
    if ent.get()!="" and ent2.get()!="" and ent3.get()!="":
        ent_=float(ent.get())
        ent2_=float(ent2.get())
        ent3_=float(ent3.get())
        D=ent2_*ent2_-4*ent_*ent3_
        if D>0:
            x1=round((-ent2_-sqrt(D))/(2*ent_),2)
            x2=round((-ent2_+sqrt(D))/(2*ent_),2)
            vas=f"X1={x1} \nX2={x2}"
        elif D==0:
            x1=round((-1*ent2_)/(2*ent_),2)
            vas=f"X1={x1}"
        else:
            vas="Lahendust pole"
        vastus.configure(text=vas)

def valik():
    val=var.get()
    ent.insert(END,val)

def graafik():
    a_=float(ent.get())
    b_=float(ent2.get())
    c_=float(ent3.get())
    x0=(-b_)/2*a_
    y0=a_*x0*x0+b_*x0+c_
    x=np.arange(x0-15,x0+15,1)
    y=a_*x*x+b_*x+c_
    fig=plt.figure()
    plt.plot(x,y,'r-d')
    plt.title("Ruutvõrrand")
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.grid(True)
    plt.show()

def checklist_to_l():
    v1=var1.get()
    v2=var2.get()
    jarjend=[v1,v2]
    l.delete(0,1)
    for item in jarjend:
        l.insert(END,item)



aken=Tk()
aken.geometry("800x800")
aken.title("Rootvõrrandid")
aken.iconbitmap('index.ico')
f1=Frame(aken,width=650,height=260)
f1.pack(side=TOP)
f2=Frame(aken,width=650,height=200)
f2.pack(side=BOTTOM)


lbl=Label(f1,text="Rootvõrrandite lahendamine",font="Times_New_Roman 26", fg="green",bg="lightblue")
vastus=Label(f1,text="vastus", height=3,width=20,bg="yellow")
ent=Entry(f1,font="Times_new_roman 26", fg="grey",bg="lightblue",width=3)
lbl2=Label(f1,text="x**2+",font="Times_new_roman 26", fg="blue", padx=10)
ent2=Entry(f1,font="Times_new_roman 26", fg="grey",bg="lightblue",width=3)
lbl3=Label(f1,text="x+",font="Times_new_roman 26", fg="blue")
ent3=Entry(f1,font="Times_new_roman 26", fg="grey",bg="lightblue",width=3)
lbl4=Label(f1,text="=0",font="Times_new_roman 26", fg="blue")
btn=Button(f1,text="Lahenda", font="Times_new_roman 26",bg="gold",command=lahenda)
btn2=Button(f1,text="Graafik", font="Times_new_roman 26",bg="gold",command=graafik)
btn_veel=Button(f2,text="Suurendada aken", font="Times_new_roman 26",bg="gold")
var=IntVar() #StringVar
r1=Radiobutton(aken,text='Esimene',font="Algerian 20",variable=var,value=1,command=valik)
r2=Radiobutton(aken,text='Teine',font="Algerian 20",variable=var,value=2,command=valik)
r3=Radiobutton(aken,text='Kolmas',font="Algerian 20",variable=var,value=3,command=valik)
var1=StringVar()
var2=StringVar()
c1=Checkbutton(aken,text='Esimene',font="Algerian 20",variable=var1,onvalue='Esimene pn valitud',offvalue='Esimene on peidetud')
c2=Checkbutton(aken,text='Esimene',font="Algerian 20",variable=var2,onvalue='Teine pn valitud',offvalue='Teine on peidetud')
l=Listbox(aken,height=3,width=20)



btn.bind('<Button-2>', checklist_to_l)
lbl.pack(side=TOP)
vastus.pack(side=BOTTOM)
ent.pack(side=LEFT)
lbl2.pack(side=LEFT)
ent2.pack(side=LEFT)
lbl3.pack(side=LEFT)
ent3.pack(side=LEFT)
lbl4.pack(side=LEFT)
btn2.pack(side=RIGHT)
btn.pack(side=RIGHT)
btn_veel.pack()
r1.pack()
r2.pack()
r3.pack()
l.pack()
c2.deselect()
c1.deselect()
c2.deselect()

aken.mainloop()

