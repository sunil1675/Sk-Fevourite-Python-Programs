import tkinter as tk
from tkinter import *
import mysql.connector


connection = mysql.connector.connect(host='localhost', user='root', port='3306',
                                     password='', database='test_py')
c = connection.cursor()
index = 0

c.execute("SELECT * FROM `users_2`")
users = c.fetchall()

print(users)

root = Tk()

frame = tk.Frame(root, bg='#bdc3c7')

label_id = tk.Label(frame, text='ID:', font=('verdana',12), bg='#bdc3c7')
entry_id = tk.Entry(frame, font=('verdana',12))

label_fname = tk.Label(frame, text='First Name:', font=('verdana',12), bg='#bdc3c7')
entry_fname = tk.Entry(frame, font=('verdana',12))

label_lname = tk.Label(frame, text='Last Name:', font=('verdana',12), bg='#bdc3c7')
entry_lname = tk.Entry(frame, font=('verdana',12))

label_email = tk.Label(frame, text='Email:', font=('verdana',12), bg='#bdc3c7')
entry_email = tk.Entry(frame, font=('verdana',12))

label_age = tk.Label(frame, text='Age:', font=('verdana',12), bg='#bdc3c7')
entry_age = tk.Entry(frame, font=('verdana',12))

frame_buttons = tk.Frame(frame, bg='#bdc3c7')

button_first = tk.Button(frame_buttons, text = 'first', font=('verdana',12), bg='gold')
button_next = tk.Button(frame_buttons, text = 'next', font=('verdana',12), bg='gold')
button_previous = tk.Button(frame_buttons, text = 'previous', font=('verdana',12),
                            bg='gold')
button_last = tk.Button(frame_buttons, text = 'last', font=('verdana',12), bg='gold')


# function to clear textfields
def clearTextfields():
    # clear textfields
    entry_id.delete(0,END)
    entry_fname.delete(0,END)
    entry_lname.delete(0,END)
    entry_email.delete(0,END)
    entry_age.delete(0,END)


# function to show first item
def showFirst():
    
    clearTextfields()

    global index
    index = 0
    entry_id.insert(0,users[index][0])
    entry_fname.insert(0,users[index][1])
    entry_lname.insert(0,users[index][2])
    entry_email.insert(0,users[index][3])
    entry_age.insert(0,users[index][4])


# function to show next item
def showNext():

    clearTextfields()

    global index
    index = index+1
    if index > len(users)-1:
        index = len(users)-1

    entry_id.insert(0,users[index][0])
    entry_fname.insert(0,users[index][1])
    entry_lname.insert(0,users[index][2])
    entry_email.insert(0,users[index][3])
    entry_age.insert(0,users[index][4])


# function to show previous item
def showPrevious():

    clearTextfields()

    global index
    index = index-1
    if index < 0:
        index =0

    entry_id.insert(0,users[index][0])
    entry_fname.insert(0,users[index][1])
    entry_lname.insert(0,users[index][2])
    entry_email.insert(0,users[index][3])
    entry_age.insert(0,users[index][4])


# function to show last item
def showLast():

    clearTextfields()

    global index
    index = len(users)-1
    entry_id.insert(0,users[index][0])
    entry_fname.insert(0,users[index][1])
    entry_lname.insert(0,users[index][2])
    entry_email.insert(0,users[index][3])
    entry_age.insert(0,users[index][4])



button_first['command'] = showFirst
button_next['command'] = showNext
button_previous['command'] = showPrevious
button_last['command'] = showLast


frame.grid(row=0, column=0)

label_id.grid(row=0, column=0, sticky='e', padx=10, pady=10)
entry_id.grid(row=0, column=1, padx=10, pady=10)

label_fname.grid(row=1, column=0, sticky='e', padx=10, pady=10)
entry_fname.grid(row=1, column=1, padx=10, pady=10)

label_lname.grid(row=2, column=0, sticky='e', padx=10, pady=10)
entry_lname.grid(row=2, column=1, padx=10, pady=10)

label_email.grid(row=3, column=0, sticky='e', padx=10, pady=10)
entry_email.grid(row=3, column=1, padx=10, pady=10)

label_age.grid(row=4, column=0, sticky='e', padx=10, pady=10)
entry_age.grid(row=4, column=1, padx=10, pady=10)

frame_buttons.grid(row=5, column=0, columnspan=2)

button_first.grid(row=0, column=0, padx=10, pady=10)
button_next.grid(row=0, column=1, padx=10, pady=10)
button_previous.grid(row=0, column=2, padx=10, pady=10)
button_last.grid(row=0, column=3, padx=10, pady=10)

root.mainloop()
