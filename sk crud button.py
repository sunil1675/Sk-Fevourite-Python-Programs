import mysql.connector as sql


projnm='PROJECT NAME TITLE'
dbname='skd'
tblnm='student'

con=sql.connect(host='localhost',user='root')
cur=con.cursor()
cur.execute(f"use {dbname}")
cur.execute(f"desc {tblnm}")
data=cur.fetchall()
fields=[]

for i in data:
    fields.append(i[0])


cur.execute(f"select * from {tblnm}")
data=cur.fetchall()
index = 0



from tkinter import *

w=Tk()
w.geometry("650x700+300+2")

Label(w,text=projnm,font=('bold',28)).place(x=100,y=5)
#===============================================================
f1=Frame(w,bg='pink',width=300,height=550)
f1.place(x=30,y=50)

f2=Frame(w,bg='green',width=300,height=550)
f2.place(x=250,y=50)

f3=Frame(w,bg='yellow',width=530,height=50)
f3.place(x=20,y=580)
#===============================================================


yy=[]
sy=20
gap=30
for i in range(len(fields)):
    yy.append(sy)
    sy=sy+gap

xx=40


for i in range(len(fields)):
    l1=Label(f1,text=fields[i],font=('bold',18))
    l1.place(x=xx,y=yy[i])
    

ent=[]
for i in range(len(fields)):
    t=Entry(f2,font=('bold',14))
    t.place(x=xx,y=yy[i])
    ent.append(t)
    

totrec=Label(w, text = 'Total Records', font=('verdana',12), bg='gold')
currec=Label(w, text = 'Current Record', font=('verdana',12), bg='gold')
totrec.place(x=20,y=640)
currec.place(x=280,y=640)


totrec.config(text='Total Records    '+ str(len(data)))
currec.config(text='Current Records  '+ str(index+1))

button_first=Button(f3, text = 'First', font=('verdana',12), bg='gold')
button_next=Button(f3, text = 'Next', font=('verdana',12), bg='gold')
button_previous=Button(f3, text = 'Previous', font=('verdana',12),bg='gold')
button_last=Button(f3, text = 'Last', font=('verdana',12), bg='gold')
button_clear=Button(f3, text = 'Clear', font=('verdana',12), bg='gold')
button_save=Button(f3, text = 'New', font=('verdana',12), bg='gold')
button_update=Button(f3, text = 'Update', font=('verdana',12), bg='gold')


button_first.place(x=20,y=10)
button_next.place(x=175,y=10)
button_previous.place(x=80,y=10)
button_last.place(x=240,y=10)
button_clear.place(x=300,y=10)
button_save.place(x=370,y=10)
button_update.place(x=440,y=10)
#===============================================================


def clearTextfields():
    
    # clear textfields
    for i in range(len(fields)):
        ent[i].delete(0,END)
    

def showFirst():
    clearTextfields()
    global index
    index = 0
    
    totrec.config(text='Total Records    '+ str(len(data)))
    currec.config(text='Current Records  '+ str(index+1))
    
    for i in range(len(fields)):
            ent[i].insert(0,data[index][i])
    
def showNext():
    clearTextfields()
    global index
    index = index+1
    
    totrec.config(text='Total Records    '+ str(len(data)))
    currec.config(text='Current Records  '+ str(index+1))

    if index > len(data)-1:
        index = len(data)-1
        
    for i in range(len(fields)):
            ent[i].insert(0,data[index][i])


def showPrevious():
    clearTextfields()
    global index
    index = index-1
    
    totrec.config(text='Total Records    '+ str(len(data)))
    currec.config(text='Current Records  '+ str(index+1))
    
    if index > len(data)-1:
        index = len(data)-1
        
    for i in range(len(fields)):
            ent[i].insert(0,data[index][i])

def showLast():
    clearTextfields()
    global index
    index = len(data)-1
    
    totrec.config(text='Total Records    '+ str(len(data)))
    currec.config(text='Current Records  '+ str(index+1))

    for i in range(len(fields)):
            ent[i].insert(0,data[index][i])


def updaterecord():
     global index,data
     rec=[]
     qr=f"update {tblnm} set "
     for i in range(len(fields)):
            qr=qr+fields[i]+"=%s,"
     qr=qr[:-1] + f" where {fields[0]} =%s"
     print("yes ",qr)
     
     
     for i in range(len(fields)):
            t=ent[i].get()
            rec.append(t)
     rec.append(ent[0].get())
     rec=tuple(rec)
     print(qr,rec)
     
     cur.execute(qr,rec)
     con.commit()
     
     cur.execute(f"select * from {tblnm}")
     data=cur.fetchall()
     
    

def saverecord():
     cnm=button_save['text']
     print(cnm)
     
     button_save['text']='Save'
     
     clearTextfields()
     global index
     rec=[]
     para=""
     for i in range(len(fields)):
            t=ent[i].get()
            rec.append(t)
            para=para+"%s,"
     rec=tuple(rec)
     para=para[:-1]
     print(rec,para)
     
     qry=f"insert into {tblnm} values({para})"
     print(qry)
     cur.execute(qry,rec)
     con.commit()
     cur.execute(f"select * from {tblnm}")
     data=cur.fetchall()
     index=len(data)
     print("Total Record ", index)
     
     totrec.config(text='Total Records    '+ str(len(data)))
     currec.config(text='Current Records  '+ str(index+1))
     
            
button_first['command'] = showFirst
button_next['command'] = showNext
button_previous['command'] = showPrevious
button_last['command'] = showLast
button_clear['command'] = clearTextfields
button_save['command'] = saverecord
button_update['command'] = updaterecord


        
w.after(500,showFirst)
w.mainloop()
