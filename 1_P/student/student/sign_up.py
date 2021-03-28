from tkinter import *
import sqlite3
#######################################################################################################################

#for Database connection
con=sqlite3.connect("std.db")
cur=con.cursor()
#Create function to make a table
def table():
    cur.execute("CREATE TABLE IF NOT EXISTS student(s_name TEXT,s_p_word TEXT)")
    con.commit()
#table()   
#Insert data
    
def ins_data():
        cur.execute("INSERT INTO student VALUES(?,?)",(t1.get(),t2.get()))
        con.commit()
#def view        
        
#########################################################################################################################    
#FOR GUI of table
##############################################
#FOR SOGN UP

root=Tk()
root.title("OLD BOOK STALL")
root.geometry("600x400")
root.resizable(0,0)
t1=StringVar()
t2=StringVar()
#Label 1
l1=Label(root,font=("impact",10),text="Enter your name",pady=10)
l1.grid(row=0,column=0)
e1=Entry(root,width=30,bg="#00ffbf",font=("impact",10),textvariable=t1)
e1.grid(row=1,column=0,padx=30)
#Label 2
l2=Label(root,font=("impact",10),text="Enter your Password",pady=10)
l2.grid(row=0,column=1)
e2=Entry(root,width=30,bg="#00ffbf",font=("impact",10),textvariable=t2)
e2.grid(row=1,column=1,padx=20)
#Button
b1=Button(root,text="Sign Up",bg="#0000ff",fg="White",font=("impact",9),width="30",command=ins_data)
b1.grid(row=2,column=0,columnspan=2,pady=20)

root.mainloop()

################################################
