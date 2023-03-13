import random
import string
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

# function to generate password
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(var.get()))
    output.config(text = password)
    output.config(text = password, font=("Ubuntu", 20), justify = 'center')

# function to copy the password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output['text'])

# create themed tkinter window
root = ThemedTk(theme = "equilux")
root.title("Password Generator")
root.geometry("300x200")

# variable to hold the number of characters in the password
var = tk.IntVar()
var.set(8)

# create a dropdown menu for the number of characters
dropdown = ttk.Combobox(root, textvariable = var, values = [8,9,10,11,12,13,14,15,16,17,18,19,20])
dropdown.pack(pady = 5)

# create 'generate' button
generate_button = ttk.Button(root, text="Generate", command = generate_password)
generate_button.pack(pady = 5)

# create 'copy' button
copy_button = ttk.Button(root, text="Copy", command = copy_to_clipboard)
copy_button.pack(pady = 5)

# create output field
output = ttk.Label(root)
output.pack(pady = 20)

# run the main loop
root.mainloop()