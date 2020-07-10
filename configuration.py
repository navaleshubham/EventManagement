from tkinter import *
import tkinter.ttk as ttk
import warnings
warnings.filterwarnings("ignore")
import tkinter as tk
global username
global password
def exitss():
    RAM.destroy()

def getconnection():
    username=E.get()
    password=E1.get()
    fo = open("donottouch.txt", "w")
    fo.write(str(len(username)))
    fo.write(username)
    fo.write(str(len(password)))
    fo.write(password)
    fo.close()
    try:
        from tkinter import messagebox
        messagebox.showinfo("SUCESS", "DATABASE CONNECTION IS SUCESSFUL")
        RAM.destroy()
        from home import homes
        homes()

    except:
        from tkinter import messagebox
        messagebox.showerror("ERROR", "PLEASE ENTER THE DATA CORRECTLY")

RAM = tk.Tk()

RAM.title('DATABASE CONFIGURATION')
RAM.geometry("450x400")
RAM.configure(background='LIGHTBLUE')

l=Label(RAM,text="SARASWATI COLLEGE OF ENGINEERING , KHARGHAR ,NAVI MUMBAI")
l.config(bg='lightblue',fg='purple')
l.place(x=40,y=20)

l1=Label(RAM,text="CONFIGURATION FOR DATABASE")
l1.config(bg='lightblue',fg='purple')
l1.place(x=130,y=50)

l2=Label(RAM,text="USERNAME")
l2.config(bg='lightblue',fg='purple')
l2.place(x=50,y=150)

l3=Label(RAM,text="PASSWORD")
l3.config(bg='lightblue',fg='purple')
l3.place(x=50,y=200)

E=Entry(RAM,width=25)
E.place(x=200,y=150)

E1=Entry(RAM,width=25)
E1.place(x=200,y=200)

b1=Button(RAM,text='SUBMIT',command=getconnection,width='6',height='1')
b1.place(x=150,y=300)

b2=Button(RAM,text='EXIT',command=exitss,width='6',height='1')
b2.place(x=300,y=300)

RAM.mainloop()