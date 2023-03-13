import tkinter as tk
from ttkbootstrap import Style
import time

class Clock:
    def __init__(self, master):
        self.master = master
        master.title("Clock")

        self.time_label = tk.Label(master, font=("Arial", 80), text="")
        self.time_label.pack(fill=tk.BOTH, expand=True)

        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.master.after(1000, self.update_time)

style = Style()
style.theme_use("morph")

root = style.master
clock = Clock(root)
root.mainloop()