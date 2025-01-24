import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime('%H:%M:%S:')
    time_label.config(text=current_time)

    current_date = datetime.now().date()
    date_label.config(text=current_date)

    root.after(1000, update_time)

task = [
    'Задача_1'
    'Задача_2'
    'Задача_3'
]

root = tk.Tk()
root.title('Дата, Время и Задча')

time_label = tk.Label(root, font=('Arial', 20), fg='blue')
time_label.pack(pady=10)

update_time()

root.mainloop()



