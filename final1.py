from tkinter import *
import csv
import os

window = Tk()
window.title("Application Form")
window.geometry("1000x400")

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

#============================ AGE ENTRY BOX ================================#
label_age = Label(frame, text="Age: ", font=label_font)
label_age.grid(row=2, column=0)

entry_age = Entry(frame, font=entry_font)
entry_age.grid(row=2, column=1)
#===========================================================================#

#============================ SALARY ENTRY BOX ================================#
label_salary = Label(frame, text="Salary: ", font=label_font)
label_salary.grid(row=3, column=0)

entry_salary = Entry(frame, font=entry_font)
entry_salary.grid(row=3, column=1)
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
filename = "premium_data.csv"
fileObj = open(filename, "a",newline="")
fields = ["First_Name", "Last_Name", "Premium"]
writer = csv.DictWriter(fileObj, fieldnames=fields)
if not os.path.exists(filename):
    print("file doesn't exist!\ncreating it and adding headers.")
    writer.writeheader()
else:
    print("File exists!\nadding data:")

def calculate_premium(age, salary) -> int:
    if age <= 30:
        if salary <= 70000:
            return 400
        else:
            return 500
    else:
        if salary <= 70000:
            return 600
        else:
            return 700

def submit_data():
    firstName = entry_firstName.get()
    lastName = entry_lastName.get()
    age = int(entry_age.get())
    salary = int(entry_salary.get())
    gender = gender_Value.get()
    premium = calculate_premium(age, salary)
    row = {"First_Name" : firstName, "Last_Name" : lastName, "Premium":premium}
    
    writer.writerow(row)
    print(row)
    entry_firstName.delete(0, "end")
    entry_lastName.delete(0, "end")
    entry_age.delete(0, "end")
    entry_salary.delete(0, "end")
    radio_female.deselect()
    radio_male.deselect()
    radio_other.deselect()
button_submit = Button(frame, text="Submit", font=label_font, command=submit_data)
button_submit.grid(row=7, columnspan=4)
#===========================================================================#

# needs to be at the bottom to build the window with all the stuff
window.mainloop()