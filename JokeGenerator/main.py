import requests
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# Define the function that gets a random joke from the API and displays it in the label widget
def get_joke():
    # Make an HTTP GET request to the API
    response = requests.get("https://official-joke-api.appspot.com/random_joke")

    # Geet the JSON data from the response and extract the setup and punchline fields
    data = response.json()
    setup = data["setup"]
    punchline = data["punchline"]

    # Set the text of the label widget to the joke
    joke_label.configure(text=f"{setup}\n\n{punchline}")

# Create the GUI window
window = tk.Tk()
window.title("Random Joke Generator")
window.geometry("700x400")
style = Style(theme="flatly")
window.style = style

# Create the label widget
joke_label = tk.Label(text="Click the button to get a random joke!", 
                      font=("TkDefaultFont", 20))
joke_label.place(relx=0.5, rely=0.5, anchor="center")

# Create the "Get Joke" button widget
get_joke_button = ttk.Button(text="Get Joke", command=get_joke)
get_joke_button.pack(pady=20)

window.mainloop()