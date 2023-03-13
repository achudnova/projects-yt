import requests
import tkinter as ttk
import ttkbootstrap as ttk

URL = "https://api.quotable.io/random"

def fetch_quote():
    response = requests.get(URL)
    data = response.json()
    quote = data["content"]
    author = data["author"]
    return quote, author

def update_quote():
    quote, author = fetch_quote()
    quote_label.config(text=quote)
    author_label.config(text=f"~{author}")

root = ttk.Window(themename="pulse")
root.title("Quotes Generator")
root.geometry("700x250")

frame = ttk.Frame(root)
frame.pack(padx=30, pady=40)

quote_label = ttk.Label(frame, text="", font=("Helvetica", 16), wraplength=650)
quote_label.pack()

author_label = ttk.Label(frame, text="", font=("Helvetica", 12))
author_label.pack(pady=10)

ttk.Button(frame, text="Get Quote", command=update_quote).pack(pady=20)

root.mainloop()