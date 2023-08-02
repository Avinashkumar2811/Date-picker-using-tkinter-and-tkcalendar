import tkinter as tk
from tkcalendar import Calendar

def get_selected_date():
    selected_date = cal.get_date()
    print("Selected date:", selected_date)

root = tk.Tk()
root.title("Date Picker")

cal = Calendar(root, selectmode='day', date_pattern='dd/mm/yyyy')
cal.pack(pady=20)

btn = tk.Button(root, text="Get Selected Date", command=get_selected_date)
btn.pack(pady=10)

root.mainloop()
