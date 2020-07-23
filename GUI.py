# HELLO
from tkinter import *


def second_win():

    second_win = Toplevel(root)

    second_win.title("Number of Employees")
    second_win.geometry('500x500')
    totalspace_text = Label(second_win, text="Total real estate per floor \n (in sq.ft)", width=40, fg="#1a577d", bg="white", font=("Calibri", 10, "bold"))
    totalspace_text.place(x=20, y=150)
    totalspace= StringVar()
    totalspace_entry = Entry(second_win, textvariable = totalspace,  width="10")
    totalspace_entry.place(x=380, y=160)



def third_win():

    third_win = Toplevel(root)
    third_win.title("Total needed spaces")
    third_win.geometry('500x500')
    totalspaces_text = Label(third_win, text="Total number of desired employees", width=40, fg="#1a577d", bg="white", font=("Calibri", 10, "bold"))
    totalspaces_text.place(x=20, y=150)
    totalspaces= IntVar()
    totalspaces_entry = Entry(third_win, textvariable = totalspaces,  width="10")
    totalspaces_entry.place(x=380, y=160)


root = Tk()
root.geometry('500x500')
root.title ("Cushman and Wakefield Office Space Analysis")
root.configure(bg="white")


register= Button(root,text = "Number of Employees", width ="30", fg="white", height = "2", command = second_win, bg="#1a577d", font="Calibri")
register.place(x=90, y= 90)

employee_text = Label(root, text="Option 1: Includes the analysis needed for Cushman & Wakefield \n for the number of employees allowed to come in to the \n office in consideration of the office space. ", width=60, fg="#1a577d", bg="white", font=("Calibri", 10, "bold"))
employee_text.place(x=40, y=180)


register= Button(root,text = "Growing Real Estate", width ="30", fg="white", height = "2", command = third_win, bg="#1a577d", font="Calibri")
register.place(x=90, y= 300)

space_text = Label(root, text="Option 2: Includes the analysis needed for Cushman & Wakefield for \n the amount of office space needed regarding how many \n employees will be coming in to the office. ", width=60, fg="#1a577d", bg="white", font=("Calibri", 10, "bold"))
space_text.place(x=40, y=380)

mainloop()
