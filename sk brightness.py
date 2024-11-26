# first install screen_brightness_control

# pip install screen_brightness_control

from screen_brightness_control import set_brightness, get_brightness
#nb= int(input("Enter brightness level 1-200"))
#nb=40

cb = get_brightness()
print("Current screen brightness is:", cb)
set_brightness(cb[0])



from tkinter import *
from tkinter import ttk
w=Tk()

w.geometry("400x200")

s=ttk.Scale(w,from_=1, to=100,orient=HORIZONTAL,value=cb[0])
s.place(x=100,y=100)  

l1=Label(w,text=cb[0])
l1.place(x=50,y=100)

def abc(e):
    v=int(s.get())
    print(v)
    l1.config(text=v)
    set_brightness(v)


s.bind('<B1-Motion>',abc)

  
b1=Button(w,text='Value',command=abc)
b1.place(x=100,y=150)

w.mainloop()
