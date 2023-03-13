import random
import tkinter as tk
import ttkbootstrap as ttk

def generate_number():
    result = random.randint(1, int(input_field.get()))
    result_label.config(text=result)

window = tk.Tk()
window.title("Random Number Generator")
window.geometry("200x200")
style = ttk.Style(theme="cosmo")

instruction_label = ttk.Label(text="Enter a number:", font=("Arial", 15))
input_field = ttk.Entry(width=10, font=("Arial", 15))
generate_button = ttk.Button(text="Generate", command=generate_number)
result_label = ttk.Label(text="", font=("Arial", 25))

instruction_label.pack(pady=10)
input_field.pack(pady=5)
generate_button.pack(pady=10)
result_label.pack(pady=10)

window.mainloop()