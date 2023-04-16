import tkinter as tk
import random

# Function to generate random colors
def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # format the color as a hex string
    color = f'#{r:02x}{g:02x}{b:02x}'
    return color

# Define a function that generated a color palette
def generate_palette():
    num_colors = int(select_field.get())
    for widget in color_frame.winfo_children():
        widget.destroy()
    for i in range(num_colors):
        color = generate_color()
        color_label = tk.Label(color_frame, bg=color, width=10, height=5)
        color_label.grid(row=i, column=0, padx=5, pady=5)
        hex_label = tk.Label(color_frame, text=color, width=10)
        hex_label.grid(row=i, column=1, padx=5, pady=5)

root = tk.Tk()
root.title("Color Palette Generator")
root.geometry("300x600")

select_field = tk.StringVar(value="1")
select = tk.OptionMenu(root, select_field, "1", "2", "3", "4", "5")
select.pack(side="top", pady=10)

generate_button = tk.Button(root, text="Generate", command=generate_palette)
generate_button.pack(side="top")

color_frame = tk.Frame(root)
color_frame.pack(pady=10)

root.mainloop()