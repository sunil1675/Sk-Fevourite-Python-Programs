from tkinter import *
import time

w = Tk()
w.geometry("900x300")

txt="Please like and subscribe my channel"
index=0
text=''
label=Label(w,text=txt,font=('Arial',30,"bold"),fg='red')
label.pack(pady=100)
def slider():
    global index, text
    if index>=len(txt):
        index=-0
        text=''
        label.config(text=text)
    else:
        text=text+txt[index]
        label.config(text=text)
        index+=1
    label.after(100, slider)
    
    w.update()

slider()
w.mainloop()