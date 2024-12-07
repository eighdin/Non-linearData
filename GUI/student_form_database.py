from tkinter import *
import sqlite3

window = Tk()
window.title("Student Form")
window.geometry("1000x800")

frame = Frame(window)
frame.pack()

label_font = ("Times", 14, "bold")
entry_font = ("Times", 14, "normal")
#============================ HEADING ======================================#
label_heading = Label(frame, text="STUDENT FORM", height=3, font=("Times", 18, "bold"))
label_heading.grid(row=0, columnspan=4)
#===========================================================================#

#============================ FIRST NAME ENTRY BOX =========================#
label_firstName = Label(frame, text="First name: ", font=label_font)
label_firstName.grid(row=1, column=0)

entry_firstName = Entry(frame, font=entry_font)
entry_firstName.grid(row=1, column=1)
#===========================================================================#

#============================ LAST NAME ENTRY BOX ==========================#
label_lastName = Label(frame, text="Last Name: ", font=label_font)
label_lastName.grid(row=2, column=0)

entry_lastName = Entry(frame, font=entry_font)
entry_lastName.grid(row=2, column=1)
#===========================================================================#

#============================ EMAIL ENTRY BOX ==========================#
label_email = Label(frame, text="Email: ", font=label_font)
label_email.grid(row=3, column=0)

entry_email = Entry(frame, font=entry_font)
entry_email.grid(row=3, column=1)
#===========================================================================#

#============================ DOB ENTRY BOX ==========================#
label_dob = Label(frame, text="DOB: ", font=label_font)
label_dob.grid(row=4, column=0)

entry_dob = Entry(frame, font=entry_font)
entry_dob.grid(row=4, column=1)
#===========================================================================#

#============================ Major Checkbox ===============================#
cyber_value = IntVar()
datasci_value = IntVar()

label_major = Label(frame, text="Major: ", font=label_font)
label_major.grid(row=5, column=0)

checkbox_cyber = Checkbutton(
    frame, text="Cyber", variable=cyber_value, 
    onvalue=1, offvalue=0,
    font=label_font
)
checkbox_cyber.grid(row=5, column=1)

checkbox_dataSci = Checkbutton(
    frame, text="D.S.", variable=datasci_value, 
    onvalue=1, offvalue=0,
    font=label_font
)
checkbox_dataSci.grid(row=5, column=2)
#===========================================================================#

#============================ GENDER =======================================#
gender_row = 6
label_gender = Label(frame, text="Gender: ", font=label_font)
label_gender.grid(row=gender_row, column=0)

gender_Value = IntVar()

radio_male = Radiobutton(frame, text="Male", variable=gender_Value, value=1, font=label_font)
radio_male.grid(row=gender_row, column=1)

radio_female = Radiobutton(frame, text="Female", variable=gender_Value, value=2, font=label_font)
radio_female.grid(row=gender_row, column=2)

radio_other = Radiobutton(frame, text="Other", variable=gender_Value, value=3, font=label_font)
radio_other.grid(row=gender_row, column=3)
#===========================================================================#

#============================ Submit Button ================================#
fields = ["First_Name", "Last_Name", "Email", "DOB", "Cyber", "DS", "Gender"]



def submit_data():
    firstName = entry_firstName.get()
    lastName = entry_lastName.get()
    email = entry_email.get()
    dob = entry_dob.get()
    isCyber = cyber_value.get()
    isDS = datasci_value.get()
    gender = gender_Value.get()
    
    conn = sqlite3.connect('student_id_db.db')
    cursor = conn.cursor()
    
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS student_id_info" 
        " (firstName TEXT, lastName TEXT, email TEXT, dob TEXT, isCyber TEXT, isDS TEXT, gender TEXT)"
    )
    insert_command_SQL = f'INSERT INTO student_id_info VALUES ("{firstName}", "{lastName}", "{email}", "{dob}", "{isCyber}", "{isDS}", "{gender}")'
    cursor.execute(insert_command_SQL)
    conn.commit()
    conn.close()

button_submit = Button(frame, text="Submit", font=label_font, command=submit_data)
button_submit.grid(row=7, columnspan=4)
#===========================================================================#

#============================ GRADE SELECTOR ===============================#
# label_grade = Label(frame, text="Grade", font=label_font)
# label_grade.grid(row=8, column=0)

# listb_Grade = Listbox(frame, height=3)
# listb_Grade.grid(row=8, column=1)

# listb_Grade.insert(1, "Freshman")
# listb_Grade.insert(2, "Sophomore")
# listb_Grade.insert(3, "Junior")
# listb_Grade.insert(4, "Senior")
# listb_Grade.insert(5, "Super Senior")
#===========================================================================#

# needs to be at the bottom to build the window with all the stuff
window.mainloop()