import tkinter as tk
from tkinter import messagebox

# Цветовые настройки
bg_color = "aquamarine4"        # Цвет фона окна
entry_bg_color = "LemonChiffon3"      # Цвет фона поля ввода
entry_text_color = "black"    # Цвет текста поля ввода
listbox_bg_color = "LemonChiffon3"    # Цвет фона списка задач
listbox_text_color = "black"  # Цвет текста списка задач
button_bg_color = "lightblue" # Цвет фона кнопок
button_text_color = "black"   # Цвет текста кнопок

# Настройки шрифта
font_family = "Arial"
entry_font_size = 12  # Размер шрифта поля ввода
button_font_size = 12  # Размер шрифта кнопок
listbox_font_size = 12  # Размер шрифта списка задач

# Настройки расположения и отступов
padding_x = 10  # Горизонтальный отступ
padding_y = 15   # Вертикальный отступ
entry_width = 40  # Ширина поля ввода
button_width = 20 # Ширина кнопок

# Функция для добавления новой задачи
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Пустая задача", "Введите задачу.")

# Функция для удаления выбранной задачи
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Ошибка", "Выберите задачу для удаления.")

# Функция для пометки задачи как выполненной (изменение цвета)
def mark_done():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.itemconfig(selected_task_index, {'bg': 'lightgreen'})
    except IndexError:
        messagebox.showwarning("Ошибка", "Выберите задачу для завершения.")

# Создание основного окна
root = tk.Tk()
root.title("Менеджер задач")
root.configure(bg=bg_color)  # Установка фона окна

# Поле ввода задачи
entry = tk.Entry(root, width=entry_width, bg=entry_bg_color, fg=entry_text_color, font=(font_family, entry_font_size))
entry.pack(pady=padding_y, padx=padding_x)  # Отступы

# Кнопка добавления задачи
add_button = tk.Button(root, text="Добавить задачу", command=add_task, bg=button_bg_color, fg=button_text_color, width=button_width, font=(font_family, button_font_size))
add_button.pack(pady=padding_y, padx=padding_x)

# Список задач
listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE, bg=listbox_bg_color, fg=listbox_text_color, font=(font_family, listbox_font_size))
listbox.pack(pady=padding_y, padx=padding_x)

# Кнопка удаления задачи
delete_button = tk.Button(root, text="Удалить задачу", command=delete_task, bg=button_bg_color, fg=button_text_color, width=button_width, font=(font_family, button_font_size))
delete_button.pack(pady=padding_y, padx=padding_x)

# Кнопка пометки задачи как выполненной
done_button = tk.Button(root, text="Задача выполнена", command=mark_done, bg=button_bg_color, fg=button_text_color, width=button_width, font=(font_family, button_font_size))
done_button.pack(pady=padding_y, padx=padding_x)

# Запуск главного цикла приложения
root.mainloop()