from tkinter import *
import ttkbootstrap
from tkinter import ttk

# Function to add a digit to the display
def add_digit(digit):
    value = display.get()
    if value == "0":
        value = digit
    else:
        value += digit
    display.delete(0, END)
    display.insert(0, value)

# Function to add an operator to the display
def add_operator(operator):
    global first_num
    first_num = int(display.get())
    global math_operator
    math_operator = operator
    display.delete(0, END)

# Function to calculate the result
def calculate():
    second_num = int(display.get())
    display.delete(0, END)
    if math_operator == "+":
        result = first_num + second_num
    elif math_operator == "-":
        result = first_num - second_num
    elif math_operator == "*":
        result = first_num * second_num
    else:
        result = first_num / second_num
    display.insert(0, result)

# Function to clear the display
def clear():
    display.delete(0, END)
    display.insert(0, "0")

# Create the main window
root = ttkbootstrap.Window(themename="flatly")
root.title("Calculator")
root.geometry("265x215")

# Create the display widget
display = ttk.Entry(root, font=("Helvetica", 20), justify=RIGHT)
display.insert(0, "0")
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Create the digit buttons
button_1 = ttk.Button(root, text="1", bootstyle="dark", command=lambda: add_digit("1"))
button_2 = ttk.Button(root, text="2", bootstyle="dark", command=lambda: add_digit("2"))
button_3 = ttk.Button(root, text="3", bootstyle="dark", command=lambda: add_digit("3"))
button_4 = ttk.Button(root, text="4", bootstyle="dark", command=lambda: add_digit("4"))
button_5 = ttk.Button(root, text="5", bootstyle="dark", command=lambda: add_digit("5"))
button_6 = ttk.Button(root, text="6", bootstyle="dark", command=lambda: add_digit("6"))
button_7 = ttk.Button(root, text="7", bootstyle="dark", command=lambda: add_digit("7"))
button_8 = ttk.Button(root, text="8", bootstyle="dark", command=lambda: add_digit("8"))
button_9 = ttk.Button(root, text="9", bootstyle="dark", command=lambda: add_digit("9"))
button_0 = ttk.Button(root, text="0", bootstyle="dark", command=lambda: add_digit("0"))

# Create the operator buttons
button_add = ttk.Button(root, text="+", bootstyle="warning", command=lambda: add_operator("+"))
button_subtract = ttk.Button(root, text="-", bootstyle="warning", command=lambda: add_operator("-"))
button_multiply = ttk.Button(root, text="*", bootstyle="warning", command=lambda: add_operator("*"))
button_divide = ttk.Button(root, text="/", bootstyle="warning", command=lambda: add_operator("/"))
button_equal = ttk.Button(root, text="=", bootstyle="dark-toolbutton", command=calculate)
button_clear = ttk.Button(root, text="C", bootstyle="danger-toolbutton", command=clear)

# Place the buttons on the grid
button_1.grid(row=3, column=0, padx=5, pady=5)
button_2.grid(row=3, column=1, padx=5, pady=5)
button_3.grid(row=3, column=2, padx=5, pady=5)
button_4.grid(row=2, column=0, padx=5, pady=5)
button_5.grid(row=2, column=1, padx=5, pady=5)
button_6.grid(row=2, column=2, padx=5, pady=5)
button_7.grid(row=1, column=0, padx=5, pady=5)
button_8.grid(row=1, column=1, padx=5, pady=5)
button_9.grid(row=1, column=2, padx=5, pady=5)
button_0.grid(row=4, column=0, padx=5, pady=5)

button_add.grid(row=1, column=3, padx=5, pady=5)
button_subtract.grid(row=2, column=3, padx=5, pady=5)
button_multiply.grid(row=3, column=3, padx=5, pady=5)
button_divide.grid(row=4, column=3, padx=5, pady=5)
button_equal.grid(row=4, column=1, padx=5, pady=5)
button_clear.grid(row=4, column=2, padx=5, pady=5)

root.mainloop()