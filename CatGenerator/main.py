import io
import tkinter as tk
import requests
from ttkbootstrap import Style, ttk
from PIL import Image, ImageTk

# API URLs
CAT_IMAGE_API = "https://cataas.com/cat"
CAT_FACT_API = "https://catfact.ninja/fact"

# Create the main window
root = tk.Tk()
root.title("Random Cat Generator")
root.geometry("600x600")

# Create a function to generate a new cat fact and picture
def generate_cat():
    # Get a random cat fact from the API
    fact_response = requests.get(CAT_FACT_API)
    fact_json = fact_response.json()
    cat_fact = fact_json['fact']

    # Get a random cat picture from the API
    pic_response = requests.get(CAT_IMAGE_API)
    pic_bytes = pic_response.content
    pic_data_stream = io.BytesIO(pic_bytes)
    cat_image = Image.open(pic_data_stream)
    cat_image = cat_image.resize((400, 400))
    cat_image = ImageTk.PhotoImage(cat_image)

    # Display the cat fact and picture in the GUI
    fact_label.config(text=cat_fact)
    pic_label.config(image=cat_image)
    pic_label.image = cat_image

# Create the GUI elements
style = Style(theme="flatly")
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

fact_label = tk.Label(frame, text="Click on the button to generate a random cat fact and picture!", wraplength=500, font=("TkDefaultFont", 17))
fact_label.pack(padx=10, pady=10)

pic_label = tk.Label(frame)
pic_label.pack(padx=10, pady=10)

generate_button = ttk.Button(frame, text="Generate", command=generate_cat)
generate_button.pack(padx=10, pady=20)

root.mainloop()