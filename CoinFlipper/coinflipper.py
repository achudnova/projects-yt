import tkinter as tk
from PIL import ImageTk, Image
import random
import ttkbootstrap as ttk

def flip_coin():
    outcomes = ["heads.png", "tails.png"]
    result = random.choice(outcomes)
    result_image = ImageTk.PhotoImage(Image.open(result))
    result_label.config(image=result_image)
    result_label.image = result_image

window = tk.Tk()
window.title("Coin Flipper")
style = ttk.Style(theme="flatly")

heads_image = ImageTk.PhotoImage(Image.open("heads.png"))
tails_image = ImageTk.PhotoImage(Image.open("tails.png"))

button = ttk.Button(text="Flip Coin", command=flip_coin, style="primary.TButton")
result_label = ttk.Label(image=heads_image)
button.pack(pady=10)
result_label.pack(pady=10)

window.mainloop()