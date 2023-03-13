import tkinter as tk
from ttkthemes import ThemedStyle

class Stopwatch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stopwatch")
        self.geometry("300x250")
        self.time = 0
        self.running = False
        
        self.style = ThemedStyle()
        self.style.set_theme("breeze")
        
        self.label = tk.Label(self, text="0:00:00", pady="20", font=("Helvetica", 35))
        self.label.pack()
        
        self.start_button = tk.Button(self, text="Start", width=10, height=2, font=("Helvetica", 14), command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(self, text="Stop", width=10, height=2, font=("Helvetica", 14), command=self.stop)
        self.stop_button.pack()

        self.reset_button = tk.Button(self, text="Reset", width=10, height=2, font=("Helvetica", 14), command=self.reset)
        self.reset_button.pack()

    def start(self):
        self.running = True
        self.count()
    
    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="0:00:00")

    def count(self):
        if self.running:
            self.time += 1
            minutes, seconds = divmod(self.time, 60)
            hours, minutes = divmod(minutes, 60)
            self.label.config(text="{:01d}:{:02d}:{:02d}".format(hours, minutes, seconds))
            self.after(1000, self.count)

if __name__ == '__main__':
    stopwatch = Stopwatch()
    stopwatch.mainloop()