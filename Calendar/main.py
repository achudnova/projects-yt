import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import *

root = ttk.Window("Calendar")
root.geometry("450x200")

s = ttk.Style()
s.configure('.', font=('Helvetica',15))

dt = datetime.now().date()

date_entry = ttk.DateEntry(dateformat='%d-%m-%Y',firstweekday=2,startdate=dt, bootstyle=SUCCESS)
date_entry.grid(row=1, column=1, padx=10, pady=20)

def my_upd():
    label.configure(text=date_entry.entry.get())

button = ttk.Button(root,text='Show date',command=lambda:my_upd(), bootstyle=SUCCESS)
button.grid(row=1,column=2)

label=ttk.Label(root,text='Date:', bootstyle=SUCCESS)
label.grid(row=1, column=3, padx=10, pady=20)

root.mainloop()