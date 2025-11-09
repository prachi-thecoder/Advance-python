from tkinter import *
from tkinter import ttk
import datetime
c= Tk()
c.title('button')
c.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
btn=Button(c,text="click",height=2,width=5,bg='green',fg='white',font=("sans-serif",30,'bold')
           ,cursor='plus',relief="ridge",activebackground='yellow',activeforeground="pink",bd=5)

# button with function
from tkinter import *
from tkinter import ttk
import datetime
c= Tk()
c.title('button')
c.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def show():
    btn.config(text="open")
btn=Button(c,text="click",command=show,height=2,width=5,bg='green',fg='white',font=("sans-serif",30,'bold')
           ,cursor='plus',relief="ridge",activebackground='yellow',activeforeground="pink",bd=5)
btn.pack()
c.mainloop()

# button with parameterised function(lambda)
from tkinter import *
from tkinter import ttk
c=Tk()
c.title('button')
c.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
a="click"
def name(a):
    btn.config(text=f'hello {a}')
btn=Button(c,text="click",command=lambda:name(a),height=2,bg='green',fg='white',font=("sans-serif",30,'bold')
           ,cursor='plus',relief="ridge",activebackground='yellow',activeforeground="pink",bd=5)
btn.pack()
c.mainloop()
# multiple button with command
from tkinter import *
from tkinter import ttk
c=Tk()
c.title('button')
c.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
l=Label(c,text="click",bg='pink',height=5,width=20,font=('sans-sarif',20,'bold'))
def hey():
    l.config(text="hey")
def by():
    l.config(text="bye")
btn=Button(c,text="hey",command=hey,height=2,bg='green',fg='white',font=("sans-serif",30,'bold')
           ,cursor='plus',relief="ridge",activebackground='yellow',activeforeground="pink",bd=5)
btn1=Button(c,text="bye",command=by,height=2,bg='green',fg='white',font=("sans-serif",30,'bold')
       ,cursor='plus',relief="ridge",activebackground='yellow',activeforeground="pink",bd=5)
l.pack(fill='x')
btn.pack()
btn1.pack()
c.mainloop()

# button with state
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
btn=Button(t,text="hey",height=2,bg='green',fg='white',font=("sans-serif",30,'bold')
           ,cursor='plus',relief="ridge",activebackground='yellow',activeforeground="pink",bd=5,state='disabled')
btn.pack()
btn1=Button(t,text="hey",height=2,bg='green',fg='white',font=("sans-serif",30,'bold')
           ,cursor='plus',relief="ridge",activebackground='yellow',activeforeground="pink",bd=5,state='normal')
btn1.pack()
btn2=Button(t,text="hey",height=2,bg='green',fg='white',font=("sans-serif",30,'bold')
           ,cursor='plus',relief="ridge",activebackground='yellow',activeforeground="pink",bd=5,state='active')
btn2.pack()
t.mainloop()

#event handling  left click 
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def left_click(event):
    l.config(text="leftclick")
l=Label(t,text="",bg="red")
l.pack()
btn=Button(t,text="hey",height=2,bg='green',fg='white')
btn.bind("<Button-1>",left_click)
btn.pack()
t.mainloop()

# for right 
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def right_click(event):
    l.config(text="rightclick")
l=Label(t,text="",bg="red")
l.pack()
btn=Button(t,text="hey",height=2,bg='green',fg='white')
btn.bind("<Button-3>",right_click)
btn.pack()
t.mainloop()

# middle click
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def middle_click(event):
    l.config(text="middle")
l=Label(t,text="",bg="red")
l.pack()
btn=Button(t,text="hey",height=2,bg='green',fg='white')
btn.bind("<Button-2>",middle_click)
btn.pack()
t.mainloop()

# double click
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def double_click(event):
    l.config(text="leftclick")
l=Label(t,text="",bg="red")
l.pack()
btn=Button(t,text="hey",height=2,bg='green',fg='white')
btn.bind("<Double-1>",double_click)
btn.pack()
t.mainloop()

# 
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def double_click(event):
    l.config(text="doublerightclick")
l=Label(t,text="",bg="red",height=5,width=20)
l.pack()
btn=Button(t,text="hey",height=2,bg='green',fg='white')
btn.bind("<Double-3>",double_click)
btn.pack()
t.mainloop()
 
# enter
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def double_click(event):
    l.config(text="enter on button area")
l=Label(t,text="",bg="red",height=5,width=20)
l.pack()
btn=Button(t,text="hey",height=2,bg='green',fg='white')
btn.bind("<Enter>",double_click)
btn.pack()
t.mainloop()

# leave
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def leave_click(event):
    l.config(text="leave from button area")
l=Label(t,text="",bg="red",height=5,width=20)
l.pack()
btn=Button(t,text="hey",height=2,bg='green',fg='white')
btn.bind("<Leave>",leave_click)
btn.pack()
t.mainloop()

# motion
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def motion_click(event):
    l.config(text="motion")
l=Label(t,text="",bg="red",height=5,width=20)
l.pack()
btn=Button(t,text="hey",height=2,bg='green',fg='white')
btn.bind("<Motion>",motion_click)
btn.pack()
t.mainloop()

# keyboard event
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def key(event):
    l.config(text="any key press")
l=Label(t,text="",bg="red",height=5,width=20)
l.pack()
btn=Button(t,text="hey",height=2,bg='green',fg='white')
t.bind("<Key>",key)
btn.pack()
t.mainloop()
# FOCUS FUNCTION
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def key(event):
    l.config(text="any key press")
l=Label(t,text="",bg="red",height=5,width=20)
l.pack()
btn=Button(t,text="hey",height=2,bg='green',fg='white')
btn.bind("<Key>",key)
btn.focus()
btn.pack()
t.mainloop()

# particular key 
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def key_click(event):
    l.config(text="A key is press")
l=Label(t,text="",bg="red",height=5,width=20)
l.pack()
btn=Button(t,text="hey",height=2,bg='green',fg='white')
t.bind("<KeyPress-a>",key_click)
btn.pack()
t.mainloop()
 
#return
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def key_click(event):
    l.config(text="enter key press")
l=Label(t,text="",bg="red",height=5,width=20)
l.pack()
btn=Button(t,text="hey",height=2,bg='green',fg='white')
t.bind("<Return>",key_click)
btn.pack()
t.mainloop()

# space
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def key_click(event):
    l.config(text="A space key is press")
l=Label(t,text="",bg="red",height=5,width=20)
l.pack()
btn=Button(t,text="hey",height=2,bg='green',fg='white')
t.bind("<space>",key_click)
btn.pack()
t.mainloop()
 
# even charcter
from tkinter import *
from tkinter import ttk
t=Tk()
t.title("heyyyy")
t.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
def key_click(event):
    l.config(text="A space key is press")
    print(event.type)
    print(event.x,event.y)
    print(event.widget)
    print(event.keysym)
    print(event.char)
    print(event.num)
l=Label(t,text="",bg="red",height=5,width=20)
l.pack()
btn=Button(t,text="hey",height=2,bg='green',fg='white')
t.bind("<Button-1>",key_click)
btn.pack()
t.mainloop()
 

 

 

 

 

 

 

 

 
