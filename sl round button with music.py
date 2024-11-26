from tkinter import *
from pygame import mixer 
mixer.init()


def playmusic(fnm):
    mixer.music.load(fnm) 
    mixer.music.set_volume(2000)
    mixer.music.play()
    
    

 


top = Tk()
top.geometry("400x300+180+120")


d=Label(text="Date : ",font=('bold',20),fg='red')
d.place(x=30,y=30)


def showdate():
    from datetime import datetime
    now = datetime.now()
    ds = now.strftime("%d/%m/%Y-- %I:%M %p")
    print("now =", now)
    d.config(text="Date :"+str(ds))
    
    playmusic("ddnews.mp3")
    
    


img1 = PhotoImage(file="gobutton1.png")
b1=Button(text="",image = img1,border=5,command=showdate)
b1.place(x=120,y=100)
#b1.config(bg="black")


def closekaro():
     mixer.music.stop()
     top.destroy()
    
    

top.protocol("WM_DELETE_WINDOW",closekaro )
top.mainloop()