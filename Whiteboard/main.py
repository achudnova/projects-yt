import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

class Whiteboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Whiteboard")
        self.master.resizable(False, False)

        # Set ttkbootstrap style
        self.style = Style(theme="pulse")

        # Create canvas
        self.canvas = tk.Canvas(self.master, width=1200, height=800, bg="white")
        self.canvas.pack()

        # Create buttons
        self.button_frame = ttk.Frame(self.master)
        self.button_frame.pack(side="top", pady=10)

        # Button configuration
        button_config = {
            "black": ("dark.TButton", lambda: self.change_color("black")),
            "red": ("danger.TButton", lambda: self.change_color("red")),
            "blue": ("info.TButton", lambda: self.change_color("blue")),
            "green": ("success.TButton", lambda: self.change_color("green")),
            "clear": ("light.TButton", self.clear_canvas)
        }

        # Add buttons to the button frame
        for color, (style, command) in button_config.items():
            ttk.Button(self.button_frame, text=color.capitalize(), 
                       command=command, style=style).pack(side="left", padx=5, pady=5)
        
        # Initialize drawing variables
        self.draw_color = "black"
        self.line_width = 5
        self.old_x, self.old_y = None, None

        # Add event listeners
        self.canvas.bind("<Button-1>", self.start_line)
        self.canvas.bind("<B1-Motion>", self.draw_line)

    # Save starting point of line
    def start_line(self, event):
        self.old_x, self.old_y = event.x, event.y

    # Draw line from starting point to current point and then update starting point
    def draw_line(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=self.line_width, fill=self.draw_color,
                                    capstyle=tk.ROUND, smooth=tk.TRUE)
            self.old_x, self.old_y = event.x, event.y
    
    # Update current drawing color
    def change_color(self, new_color):
        self.draw_color = new_color
    
    # Delete all objects on canvas
    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    whiteboard = Whiteboard(root)
    root.mainloop()