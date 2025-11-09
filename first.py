from tkinter import *
from tkinter import ttk
c = Tk()
width=c.winfo_screenwidth()
height=c.winfo_screenheight()
c.config(bg='yellow')      #for bg colour
# c.geometry(f'{width}x{height}')
l =Label(c,text="prachiiiiiiiiiiieeeee",bg='maroon',fg='green',font=('sans-serif',16,'bold'),
         height=10,width=30,cursor='plus',relief='ridge')
# l.pack()
# l.grid(row=1,column=10)
l.place(relx=0.4,rely=0.4,width=100,height=100)   #shifting  
# ttk.Label(c,text='welcome').pack()
c.mainloop() 

# 
c.title("firstApp")     #title name
c.iconbitmap(r"C:\Users\hp\Desktop\advance python\gui  graphical interface\icon.ico")   #for icon
c.geometry('1000x600')
c.minsize(width=200,height=200)
c.maxsize(width=1200,height=800)
c.resizable(False,False)    #disable maximize button
c.attributes('-alpha',0.3)      #transparancy
# c.attributes('-disabled',0.3) 
    

c.mainloop() 
