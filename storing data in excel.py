from tkinter import *
from mysql.connector import *

def savedata():
    mycon=connect(host='localhost',user='root',password='naina2005',database='naina')
    mycur=mycon.cursor()
    val1=ntxt.get()
    val2=ctxt.get()
    val3=mtxt.get()
    print(val1,val2,val3)
    q='insert into customer(name,city,mobile) values(%s,%s,%s)'
    t=(val1,val2,val3)
    mycur.execute(q,t)
    mycon.commit()
    mycon.close()

root=Tk()

root.geometry('600x500')
root.resizable(0,0)

nlbl=Label(root,text='name')
nlbl.place(x=40,y=30)

ntxt=Entry(root)
ntxt.place(x=100,y=30)

albl=Label(root,text='city')
albl.place(x=40,y=100)

ctxt=Entry(root)
ctxt.place(x=100,y=100)

ilbl=Label(root,text='mobileno')
ilbl.place(x=40,y=170)

mtxt=Entry(root) 
mtxt.place(x=100,y=170)



btn=Button(root,text='save',command=savedata)
btn.place(x=100,y=250)

root.mainloop()
