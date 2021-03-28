from tkinter import messagebox
from tkinter import *
import sqlite3
from db_signup import *
#####################################################################################################

# THIS IS SIGN UP PAGE THERE ARE 4 ENTRY YOU HAVE TO FILL UP ABOUT USE TO GET AN USER ID 1-NAME 2-PHONE NUMBER 3-ADDRESS 4-PASSWORD
def a_signup():
    root=Tk()
    root.configure(background='#ffcccc',relief=RAISED)
    root.title("OLD BOOK STALL")
    root.geometry("600x400+400+150")
    root.resizable(0,0)
####################################################################################################

    
#name=StringVar()
#phone=StringVar()
#add=StringVar()
#password=StringVar()

#THIS FUNCTION TRANSFER USER INPUT INTO A FUNCTION OF SIGNUP DATABASE FILE    
    def pre_signup():
        #global name
        #global phone
        #global add
        #global password
        u_create_table()
        #c_id=u_insert_data(e1.get(),e2.get(),e3.get(),e4.get())
        #VALIDATION
        name=e1.get()
        phone=e2.get()
        password=e4.get()
        if all(i.isalpha() or i.isspace()for i in name)and name[0]!=" ":
            if(phone.isdigit()):
                if(len(password)>=8):
                    c_id=u_insert_data(e1.get(),e2.get(),e3.get(),e4.get())
                    messagebox.showinfo("YOUR UNIQUE USER ID",c_id)
                else:
                    messagebox.showinfo("PASSWORD TOO SHORT","Enter proper password ")
            else:
                messagebox.showinfo("WRONG ENTRY","Enter proper number ")
        else:
            messagebox.showinfo("WRONG ENTRY","Enter proper name ")
           
    #tkMessageBox.showinfo("your user id", i)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        
        




####################################################################################################    

    l0=Label(root,text="SIGN UP",bg="#990000",fg="White",font=("impact",20),width="45",height='1',justify="right")
    l0.grid(row=0,column=0,columnspan=2)

    l1=Label(root,text="NAME",bg="#990000",fg="White",font=("impact",20),width="15",height='1',justify="left",anchor='w')
    l1.grid(row=1,column=0)
    e1=Entry(root,bg="#ff4d4d",fg="White",font=("impact",20),width="20")#,textvariable=name)
    e1.grid(row=1,column=1,pady=10,padx=0)

    l2=Label(root,text="PHONE",bg="#990000",fg="White",font=("impact",20),width="15",height='1',anchor='w')
    l2.grid(row=2,column=0,)
    e2=Entry(root,bg="#ff4d4d",fg="White",font=("impact",20),width="20")#,textvariable=phone)
    e2.grid(row=2,column=1,pady=10,padx=0)

    l3=Label(root,text="ADDRESS",bg="#990000",fg="White",font=("impact",20),width="15",height='1',anchor='w')
    l3.grid(row=3,column=0,)
    e3=Entry(root,bg="#ff4d4d",fg="White",font=("impact",20),width="20")#,textvariable=add)
    e3.grid(row=3,column=1,pady=10,padx=0)

    l4=Label(root,text="PASSWORD",bg="#990000",fg="White",font=("impact",20),width="15",height='1',anchor='w')
    l4.grid(row=4,column=0,)
    e4=Entry(root,bg="#ff4d4d",fg="White",font=("impact",20),width="20")#,textvariable=password)
    e4.grid(row=4,column=1,pady=10,padx=50)

    b1=Button(root,text="SIGN UP",bg="#330000",fg="White",font=("impact",20),width="20",command=pre_signup)
    b1.grid(row=5,column=0,pady=10,padx=0,columnspan=4)
    root.mainloop()
########################################################################################################

    













    





























    

    
