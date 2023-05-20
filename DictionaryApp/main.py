import tkinter as tk
from ttkbootstrap import Style, ttk
import requests

def get_definition(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        data = response.json()
        if data:
            meanings = data[0]['meanings']
            definitions = []
            for meaning in meanings:
                definitions.append(f"• Meaning: {meaning['partOfSpeech']}\nDefinition: {meaning['definitions'][0]['definition']}\n")
            return '\n'.join(definitions)
        return "No definition found."

def search_definition():
    word = entry_word.get()
    definition = get_definition(word)
    text_output.configure(state='normal')
    text_output.delete('1.0', tk.END)
    text_output.insert(tk.END, definition)
    text_output.configure(state='disabled')

root = tk.Tk()
style = Style(theme="flatly")
root.title("Dictionary App")
root.geometry("500x300")

# Search frame
frame_search = ttk.Frame(root)
frame_search.pack(padx=20, pady=20)

# Label for the word entry field
label_word = ttk.Label(frame_search, text="Enter a word:", 
                       font=('TkDefaultFont', 15, 'bold'))
label_word.grid(row=0, column=0, padx=5, pady=5)

# Entry field for the word
entry_word = ttk.Entry(frame_search, width=20, font=('TkDefaultFont 15'))
entry_word.grid(row=0, column=1, padx=5, pady=5)

# Search button
button_search = ttk.Button(frame_search, text="Search", command=search_definition)
button_search.grid(row=0, column=2, padx=5, pady=5)

# Output frame
frame_output = ttk.Frame(root)
frame_output.pack(padx=20, pady=10)

# Text output field for displaying the definition
text_output = tk.Text(frame_output, height=10, state='disabled',
                      font=('TkDefaultFont', 15))
text_output.pack()

root.mainloop()