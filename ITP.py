import tkinter as tk

from tkinter import ttk

import sqlite3

def add_employee():

    # Получение данных из текстовых полей

    fio = fio_entry.get()

    phone = phone_entry.get()

    email = email_entry.get()

    salary = salary_entry.get()

    # Вставка данных в базу данных

    conn.execute("INSERT INTO employees (fio, phone, email, salary) VALUES (?, ?, ?, ?)", (fio, phone, email, salary))

    conn.commit()

    def update_employee():

    # Получение данных из текстовых полей

    fio = fio_combobox.get()

    phone = phone_entry.get()

    email = email_entry.get()

    salary = salary_entry.get()

    def update_employee():


        # Обновление данных в базе данных

    conn.execute("UPDATE employees SET phone = ?, email = ?, salary = ? WHERE fio = ?", (phone, email, salary, fio))

    conn.commit()

    def delete_employee():

    # Получение данных из текстовых полей

    fio = fio_combobox.get()

    # Удаление данных из базы данных

    conn.execute("DELETE FROM employees WHERE fio = ?", (fio,))

    conn.commit()def search_employee():

    def search_employee():

    # Получение данных из текстового поля

    fio = search_entry.get()

    # Выполнение поиска с использованием LIKE

    cursor = conn.execute("SELECT * FROM employees WHERE fio LIKE ?", ('%' + fio + '%',))

    for row in cursor:

        print(row)

        # Создание базы данных и таблицы, если они не существуют

conn = sqlite3.connect('company.db')

conn.execute("CREATE TABLE IF NOT EXISTS employees (fio TEXT, phone TEXT, email TEXT, salary REAL)")

# Создание главного окна и рамки

root = tk.Tk()

frame = ttk.Frame(root)

frame.pack(padx=10, pady=10)

# Создание виджетов для добавления сотрудника

ttk.Label(frame, text="ФИО:").grid(row=0, column=0, sticky=tk.W)

fio_entry = ttk.Entry(frame)

fio_entry.grid(row=0, column=1)

ttk.Label(frame, text="Телефон:").grid(row=1, column=0, sticky=tk.W)

phone_entry = ttk.Entry(frame)

phone_entry.grid(row=1, column=1)

ttk.Label(frame, text="Заработная плата:").grid(row=3, column=0, sticky=tk.W)

salary_entry = ttk.Entry(frame)

salary_entry.grid(row=3, column=1)

add_button = ttk.Button(frame, text="Добавить", command=add_employee)

add_button.grid(row=4, column=0, columnspan=2, pady=10)

# Создание виджетов для изменения сотрудника

ttk.Label(frame, text="Выберите сотрудника:").grid(row=5, column=0, sticky=tk.W)

fio_combobox = ttk.Combobox(frame)

fio_combobox.grid(row=5, column=1)

ttk.Label(frame, text="Телефон:").grid(row=6, column=0, sticky=tk.W)

phone_entry = ttk.Entry(frame)

phone_entry.grid(row=6, column=1)

ttk.Label(frame, text="Email:").grid(row=7, column=0, sticky=tk.W)

email_entry = ttk.Entry(frame)

email_entry.grid(row=7, column=1)

ttk.Label(frame, text="Заработная плата:").grid(row=8, column=0, sticky=tk.W)

salary_entry = ttk.Entry(frame)

salary_entry.grid(row=8, column=1)

update_button = ttk.Button(frame, text="Изменить", command=update_employee)

update_button.grid(row=9, column=0, columnspan=2, pady=10)

# Создание виджетов для удаления сотрудника

ttk.Label(frame, text="Выберите сотрудника:").grid(row=10, column=0, sticky=tk.W)

fio_combobox = ttk.Combobox(frame)

fio_combobox.grid(row=10, column=1)

delete_button = ttk.Button(frame, text="Удалить", command=delete_employee)

delete_button.grid(row=11, column=0, columnspan=2, pady=10)

# Создание виджетов для поиска сотрудника

ttk.Label(frame, text="Введите ФИО:").grid(row=12, column=0, sticky=tk.W)

search_entry = ttk.Entry(frame)

search_entry.grid(row=12, column=1)

search_button = ttk.Button(frame, text="Найти", command=search_employee)

search_button.grid(row=13, column=0, columnspan=2, pady=10)



# Запуск приложения

root.mainloop()

# Закрытие соединения с базой данных

conn.close()
