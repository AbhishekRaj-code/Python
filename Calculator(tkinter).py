# Simple Calculator using tkinter
# This code creates a basic calculator GUI with buttons for digits and operations.
# It supports addition, subtraction, multiplication, and division.

# Importing tkinter module
from tkinter import *

# Creating main window
window = Tk()
window.title("Simple Calculator")
window.geometry("500x500")

# Creating an entry widget for displaying input and results
e =Entry(window, width=56, borderwidth=5)
e.place(x=10, y=10)

# Function to handle button clicks
def click(num):
    result = e.get() # Get current input
    e.delete(0, END) # Clear the entry
    e.insert(0, str(result) + str(num)) # Append new number and display

#function to add decimal point
def dot():
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + '.')

# Creating buttons for numbers 0-9
b = Button(window, text="1", width=12, command=lambda:click(1)) 
b.place(x=10, y=60)

b = Button(window, text="2", width=12, command=lambda:click(2))
b.place(x=80, y=60)

b = Button(window, text="3", width=12, command=lambda:click(3))
b.place(x=170, y=60)

b = Button(window, text="4", width=12, command=lambda:click(4))
b.place(x=10, y=120)

b = Button(window, text="5", width=12, command=lambda:click(5))
b.place(x=80, y=120)

b = Button(window, text="6", width=12, command=lambda:click(6))
b.place(x=170, y=120)

b = Button(window, text="7", width=12, command=lambda:click(7))
b.place(x=10, y=180)

b = Button(window, text="8", width=12, command=lambda:click(8))
b.place(x=80, y=180)

b = Button(window, text="9", width=12, command=lambda:click(9))
b.place(x=170, y=180)

b = Button(window, text="0", width=12, command=lambda:click(0))
b.place(x=80, y=240)



# Operation functions

# Function for addition
def add():
    n1 = e.get()                              # Get the first number
    global math                               # Declare math as global to use it outside this function
    math = "addition"
    global i                                  # Declare i as global to store the first number
    i = float(n1)
    e.delete(0, END)                          # Clear the entry for the next number

# Function for subtraction
def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = float(n1)
    e.delete(0, END)

# Function for multiplication
def mul():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = float(n1)
    e.delete(0, END)

# Function for division
def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = float(n1)
    e.delete(0, END)

# Function to calculate resfloat
def equal():
    n2 = e.get()                             # Get the second number
    e.delete(0, END)                         # Clear the entry

    # Perform the operation based on the value of math
    if math == "addition":
        e.insert(0, i + float(n2))
    elif math == "subtraction":
        e.insert(0, i - float(n2))
    elif math == "multiplication":
        e.insert(0, i * float(n2))
    elif math == "division":
        e.insert(0, i / float(n2))

# Function to clear the entry
def clear():
    e.delete(0, END)                        # Clear the entry widget


    


# Creating buttons for operations
b_add = Button(window, text="+", width=12, command= add) 
b_add.place(x=260, y=60)

b_sub = Button(window, text="-", width=12, command= sub)
b_sub.place(x=260, y=120)

b_mul = Button(window, text="*", width=12, command= mul)
b_mul.place(x=260, y=180)

b_div = Button(window, text="/", width=12, command= div)
b_div.place(x=260, y=240)

b_equal = Button(window, text="=", width=12, command= equal)
b_equal.place(x=170, y=240)

b_clear = Button(window, text="Clear", width=12, command= clear)
b_clear.place(x=10, y=240)

b_dot = Button(window, text=".", width=12, command= dot)
b_dot.place(x=340, y=60)


# Running the main event loopwindow.
mainloop()