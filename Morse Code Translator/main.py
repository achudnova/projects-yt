import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style, ttk

# Morse Code Dictionary
morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                   '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
                   '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
                   ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
                   '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
                   }

# Reverse Morse Code Dictionary
reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

# Function to show the 'text to morse code' translation screen
def show_text_to_morse():
    home_frame.pack_forget()
    translation_frame.pack()
    translation_label.config(text="Input Text:")
    translation_button.config(text="Translate to Morse Cede")
    translation_button.config(command=text_to_morse_code)

def show_morse_code_to_text():
    home_frame.pack_forget()
    translation_frame.pack()
    translation_label.config(text="Input Morse Code:")
    translation_button.config(text="Translate to Text")
    translation_button.config(command=morse_code_to_text)

# Function to show the home screen
def show_home_screen():
    translation_frame.pack_forget()
    home_frame.pack()
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")

# Function to translate text to morse code
def text_to_morse_code():
    text = input_text.get("1.0", "end").strip().upper()
    if not text:
        messagebox.showwarning("Empty Input", "Please enter some text.")
        return
    # Validate if Morse code is entered
    for char in text:
        if char in morse_code_dict.values():
            messagebox.showwarning(
                "Invalid Input", "Cannot input Morse code in this option.")
            return
    
    morse_code = ""
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "
        else:
            morse_code += char
    output_text.delete("1.0", "end")
    output_text.insert("1.0", morse_code)

# Function to translate Morse Code to Text
def morse_code_to_text():
    morse_code = input_text.get("1.0", "end").strip().split(" ")
    if not morse_code:
        messagebox.showwarning("Empty Input", "Please enter some Morse code.")
        return
    
    # Validate if leeters are entered
    for code in morse_code:
        if code.isalpha():
            messagebox.showwarning(
                "Invalid Input", "Cannot input letters in this option")
            return
    
    text = ""
    for code in morse_code:
        if code in reverse_morse_code_dict:
            text += reverse_morse_code_dict[code]
        else:
            text += code
    output_text.delete("1.0", "end")
    output_text.insert("1.0", text)

# Function to clear the input and output fields and show the home screen
def clear_text():
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")
    show_home_screen()

# Create the main window
window = tk.Tk()
window.title("Morse Code Translator")
window.geometry("400x400")
style = Style(theme="flatly")

# Create home screen
home_frame = ttk.Frame(window, padding="20")
home_frame.pack()

home_label = ttk.Label(home_frame, text="Select Translation Type:", 
                       font=('tk.DefaultFont', 20))
home_label.pack(pady=10)

# Text -> Morse Code button
text_to_morse_code_btn = ttk.Button(home_frame, text="Text to Morse Code",
                                    command=show_text_to_morse)
text_to_morse_code_btn.pack(pady=5)

# Morse Code -> text button
morse_code_to_text_btn = ttk.Button(home_frame, text="Morse Code to Text",
                                    command=show_morse_code_to_text)
morse_code_to_text_btn.pack(pady=5)

# Create translation screen
translation_frame = ttk.Frame(window, padding="20")

# Create label for input text
translation_label = ttk.Label(translation_frame, text="Input Text:", 
                              font=('tk.DefaultFont', 20))
translation_label.pack(pady=10)

# Create input text field
input_text = tk.Text(translation_frame, height=5)
input_text.pack()

# Create label for output text
output_text_label = ttk.Label(translation_frame, text="Output Text:",
                              font=('tk.DefaultFont', 20))
output_text_label.pack()

# Create output text field
output_text = tk.Text(translation_frame, height=5)
output_text.pack()

# Create translation button
translation_button = ttk.Button(translation_frame, text="Translate", command=None)
translation_button.pack(pady=15)

# Create back button to return to home screen
back_button = ttk.Button(translation_frame, text="Back", command=show_home_screen)
back_button.pack(pady=5)

# Hide translation screen initially
translation_frame.pack_forget()

window.mainloop()