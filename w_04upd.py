import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# Функция для обновления времени и даты
def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    time_label.config(text=current_time)

    current_date = datetime.now().date()
    date_label.config(text=current_date)

    # Обновляем каждые 1000 мс (1 секунда)
    root.after(1000, update_time)


# Функция для добавления новой задачи
def add_task():
    new_task = entry.get()
    if new_task != '':
        tasks.append(new_task)
        task_list.delete(0, tk.END)
        for task in tasks:
            task_list.insert(tk.END, task)
        entry.delete(0, tk.END)


# Функция для удаления задачи
def delete_task():
    try:
        selected_index = task_list.curselection()[0]
        tasks.pop(selected_index)
        task_list.delete(selected_index)
    except IndexError:
        pass


# Функция для редактирования задачи
def edit_task():
    def save_edits():
        edited_task = edit_entry.get()
        if edited_task != '':
            tasks[index] = edited_task
            task_list.delete(index)
            task_list.insert(index, edited_task)
            edit_window.destroy()

    try:
        index = task_list.curselection()[0]
        selected_task = tasks[index]

        # Открываем новое окно для редактирования задачи
        edit_window = tk.Toplevel(root)
        edit_window.title("Редактирование задачи")

        # Метка и поле для редактирования задачи
        edit_label = tk.Label(edit_window, text="Введите измененную задачу:")
        edit_label.pack(pady=10)

        edit_entry = tk.Entry(edit_window, width=30)
        edit_entry.insert(0, selected_task)
        edit_entry.pack(pady=10)

        # Кнопка для сохранения изменений
        save_button = tk.Button(edit_window, text="Сохранить изменения", command=save_edits)
        save_button.pack(pady=10)
    except IndexError:
        messagebox.showerror("Ошибка", "Пожалуйста, выберите задачу для редактирования.")


# Список задач
tasks = [
    'Задача 1',
    'Задача 2',
    'Задача 3'
]

# Создаем главное окно
root = tk.Tk()
root.title('Дата, Время, Задача')

# Создаем метки для отображения даты и времени
time_label = tk.Label(root, font=('Arial', 20), fg='blue')
time_label.pack(pady=10)

date_label = tk.Label(root, font=('Arial', 16))
date_label.pack(pady=10)

# Поле для ввода новой задачи
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Кнопка для добавления новой задачи
add_button = tk.Button(root, text='Добавить задачу', command=add_task)
add_button.pack(pady=10)

# Кнопка для удаления задачи
delete_button = tk.Button(root, text='Удалить задачу', command=delete_task)
delete_button.pack(pady=10)

# Кнопка для редактирования задачи
edit_button = tk.Button(root, text='Редактировать задачу', command=edit_task)
edit_button.pack(pady=10)

# Отображаем список задач
task_list = tk.Listbox(root, height=len(tasks), width=50)
for task in tasks:
    task_list.insert(tk.END, task)
task_list.pack(padx=20, pady=20)

# Запускаем функцию обновления времени
update_time()

# Запускаем главный цикл приложения
root.mainloop()