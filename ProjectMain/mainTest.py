import random
import tkinter as tk
from tkinter import ttk, Toplevel, Text, Scrollbar  # Добавлены Toplevel, Text, Scrollbar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ProjectFunctions.CSV_SaveLoad import save_employees_to_csv, load_employees_from_csv
from ProjectFunctions.EmployeeF import departments, generate_employees

# --- 3. Глобальные переменные ---
loaded_departments = {}  # Здесь будут храниться загруженные данные
num_employees = 0 # Здесь будет храниться количество сотрудников

# --- 4. Функции для работы с данными и графиками ---

def create_employees():
    """Создает сотрудников и сохраняет данные в CSV."""
    global num_employees, loaded_departments
    try:
        num_employees = int(num_employees_entry.get()) #Пытаемся прочитать число из поля ввода
    except ValueError:
        status_label.config(text="Ошибка: Введите целое число сотрудников.")
        return

    for department in departments.values():  # Очищаем существующие отделы
        department.employees = []
    generate_employees(departments, num_employees) #Генерируем сотрудников
    save_employees_to_csv(departments) #Сохраняем
    loaded_departments = departments #Присваиваем сгенерированные данные в loaded_departments
    update_department_info()  # Обновляем информацию об отделах
    update_chart()  # Обновляем график
    status_label.config(text=f"Создано {num_employees} сотрудников и сохранено в файл.")


def load_employees():
    """Загружает сотрудников из CSV."""
    global loaded_departments, num_employees
    for department in departments.values():  # Очищаем существующие отделы
        department.employees = []

    loaded_departments = load_employees_from_csv() #Загружаем
    if loaded_departments:
        num_employees = sum(len(dep.employees) for dep in loaded_departments.values()) #Считаем общее кол-во сотрудников
        update_department_info()  # Обновляем информацию об отделах
        update_chart()  # Обновляем график
        status_label.config(text=f"Загружено {num_employees} сотрудников из файла.")
    else:
        status_label.config(text="Ошибка загрузки данных. Проверьте CSV файл.")


def update_department_info():
    """Обновляет информацию об отделах в текстовых метках."""
    for dept_name, label in department_labels.items():
        if dept_name in loaded_departments:
            label.config(text=f"{dept_name}: {len(loaded_departments[dept_name].employees)} сотрудников")
        else:
            label.config(text=f"{dept_name}: 0 сотрудников (нет данных)")

def update_chart():
    """Обновляет столбчатую диаграмму численности отделов."""
    global loaded_departments
    if not loaded_departments:
        status_label.config(text="Нет данных для отображения графика. Сначала создайте или загрузите сотрудников.")
        return

    department_counts = {}
    for department_name, department in loaded_departments.items():
        department_counts[department_name] = len(department.employees)

    department_names = list(department_counts.keys())
    employee_counts = list(department_counts.values())

    # Очистка старого графика
    for item in chart_frame.winfo_children():
        item.destroy()

    # Создание нового графика
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['skyblue', 'lightgreen', 'lightcoral', 'orange']  # Список цветов
    bars = ax.bar(department_names, employee_counts, color=colors)

    ax.set_xlabel("Отдел")
    ax.set_ylabel("Количество сотрудников")
    ax.set_title("Численность сотрудников по отделам")
    ax.tick_params(axis='x', rotation=45)

    # Добавление подписей с количеством сотрудников внутри столбцов
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

    # Встраивание графика в tkinter окно
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def show_department_employees(department_name):
    """Создает новое окно с таблицей сотрудников для выбранного отдела."""
    if department_name not in loaded_departments:
        status_label.config(text=f"Нет данных для отдела '{department_name}'.")
        return

    department = loaded_departments[department_name]

    # Создаем новое окно
    employee_window = Toplevel(root)
    employee_window.title(f"Сотрудники отдела '{department_name}'")

    # Определяем столбцы таблицы (все характеристики сотрудника)
    columns = ("Имя", "Возраст", "Стаж", "Внимательность", "Тех. грамотность", "Стрессоустойчивость",
               "Следование инструкциям", "Обучаемость", "Осведомленность о социальной инженерии",
               "Культура отчетности", "Уважение к авторитетам", "Рабочая нагрузка", "Склонность к риску")
    tree = ttk.Treeview(employee_window, columns=columns, show="headings") # show="headings" скрывает первый столбец с ID

    # Задаем заголовки для столбцов
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)  # Устанавливаем ширину столбцов

    # Заполняем таблицу данными о сотрудниках
    for employee in department.employees:
        tree.insert("", tk.END, values=(employee.name, employee.age, employee.experience,
                                        f"{employee.attentiveness:.2f}", f"{employee.technical_literacy:.2f}",
                                        f"{employee.stress_resistance:.2f}", f"{employee.instruction_following:.2f}",
                                        f"{employee.learnability:.2f}", f"{employee.social_engineering_awareness:.2f}",
                                        f"{employee.reporting_culture:.2f}", f"{employee.authority_respect:.2f}",
                                        f"{employee.workload:.2f}", f"{employee.risk_aversion:.2f}")) #Используем f-строки для форматирования

    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Добавляем полосу прокрутки
    scrollbar = ttk.Scrollbar(employee_window, orient="vertical", command=tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.configure(yscrollcommand=scrollbar.set)


# --- 5. Создание главного окна ---
root = tk.Tk()
root.title("Симуляция отдела информационной безопасности")

# --- 6. Элементы управления ---
# Рамка для элементов управления
controls_frame = ttk.Frame(root, padding=10)
controls_frame.pack(side=tk.TOP, fill=tk.X)

# Количество сотрудников
ttk.Label(controls_frame, text="Количество сотрудников:").grid(row=0, column=0, sticky=tk.W)
num_employees_entry = ttk.Entry(controls_frame, width=10)
num_employees_entry.grid(row=0, column=1, sticky=tk.W)
num_employees_entry.insert(0, "100")  # Значение по умолчанию

# Кнопки
create_button = ttk.Button(controls_frame, text="Создать сотрудников", command=create_employees)
create_button.grid(row=0, column=2, padx=5, sticky=tk.W)

load_button = ttk.Button(controls_frame, text="Загрузить сотрудников из CSV", command=load_employees)
load_button.grid(row=0, column=3, padx=5, sticky=tk.W)


# --- 7. Рамка для информации об отделах ---
departments_frame = ttk.Frame(root, padding=10)
departments_frame.pack(side=tk.TOP, fill=tk.X)

department_labels = {} #Словарь для хранения labels

# Создание меток для каждого отдела, привязка события клика
i = 0 #Инициализируем счетчик
for dept_name, department in departments.items():
    # Создаем метку с информацией о количестве сотрудников
    label = ttk.Label(departments_frame, text=f"{dept_name}: 0 сотрудников")
    label.grid(row=0, column=i, padx=5, sticky=tk.W)
    department_labels[dept_name] = label

    # Создаем кнопку "Показать сотрудников" для каждого отдела
    show_employees_button = ttk.Button(departments_frame, text=f"Показать сотрудников {dept_name}", command=lambda name=dept_name: show_department_employees(name)) #Создаем кнопку
    show_employees_button.grid(row=1, column=i, padx=5, sticky=tk.W) #Размещаем кнопку
    i += 1 #Увеличиваем счетчик


# --- 8. Рамка для графика ---
chart_frame = ttk.Frame(root, padding=10)
chart_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# --- 9. Метка статуса ---
status_label = ttk.Label(root, text="")
status_label.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

# --- 10. Запуск главного цикла ---
root.mainloop()