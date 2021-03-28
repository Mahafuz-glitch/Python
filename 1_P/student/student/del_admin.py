
from tkinter import *
import sqlite3
from db_delete import *
#####################################################################################################

# THIS IS administrator page
def u_del_acc():
    ###############################################################################
    #CALL DELETE FUNCTION TO DELETE USER ACCOUNT
    def a_acc_del():
        acc_del(e1.get())
        e1.delete(0,END)

    
    ###############################################################################
    #CALL DELETE FUNCTION TO DELETE A BOOK FROM A LIST OF BOOK
    def a_bk_del():
        bk_del(e2.get())
        e1.delete(0,END)
    

    
    ###############################################################################
    
    
    root=Tk()
    root.configure(background='#ffb3b3',relief=RAISED)
    root.title("OLD BOOK STALL")
    root.geometry("600x400+400+150")
    root.resizable(0,0)
    l1=Label(root,text="ENTER THE USER ID",bg="#4d0000",fg="white",font=("impact",20),width="20")
    l1.grid(row=0,column=0,pady=0,padx=10)
    e1=Entry(root,bg="white",fg="black",font=("impact",20),width="20")
    e1.grid(row=0,column=1,pady=10,padx=10)
    b1=Button(root,text="DELETE ACCOUNT",bg="#ff3333",fg="White",font=("impact",20),width="20",height='1',relief=RAISED,command=a_acc_del)
    b1.grid(row=1,column=1,pady=0,padx=10,sticky=N)

    l2=Label(root,text="ENTER THE BOOK ID",bg="#4d0000",fg="white",font=("impact",20),width="20")
    l2.grid(row=2,column=0,pady=0,padx=10)
    e2=Entry(root,bg="white",fg="black",font=("impact",20),width="20")
    e2.grid(row=2,column=1,pady=20,padx=10)        
    b2=Button(root,text="DELETE BOOK",bg="#ff3333",fg="White",font=("impact",20),width="20",height='1',relief=SUNKEN,command=a_bk_del)
    b2.grid(row=3,column=1,pady=0,padx=10)


########################################################################################################

    root.mainloop()
