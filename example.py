# from tkinter import *
# from tkinter import ttk
# import datetime as d
# c= Tk()
# c.title("datetime")
# c.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
# p=d.datetime.now()
# m=p.minute
# l=Label(c,text=f'{p.hour}:{m}:{p.second}',fg='black',bg='pink')
# l.pack()
# c.mainloop()

# create timer using tkinter
# from tkinter import *
# from tkinter import ttk
# import datetime as d
# c= Tk()
# c.title("timer")
# c.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
# # t='10'
# l=Label(c,text='10',bg='black',fg='white',height=10,width=50,font=('sans-serif',30))
# l.pack()
# t=10
# def updatetime():
#     global t
#     if(t>0):
#         l.config(text=f"timer:{t}")
#         t=t-1
#         c.after(1000,updatetime)       #milesecon,funname
#     else:
#         l.config(text='timeoff',bg='red')
# updatetime()
# c.mainloop()
# change the background colour when user click on button 
# from tkinter import *
# from tkinter import ttk
# import datetime
# c= Tk()
# c.title('button')
# c.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
# def change():
#     btn.config(text="open",bg='yellow')
# btn=Button(c,text="click",command=change,height=2,width=5,bg='green',fg='white',font=("sans-serif",30,'bold')
#            ,cursor='plus',relief="ridge",activebackground='yellow',activeforeground="pink",bd=5)
# btn.pack()
# c.mainloop()
# # 
# from tkinter import *
# from tkinter import ttk
# import datetime
# p= Tk()
# p.title('button')
# p.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
# l=Label(p,text="you selected",bg="pink",height=5,bd="5")
# a="red"
# b="yellow"
# c="green"
# def b1(a):
#     p.config(bg='red')
#     l.config(text=f"you selected:{a}",bg="red",relief="solid")
# def b2(b):
#     p.config(bg="yellow")
#     l.config(text=f"you selected:{b}",bg="yellow",relief="solid")
# def b3(c):
#     p.config(bg="green")
#     l.config(text=f"you selected:{c}",bg="green",relief="solid")
# btn=Button(p,text="red",command=lambda:b1(a),height=2,width=5,fg='orange',font=("sans-serif",30,'bold')
#            ,cursor='plus',relief="ridge",activebackground='yellow',activeforeground="pink",bd=5)
# btn1=Button(p,text="yellow",command=lambda:b2(b),height=2,width=5,fg="orange",bg='white',font=("sans-serif",30,'bold')
#            ,cursor='plus',relief="ridge",activebackground='yellow',activeforeground="pink",bd=5)
# btn2=Button(p,text="green",command=lambda:b3(c),height=2,width=5,fg='orange',font=("sans-serif",30,'bold')
#            ,cursor='plus',relief="ridge",activebackground='yellow',activeforeground="pink",bd=5)
# l.pack(fill='x')
# btn.pack()
# btn1.pack()
# btn2.pack()
# p.mainloop()

# make headline
# from tkinter import *
# from tkinter import ttk
# win=Tk()
# win.title("NEWSCHANNEL")
# win.config(bg='black')
# win.iconbitmap(r"C:\Users\hp\Desktop\advance python\gui  graphical interface\elsa.ico")
# l=Label(win,text="PYTHON DEVELOPER",bg="pink",fg='black',height=5,width=30,bd=10,relief='raised')
# l.place(x=15,y=15)
# x=10
# def updatetime():
#     global x
#     if(x<1500):
#         # l.config(win,text="PYTHON DEVELOPER",bg="red",fg='black')
#         x=x+10
#         l.place(x=x,y=15)
#         win.after(70,updatetime)
#     else:
#         x=0
#         x=x+10
#         l.place(x=x,y=15)
#         win.after(50,updatetime)
# updatetime()
# win.mainloop()

#take 2 button enable and disable and when user click disable button make it disable 
# from tkinter import *
# from tkinter import ttk
# t=Tk()
# t.title("heyyyy")
# t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
# def button():
#     btn2.config(state='disabled')
# btn=Button(t,text="enable",height=2,bg='green',fg='white',font=("sans-serif",30,'bold')
#            ,cursor='plus',relief="ridge",activebackground='yellow',activeforeground="pink",bd=5,state='active')
# btn.pack()
# btn2=Button(t,text="disable",height=2,bg='green',fg='white',font=("sans-serif",30,'bold')
#            ,cursor='plus',relief="ridge",activebackground='yellow',activeforeground="pink",bd=5,state='active',command=button)
# btn2.pack()
# t.mainloop()

#count the no of visiter press left side
# from tkinter import *
# from tkinter import ttk
# t=Tk()
# t.title("heyyyy")
# t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
# count = 0
# def key(event):
#     global count
#     count=count+1
#     l.config(text=f"{count}")
# l=Label(t,text="0",bg="red",height=5,width=20)
# l.pack()
# btn=Button(t,text="hey",height=2,bg='green',fg='white')
# btn.bind("<Button-1>",key)
# btn.pack()
# t.mainloop() 

# create a label with some text and background color when mouse enters the label area change the backgroud color to green
# when mouse leaves the label change the bg color to blue
# from tkinter import *
# from tkinter import ttk
# t=Tk()
# t.title("heyyyy")
# t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
# def fun(event):
#     l.config(bg="green")
# def fun1(event):
#     l.config(bg="blue")
# l=Label(t,text="label",height=5,width=20)
# # btn=Button(t,text="button",bg="blue",fg="white")
# l.pack()
# # btn.pack()
# l.bind("<Enter>",fun)
# l.bind("<Leave>",fun1)
# t.mainloop()

# create a button with text key not set when user presses key r change bg color ofwindow to red and text on button to red
# when user press g window color change to green and text on button change to green when user press key b 
# then chnage bg blue and text blue when user presses except 3 keys button text change to text not chnage bg color white 
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def fun1(event):
    chr=event.keysym.lower()
    if(chr=="r"):
        t.config(bg="red")
        btn.config(text="red")
    elif(chr=="g"):
        t.config(bg="green")
        btn.config(text="green")
    elif(chr=="b"):
        t.config(bg="blue")
        btn.config(text="blue")
    else:
        t.config(bg="white")
        btn.config(text="textisnotset")

btn=Button(t,text="textisnotset",bg="yellow",fg="black")
btn.pack()
t.bind("<Key>",fun1)
t.mainloop()