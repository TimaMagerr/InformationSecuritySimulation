import random
import tkinter as tk
from tkinter import ttk, Toplevel, Text, Scrollbar, filedialog  # Добавлены Toplevel, Text, Scrollbar
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from ProjectClasses.DepartmentC import departments
from ProjectFunctions.AttackSimulation import perform_department_attack_simulation
from ProjectFunctions.CSV_SaveLoad import save_employees_to_csv, load_employees_from_csv, save_department_data_to_csv, \
    save_all_department_data, load_department_data_from_csv
from ProjectFunctions.EmployeeF import generate_employees
from ProjectFunctions.TrainingF import perform_department_training

# --- Глобальные переменные ---
loaded_departments = {}  # Здесь будут храниться загруженные данные
num_employees = 0 # Здесь будет храниться количество сотрудников

# --- Функции для работы с данными и графиками ---
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

    loaded_departments = load_employees_from_csv(departments) #Загружаем, передавая departments
    if loaded_departments:
        num_employees = sum(len(dep.employees) for dep in loaded_departments.values()) #Считаем общее кол-во сотрудников
        update_department_info()  # Обновляем информацию об отделах
        update_chart()  # Обновляем график
        status_label.config(text=f"Загружено {num_employees} сотрудников из файла.")
    else:
        status_label.config(text="Ошибка загрузки данных. Проверьте CSV файл.")

def load_departments_data():
    """Загружает данные отделов из отдельных CSV файлов."""
    global loaded_departments

    # Открываем диалоговое окно для выбора нескольких файлов
    filenames = filedialog.askopenfilenames(
        initialdir=".",
        title="Выберите CSV файлы с данными отделов",
        filetypes=(("CSV files", "*.csv"), ("Все файлы", "*.*"))
    )

    if not filenames:
        print("Загрузка отменена пользователем.")
        return

    for filename in filenames:
        department_data = load_department_data_from_csv(filename)
        if department_data:
            loaded_departments.update(department_data)

    update_department_info()  # Обновляем информацию об отделах в GUI
    status_label.config(text="Данные отделов загружены из файлов.")


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
    else:
        # ******************** Загрузка отделов ******************** #
        department = loaded_departments[department_name]

        # Создаем новое окно
        employee_window = Toplevel(root)
        employee_window.title(f"Сотрудники отдела '{department_name}'")

        # Определяем столбцы таблицы (все характеристики сотрудника)
        columns = ["Имя", "Возраст", "Стаж", "Внимательность", "Тех. грамотность", "Стрессоустойчивость",
                   "Следование инструкциям", "Обучаемость", "Осведомленность о социальной инженерии",
                   "Культура отчетности", "Уважение к авторитетам", "Рабочая нагрузка", "Склонность к риску",
                   "Количество успешных фишинг-атак", "Всего фишинг-атак",
                   "Количество успешных атак вредоносного ПО", "Всего атак вредоносного ПО",
                   "Количество успешных атак социальной инженерии", "Всего атак социальной инженерии"]
        tree = ttk.Treeview(employee_window, columns=columns,
                            show="headings")  # show="headings" скрывает первый столбец с ID

        # Задаем заголовки для столбцов
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)  # Устанавливаем ширину столбцов

        # Заполняем таблицу данными о сотрудниках
        for employee in department.employees:
            tree.insert("", tk.END, values=(employee.name, employee.age, employee.experience,
                                            f"{employee.attentiveness:.2f}", f"{employee.technical_literacy:.2f}",
                                            f"{employee.stress_resistance:.2f}",
                                            f"{employee.instruction_following:.2f}",
                                            f"{employee.learnability:.2f}",
                                            f"{employee.social_engineering_awareness:.2f}",
                                            f"{employee.reporting_culture:.2f}", f"{employee.authority_respect:.2f}",
                                            f"{employee.workload:.2f}",
                                            f"{employee.risk_aversion:.2f}",
                                            employee.attack_stats['phishing']['success_count'],
                                            employee.attack_stats['phishing']['total_attacks'],
                                            employee.attack_stats['malware']['success_count'],
                                            employee.attack_stats['malware']['total_attacks'],
                                            employee.attack_stats['social_engineering']['success_count'],
                                            employee.attack_stats['social_engineering']['total_attacks']))

        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Добавляем полосу прокрутки
        scrollbar = ttk.Scrollbar(employee_window, orient="vertical", command=tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.configure(yscrollcommand=scrollbar.set)
        return

def simulation_attack_read():
    """Считывает параметры атаки из GUI и запускает симуляцию."""
    attack_type = attack_type_combobox.get()  # Получаем выбранный тип атаки
    try:
        count_attacks = int(count_attacks_entry.get())  # Получаем количество атак
    except ValueError:
        status_label.config(text="Ошибка: Введите целое число для количества атак.")
        return

    department_name = attack_department_combobox.get()  # Получаем выбранный отдел для атаки
    perform_attack_and_update(department_name, attack_type, count_attacks)  # Вызываем функцию симуляции

def perform_training_read():
    """Считывает параметры тренинга из GUI и запускает тренинг для отдела."""
    training_type = training_type_combobox.get()
    try:
        intensity = float(intensity_entry.get())
        if not 0.0 <= intensity <= 1.0:
            status_label.config(text="Ошибка: Интенсивность тренинга должна быть от 0.0 до 1.0.")
            return
    except ValueError:
        status_label.config(text="Ошибка: Введите число для интенсивности тренинга.")
        return

    department_name = attack_department_combobox.get()  # Получаем выбранный отдел для атаки
    perform_training_and_update(department_name, training_type, intensity)

def perform_attack_and_update(department_name, attack_type, count_attacks):
    """
    Симулирует атаки указанного типа на указанный отдел, обновляет статистику и отображает комбинированную столбчатую диаграмму.
    """
    global loaded_departments

    if department_name not in loaded_departments:
        status_label.config(text=f"Отдел '{department_name}' не найден.")
        return

    department = loaded_departments[department_name]
    department = perform_department_attack_simulation(department, attack_type, count_attacks)
    save_department_data_to_csv(department, f"department_{department_name}.csv")
    show_department_employees(department_name)
    status_label.config(text=f"Симуляция атаки '{attack_type}' ({count_attacks} атак) на отдел '{department_name}' завершена. Статистика обновлена и сохранена.")

    employee_names = [employee.name for employee in department.employees]
    success_counts = []
    total_attacks = []

    for employee in department.employees:
        success_counts.append(employee.attack_stats[attack_type]["success_count"])
        total_attacks.append(employee.attack_stats[attack_type]["total_attacks"])

    failure_counts = [total - success for total, success in zip(total_attacks, success_counts)] #Кол-во неуспешных атак

    # Создаем график
    fig, ax = plt.subplots(figsize=(10, 6))
    width = 0.75 #Ширина столбца

    ax.bar(employee_names, success_counts, width, label='Успешные атаки', color='green') #Успешные атаки
    ax.bar(employee_names, failure_counts, width, bottom=success_counts, label='Неуспешные атаки', color='red') #Неуспешные атаки

    ax.set_xlabel('Сотрудники') #Надпись для Х
    ax.set_ylabel('Количество атак') #Надпись для Y
    ax.set_title(f'Результаты атак типа "{attack_type}" в отделе "{department_name}"') #Заголовок
    ax.legend() #Легенда

    plt.xticks(rotation=45, ha='right') #Подписи X
    plt.tight_layout() #Автоматическое размещение элементов, чтобы они не налезали друг на друга
    plt.show() #Показ графика

def perform_training_and_update(department_name, training_type, intensity):
    """
    Проводит тренинг указанного типа для выбранного отдела и обновляет статистику в CSV файлах.
    """
    global loaded_departments

    if department_name not in loaded_departments:
        status_label.config(text=f"Отдел '{department_name}' не найден.")
        return

    department = loaded_departments[department_name]
    department = perform_department_training(department, training_type, intensity)
    # Сохраняем данные в CSV файлы
    save_department_data_to_csv(department, f"department_{department_name}.csv")  # Сохраняем данные отдела
    show_department_employees(department_name) #Показываем табличку

    status_label.config(text=f"Тренинг '{training_type}' с интенсивностью {intensity:.2f} успешно проведен для отдела '{department_name}'.")
    show_training_progress(department_name, training_type)

#Функция для отображения прогресса после тренинга:
def show_training_progress(department_name, training_type):
    """
    Отображает график прогресса сотрудников после тренинга.
    """
    global loaded_departments

    if department_name not in loaded_departments:
        status_label.config(text=f"Отдел '{department_name}' не найден.")
        return

    department = loaded_departments[department_name]

    employee_names = [employee.name for employee in department.employees]
    initial_values = {}
    final_values = {}

    # Получаем начальные и конечные значения характеристик для каждого сотрудника
    for employee in department.employees:
        if training_type == "phishing":
            characteristics = ["attentiveness", "technical_literacy", "social_engineering_awareness"]
        elif training_type == "password":
            characteristics = ["instruction_following", "technical_literacy", "risk_aversion"]
        elif training_type == "data_handling":
            characteristics = ["instruction_following", "technical_literacy", "attentiveness"]
        elif training_type == "stress":
            characteristics = ["stress_resistance", "reporting_culture", "attentiveness"]
        elif training_type == "social_engineering":
            characteristics = ["social_engineering_awareness", "attentiveness", "authority_respect", "risk_aversion"]
        else:
            status_label.config(text="Неизвестный тип тренинга.")
            return

        initial_values[employee.name] = {char: getattr(employee, char) for char in characteristics}
        final_values[employee.name] = {}
        for char in characteristics:
            final_values[employee.name][char] = getattr(employee, char)

    # --- Создаем график ---
    fig, ax = plt.subplots(figsize=(12, 8))  # Увеличиваем размер графика для лучшей читаемости
    width = 0.35  # Ширина столбцов

    x = np.arange(len(employee_names))  # Позиции для столбцов

    # Создаем столбцы для начальных и конечных значений
    for i, char in enumerate(characteristics):
        initial = [initial_values[name][char] for name in employee_names]
        final = [final_values[name][char] for name in employee_names]

        x_pos = x + i * width  # Смещаем столбцы для каждой характеристики
        ax.bar(x_pos, initial, width, label=f"{char} (Начальное)", color=f'C{i}', alpha=0.5)
        ax.bar(x_pos, final, width, label=f"{char} (Конечное)", color=f'C{i}')

    # Настраиваем график
    ax.set_xlabel('Сотрудники')
    ax.set_ylabel('Значение характеристики')
    ax.set_title(f'Прогресс после тренинга "{training_type}" в отделе "{department_name}"')
    ax.set_xticks(x + width * (len(characteristics) - 1) / 2)  # Выравниваем метки оси X
    ax.set_xticklabels(employee_names, rotation=45, ha='right')  # Наклоняем подписи оси X для читаемости

    ax.legend()  # Добавляем легенду

    plt.tight_layout()  # Автоматически размещаем элементы, чтобы они не налезали друг на друга
    plt.show()  # Показ графика

def show_department_attack_stats(department_name, attack_type):
    """
    Отображает комбинированную столбчатую диаграмму для указанного отдела и типа атаки.
    """
    global loaded_departments

    if department_name not in loaded_departments:
        status_label.config(text=f"Отдел '{department_name}' не найден.")
        return

    department = loaded_departments[department_name]

    employee_names = [employee.name for employee in department.employees]
    success_counts = []
    total_attacks = []

    for employee in department.employees:
        success_counts.append(employee.attack_stats[attack_type]["success_count"])
        total_attacks.append(employee.attack_stats[attack_type]["total_attacks"])

    failure_counts = [total - success for total, success in zip(total_attacks, success_counts)]  # Кол-во неуспешных атак

    # Создаем график
    fig, ax = plt.subplots(figsize=(10, 6))
    width = 0.75  # Ширина столбца

    ax.bar(employee_names, success_counts, width, label='Успешные атаки', color='green')  # Успешные атаки
    ax.bar(employee_names, failure_counts, width, bottom=success_counts, label='Неуспешные атаки', color='red')  # Неуспешные атаки

    ax.set_xlabel('Сотрудники')  # Надпись для Х
    ax.set_ylabel('Количество атак')  # Надпись для Y
    ax.set_title(f'Результаты атак типа "{attack_type}" в отделе "{department_name}"')  # Заголовок
    ax.legend()  # Легенда

    plt.xticks(rotation=45, ha='right')  # Подписи X
    plt.tight_layout()  # Автоматическое размещение элементов, чтобы они не налезали друг на друга
    plt.show()  # Показ графика


# --- Создание главного окна ---
root = tk.Tk()
root.title("Симуляция отдела информационной безопасности")

# --- Элементы управления ---
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

department_labels = {} #Словарь для хранения labels

# --- Рамка для информации об отделах ---
departments_frame = ttk.Frame(root, padding=10)
departments_frame.pack(side=tk.TOP, fill=tk.X)
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

    # --- Выпадающий список с типами атак ---
    attack_type_combobox = ttk.Combobox(departments_frame, values=["phishing", "malware", "social_engineering"],
                                        state="readonly")
    attack_type_combobox.grid(row=2, column=i, padx=5, sticky=tk.W)
    attack_type_combobox.set("phishing")  # Значение по умолчанию

    # --- Кнопка "Показать статистику атак" ---
    show_attack_stats_button = ttk.Button(departments_frame, text=f"Статистика атак {dept_name}", command=lambda name=dept_name, combo=attack_type_combobox: show_department_attack_stats(name, combo.get()))
    show_attack_stats_button.grid(row=3, column=i, padx=5, sticky=tk.W)
    i += 1 #Увеличиваем счетчик

save_departments_button = ttk.Button(departments_frame, text="Сохранить данные по отделам", command=lambda: save_all_department_data(loaded_departments)) #Создаем кнопку
save_departments_button.grid(row=5, column=0, padx=5, sticky=tk.W) #Выделяем место
# Кнопка загрузки данных отделов
load_departments_button = ttk.Button(departments_frame, text="Загрузить данные отделов", command=load_departments_data)
load_departments_button.grid(row=5, column=1, padx=5, sticky=tk.W)

# --- Тип атаки ---
ttk.Label(controls_frame, text="Тип атаки:").grid(row=1, column=0, sticky=tk.W)
attack_type_combobox = ttk.Combobox(controls_frame, values=["phishing", "malware", "social_engineering"],
                                    state="readonly")
attack_type_combobox.grid(row=1, column=1, sticky=tk.W)
attack_type_combobox.set("phishing")  # Значение по умолчанию

# --- Количество атак ---
ttk.Label(controls_frame, text="Количество атак:").grid(row=2, column=0, sticky=tk.W)
count_attacks_entry = ttk.Entry(controls_frame, width=10)
count_attacks_entry.grid(row=2, column=1, sticky=tk.W)
count_attacks_entry.insert(0, "1")  # Значение по умолчанию

# --- Отдел для атаки ---
ttk.Label(controls_frame, text="Отдел для атаки/тренинга:").grid(row=3, column=0, sticky=tk.W)
attack_department_combobox = ttk.Combobox(controls_frame, values=list(departments.keys()),
                                          state="readonly")
attack_department_combobox.grid(row=3, column=1, sticky=tk.W)
attack_department_combobox.set(list(departments.keys())[0])  # Первый отдел по умолчанию

# --- Кнопка "Симулировать атаку" ---
simulate_button = ttk.Button(controls_frame, text="Симулировать атаку", command=lambda: simulation_attack_read())
simulate_button.grid(row=4, column=0, padx=5, sticky=tk.W)

# --- Тип тренинга ---
ttk.Label(controls_frame, text="Тип тренинга:").grid(row=5, column=0, sticky=tk.W)
training_type_combobox = ttk.Combobox(controls_frame,
                                      values=["phishing", "password", "data_handling", "stress", "social_engineering"],
                                      state="readonly")
training_type_combobox.grid(row=5, column=1, sticky=tk.W)
training_type_combobox.set("phishing")  # Значение по умолчанию

# --- Интенсивность тренинга ---
ttk.Label(controls_frame, text="Интенсивность тренинга:").grid(row=6, column=0, sticky=tk.W)
intensity_entry = ttk.Entry(controls_frame, width=10)
intensity_entry.grid(row=6, column=1, sticky=tk.W)
intensity_entry.insert(0, "0.5")  # Значение по умолчанию

# --- Кнопка "Провести тренинг" ---
train_button = ttk.Button(controls_frame, text="Провести тренинг", command=lambda: perform_training_read())
train_button.grid(row=7, column=0, padx=5, sticky=tk.W)

# --- Рамка для графика ---
chart_frame = ttk.Frame(root, padding=10)
chart_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# --- Метка статуса ---
status_label = ttk.Label(root, text="")
status_label.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

# --- Запуск главного цикла ---
root.mainloop()