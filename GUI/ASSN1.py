from curses.ascii import isdigit
from operator import contains
from tkinter import *
import sqlite3
from tkinter import messagebox

from numpy import delete

window = Tk()
window.title("SIGN UP Form")
window.geometry("1000x800")

frame = Frame(window)
frame.pack()

label_font = ("Times", 14, "bold")
entry_font = ("Times", 14, "normal")

#============================ FIRST NAME ENTRY BOX =========================#
label_firstName = Label(frame, text="First name: ", font=label_font)
label_firstName.grid(row=1, column=0)

entry_firstName = Entry(frame, font=entry_font)
entry_firstName.grid(row=1, column=1)
#===========================================================================#

#============================ LAST NAME ENTRY BOX ==========================#
label_lastName = Label(frame, text="Last Name: ", font=label_font)
label_lastName.grid(row=1, column=2)

entry_lastName = Entry(frame, font=entry_font)
entry_lastName.grid(row=1, column=3)
#===========================================================================#

#============================ USERNAME ENTRY BOX ==========================#
label_un = Label(frame, text="User Name: ", font=label_font)
label_un.grid(row=2, column=0)

entry_un = Entry(frame, font=entry_font)
entry_un.grid(row=2, column=1)
#===========================================================================#

#============================ PHONE NUMBER ENTRY BOX ==========================#
label_pn = Label(frame, text="Phone: ", font=label_font)
label_pn.grid(row=3, column=0)

entry_pn = Entry(frame, font=entry_font)
entry_pn.grid(row=3, column=1)
#===========================================================================#

#============================ PASSWORD ENTRY BOXES ==========================#
label_pw = Label(frame, text="Choose Password: ", font=label_font)
label_pw.grid(row=4, column=0)

entry_pw = Entry(frame, font=entry_font, show="*")
entry_pw.grid(row=4, column=1)

label_pw_confirm = Label(frame, text="Confirm Password: ", font=label_font)
label_pw_confirm.grid(row=5, column=0)

entry_pw_confirm = Entry(frame, font=entry_font, show="*")
entry_pw_confirm.grid(row=5, column=1)
#===========================================================================#

#============================ Submit Button ================================#
fields = ["First_Name", "Last_Name", "Username", "Phone", "Password"]



def submit_data():
    firstName = entry_firstName.get()
    lastName = entry_lastName.get()
    username = entry_un.get()
    phone = entry_pn.get()
    if entry_pw.get() == entry_pw_confirm.get():
        if len(phone) == 10 and phone.isdigit():
            password = entry_pw_confirm.get()
            conn = sqlite3.connect('assn1.db')
            cursor = conn.cursor()
        
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS users" 
                " (firstName TEXT, lastName TEXT, userName TEXT, phone TEXT, password TEXT)"
            )
            insert_command_SQL = f'INSERT INTO users VALUES ("{firstName}", "{lastName}", "{username}", "{phone}", "{password}")'
            cursor.execute(insert_command_SQL)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success!", "Your account has been created successfully")
            entry_firstName.delete(0,"end")
            entry_lastName.delete(0,"end")
            entry_un.delete(0,"end")
            entry_pn.delete(0,"end")
            entry_pw.delete(0,"end")
            entry_pw_confirm.delete(0,"end")
        else:
            messagebox.showerror("Error", "Make sure the phone number is valid")
    else:
        messagebox.showerror("Error", "The confirm password and choose password entries do not match")

button_submit = Button(frame, text="Submit", font=label_font, command=submit_data)
button_submit.grid(row=7, columnspan=4)
#===========================================================================#

# needs to be at the bottom to build the window with all the stuff
window.mainloop()