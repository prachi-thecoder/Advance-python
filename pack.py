from tkinter import *
from tkinter import ttk
c= Tk()
c.title('prachiiie')
c.iconbitmap(r"C:\Users\hp\Desktop\advance python\gui  graphical interface\shinchan.ico")
# l=Label(c,text='shinchan',fg='red',bg='green',font=('sans-serif',20,'bold'))
# l1=Label(c,text='prachie',fg='yellow',bg="red",font=('sans-serif',20,'bold'))
# l2=Label(c,text='mhaske',fg='pink',bg="grey",font=('sans-serif',20,'bold'))
# l3=Label(c,text='duggu',fg='blue',bg="purple",font=('sans-serif',20,'bold'))
# l.pack(padx=20,pady=20,ipadx=20,ipady=20,side='left',fill='y')
# l1.pack(padx=20,pady=20,ipadx=20,ipady=20,side='right',fill='y')
# l2.pack(padx=20,pady=20,ipadx=20,ipady=20,side='bottom')
# l3.pack(padx=20,pady=20,ipadx=20,ipady=20,side='top')


u=input("enter a text:")
ll=Label(c,text=u,fg='red',bg='yellow')
ll.pack(padx=20,pady=20,ipadx=20,ipady=20,side='top')
c.mainloop()