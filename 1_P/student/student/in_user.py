
from tkinter import *
import sqlite3
from sale import *
from db_signin import *
#####################################################################################################

# THIS IS USER INSIDE PAGE TO SHOW USER 4 BUTTON, THAT IS CHECK  1-SALE BOOK 2-FULL DATABASE 3-CURRENT BOOK 4-SOLD BOOK 
def u_in_user():
    root=Tk()
    root.configure(background='#ccffff',relief=RAISED)
    root.title("OLD BOOK STALL")
    root.geometry("600x400+400+150")
    root.resizable(0,0)
    b1=Button(root,text="SALE",bg="#009999",fg="White",font=("impact",20),width="20",height='1',command=a_sale)
    b1.grid(row=0,column=0,pady=10,padx=100)
    b2=Button(root,text="CHECK_HISTORY",bg="#009999",fg="White",font=("impact",20),width="20",height='1',command=b_history)
    b2.grid(row=1,column=0,pady=10,padx=100)

    b3=Button(root,text="CURRENT_BOOK",bg="#009999",fg="White",font=("impact",20),width="20",height='1',command=b_current)
    b3.grid(row=2,column=0,pady=10,padx=100)
    b4=Button(root,text="SOLD_BOOK",bg="#009999",fg="White",font=("impact",20),width="20",height='1',command=b_sold)
    b4.grid(row=3,column=0,pady=10,padx=180)
########################################################################################################

    root.mainloop()
