from tkinter import *

root = Tk()
root.title("Python - Update SQLite Data")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)


Top = Frame(root, width=900, height=50, bd=2, relief="raise")
Top.pack(side=TOP)


Left = Frame(root, width=600, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=300, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Right, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Right, width=300, height=100, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)
RadioGroup = Frame(Forms)
