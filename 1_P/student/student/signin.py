from tkinter import *
import sqlite3
from in_user import*
from db_signin import *
from tkinter import messagebox
#####################################################################################################

# THIS IS SIGNIN PAGE TO GET USER NAME AND PASSWORD FROM USER
def a_signin():
    root=Tk()
    root.configure(background='#f5ccff',relief=RAISED)
    root.title("OLD BOOK STALL")
    root.geometry("600x400+400+150")
    root.resizable(0,0)
    #############################################################
    #SIGN IN CHECK UP
    def signin_check():
        r=u_check(e1.get(),e2.get())
        if(r>0):
            u_in_user()
            e1.delete(0,END)    
            e2.delete(0,END)
        else:
            messagebox.showinfo("WRONG ENTRY","INVALID ACCOUNT")
 



    #############################################################

    l0=Label(root,text="SIGN in",bg="#660066",fg="White",font=("impact",20),width="45",height='1',justify="right")
    l0.grid(row=0,column=0,columnspan=2)

    l1=Label(root,text="NAME",bg="#660066",fg="White",font=("impact",20),width="20",height='1',justify="left",anchor='w')
    l1.grid(row=1,column=0)
    e1=Entry(root,bg="#ffb3ff",fg="black",font=("impact",20),width="20")
    e1.grid(row=1,column=1,pady=10,padx=0)

    l2=Label(root,text="PASSWORD",bg="#660066",fg="White",font=("impact",20),width="20",height='1',anchor='w')
    l2.grid(row=2,column=0,)
    e2=Entry(root,bg="#ffb3ff",show='*',fg="black",font=("impact",20),width="20")
    e2.grid(row=2,column=1,pady=10,padx=0)



    b1=Button(root,text="SIGN IN",bg="#330033",fg="White",font=("impact",20),width="20",command=signin_check)
    b1.grid(row=3,column=0,pady=10,padx=0,columnspan=4)

########################################################################################################

    root.mainloop()
