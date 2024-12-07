from math import comb
from tkinter import *
import csv
import os
from tkinter import messagebox

window = Tk()
window.title("IRL Stats")
window.geometry("1400x800")

frame = Frame(window)
frame.pack()

label_font = ("Times", 14, "bold")
entry_font = ("Times", 14, "normal")
#============================ HEADING ======================================#
label_heading = Label(frame, text="Character Sheet", height=3, font=("Times", 18, "bold"))
label_heading.grid(row=0, columnspan=4)
#===========================================================================#

#============================ TITLE ENTRY BOX =========================#
title_row = 1
label_title = Label(frame, text="Title: ", font=label_font)
label_title.grid(row=title_row, column=0)

title_value = IntVar()

radio_sir = Radiobutton(frame, text="Sir", variable=title_value, value=1, font=label_font)
radio_sir.grid(row=title_row, column=1)

radio_dr = Radiobutton(frame, text="Dr.", variable=title_value, value=2, font=label_font)
radio_dr.grid(row=title_row, column=2)

radio_jr = Radiobutton(frame, text="Jr.", variable=title_value, value=3, font=label_font)
radio_jr.grid(row=title_row, column=3)

radio_sr = Radiobutton(frame, text="Jr.", variable=title_value, value=3, font=label_font)
radio_sr.grid(row=title_row, column=4)
#===========================================================================#

#============================ FIRST NAME ENTRY BOX =========================#
label_firstName = Label(frame, text="First name: ", font=label_font)
label_firstName.grid(row=2, column=0)

entry_firstName = Entry(frame, font=entry_font)
entry_firstName.grid(row=2, column=1)
#===========================================================================#

#============================ LAST NAME ENTRY BOX ==========================#
label_lastName = Label(frame, text="Last Name: ", font=label_font)
label_lastName.grid(row=2, column=2)

entry_lastName = Entry(frame, font=entry_font)
entry_lastName.grid(row=2, column=3)
#===========================================================================#

#============================ GENDER SELECTOR ==========================#
gender_row = 3
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

#============================ AGE ENTRY BOX ==========================#
label_age = Label(frame, text="Age: ", font=label_font)
label_age.grid(row=4, column=0)

entry_age = Entry(frame, font=entry_font)
entry_age.grid(row=4, column=1)
#===========================================================================#

#============================ Skill Checkbox ===============================#
computer_value = IntVar()
mechanic_value = IntVar()
combat_value = IntVar()
magic_value = IntVar()
sales_value = IntVar()
stealth_value = IntVar()


label_skill = Label(frame, text="Skills: ", font=label_font)
label_skill.grid(row=5, column=0)

checkbox_computer = Checkbutton(
    frame, text="Computer Skills: ", variable=computer_value, 
    onvalue=1, offvalue=0,
    font=label_font
)
checkbox_computer.grid(row=5, column=1)

checkbox_mechanic = Checkbutton(
    frame, text="Mechanical Skills: ", variable=mechanic_value, 
    onvalue=1, offvalue=0,
    font=label_font
)
checkbox_mechanic.grid(row=5, column=2)

checkbox_combat = Checkbutton(
    frame, text="Combat Skills: ", variable=combat_value, 
    onvalue=1, offvalue=0,
    font=label_font
)
checkbox_combat.grid(row=5, column=3)

checkbox_magic = Checkbutton(
    frame, text="Magic Skills: ", variable=magic_value, 
    onvalue=1, offvalue=0,
    font=label_font
)
checkbox_magic.grid(row=6, column=1)

checkbox_sales = Checkbutton(
    frame, text="Sales Skills: ", variable=sales_value, 
    onvalue=1, offvalue=0,
    font=label_font
)
checkbox_sales.grid(row=6, column=2)

checkbox_stealth = Checkbutton(
    frame, text="Stealth Skills: ", variable=stealth_value, 
    onvalue=1, offvalue=0,
    font=label_font
)
checkbox_stealth.grid(row=6, column=3)
#===========================================================================#

#============================ MAX BENCH ENTRY BOX ==========================#
label_bench = Label(frame, text="Max Bench (lbs): ", font=label_font)
label_bench.grid(row=7, column=0)

entry_bench = Entry(frame, font=entry_font)
entry_bench.grid(row=7, column=1)
#===========================================================================#

#============================ VERT ENTRY BOX ==========================#
label_vert = Label(frame, text="Vertical Jump (ft): ", font=label_font)
label_vert.grid(row=7, column=2)

entry_vert = Entry(frame, font=entry_font)
entry_vert.grid(row=7, column=3)
#===========================================================================#

#============================ HEIGHT ENTRY BOX ==========================#
label_height = Label(frame, text="Height (in): ", font=label_font)
label_height.grid(row=8, column=0)

entry_height = Entry(frame, font=entry_font)
entry_height.grid(row=8, column=1)
#===========================================================================#

#============================ Submit Button ================================#
filename = "character_sheet.csv"
fileObj = open(filename, "a",newline="")
fields = ["First_Name", "Last_Name", "Gender", "Age", "Computer", "Mechanic", "Combat", "Magic", "Sales", "Stealth", "Max_Bench", "Vert", "Height"]
writer = csv.DictWriter(fileObj, fieldnames=fields)
if not os.path.exists(filename):
    print("file doesn't exist!\ncreating it and adding headers.")
    writer.writeheader()
else:
    print("File exists!\nadding data:")


def submit_data():
    firstName = entry_firstName.get()
    lastName = entry_lastName.get()
    gender = gender_Value.get()
    age = entry_age.get()
    computer = computer_value.get()
    mechanic = mechanic_value.get()
    combat = combat_value.get()
    magic = magic_value.get()
    sales = sales_value.get()
    stealth = stealth_value.get()
    maxBench = entry_bench.get()
    vert = entry_vert.get()
    height = entry_height.get()
    row = {
        "First_Name" : firstName, "Last_Name" : lastName, "Gender" : gender, "Age" : age,
        "Computer" : computer, "Mechanic" : mechanic, "Combat" : combat, "Magic" : magic, "Sales" : sales, "Stealth" : stealth,
        "Max_Bench" : maxBench, "Vert" : vert, "Height" : height
    }
    if sum([computer, mechanic, combat, magic, sales, stealth]) > 3:
        messagebox.showerror("Error", "Can only select 3 skills")
    else:
        writer.writerow(row)
        messagebox.showinfo("Success!", "Character added to sheet")
    print(row)
button_submit = Button(frame, text="Submit", font=label_font, command=submit_data)
button_submit.grid(row=10, columnspan=4)
#===========================================================================#

# needs to be at the bottom to build the window with all the stuff
window.mainloop()