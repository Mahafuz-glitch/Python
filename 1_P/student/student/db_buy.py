import sqlite3
from tkinter import *
con=sqlite3.connect('book.db')
cur=con.cursor()

#BUY BOOK AND UPDATE TABLE AVAILABLE TO SOLD
def b_buy(bk_id):#update table
    #cur.execute("UPDATE book SET b_price=350 WHERE b_price=400")
    cur.execute("update sale set status='sold' where status='available' and b_ib=?",(bk_id,))
    print(bk_id)
    print(type(bk_id))
    con.commit()
