
from tkinter import *
import sqlite3
from del_admin import *
from admin_dtl import *
#####################################################################################################

# THIS IS administrator page
def admin_acc():
    root=Tk()
    root.title("OLD BOOK STALL")
    root.configure(background='#ffe0cc',relief=RAISED)
    root.geometry("600x400+400+150")
    root.resizable(0,0)
    b1=Button(root,text="USER DETAILS",bg="#ff6600",fg="White",font=("impact",20),width="20",height='1',command=u_view)
    b1.grid(row=0,column=0,pady=60,padx=180)
    b2=Button(root,text="DELETE",bg="#ff6600",fg="White",font=("impact",20),width="20",height='1',command=u_del_acc)
    b2.grid(row=1,column=0,pady=0,padx=180)


########################################################################################################

    root.mainloop()
