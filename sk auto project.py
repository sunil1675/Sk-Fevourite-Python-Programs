spl='''
from tkinter import *
w=Tk()
w.geometry('620x410+350+100')
w.configure()
w.title("ST. ANTHONY'S GUI BY SUNIL")
w.overrideredirect(True)
p=PhotoImage(file="sksplash.png")
l1=Label(w,image=p)
l1.place(x=0,y=0)

def bandkaro():
    w.destroy()
w.after(2000,bandkaro)
'''

fnm=['blank','splash','progressbar','welcome','registration','login','mainmenu','help','about','home']

n=input("Enter first 4 letter of your name ")
for i in fnm:
    ff=n+i+".py"
    f=open(ff,'w')
    f.write(spl)
    f.close()