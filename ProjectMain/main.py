import random
import math
import matplotlib.pyplot as plt
from ProjectFunctions.EmployeeF import *
from ProjectFunctions.CSV_SaveLoad import save_employees_to_csv, load_employees_from_csv
import openpyxl

# Создаем 100 сотрудников
num_employees = 100
#generate_employees(departments, num_employees)
#save_employees_to_csv(departments)  # Сохраняем сгенерированных сотрудников
loaded_departments = load_employees_from_csv() # Загружаем из файла

department_counts = {}
for department_name, department in loaded_departments.items():
    department_counts[department_name] = len(department.employees)

print("Количество сотрудников в отделах:", department_counts) #Вывод для отладки

# --- 6. Визуализация численности отделов ---
department_names = list(department_counts.keys())
employee_counts = list(department_counts.values())

# Цвета для каждого отдела
colors = ['skyblue', 'lightgreen', 'lightcoral', 'orange'] #Список цветов
#Если отделов больше чем цветов, то цвета будут повторяться.  Можно сделать генерацию случайных цветов.

plt.figure(figsize=(10, 6))  # Размер графика
bars = plt.bar(department_names, employee_counts, color=colors) #Сохраняем объекты столбиков в переменной bars
plt.xlabel("Отдел") #Подпись оси X
plt.ylabel("Количество сотрудников") #Подпись оси Y
plt.title("Численность сотрудников по отделам") #Заголовок графика
plt.xticks(rotation=45, ha="right") #Поворот подписей на оси X для читаемости

# Добавление подписей с количеством сотрудников внутри столбцов
for bar in bars:
    yval = bar.get_height()  # Получаем высоту столбца
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom') #Пишем текст

plt.tight_layout()  # Автоматическая корректировка параметров, чтобы все поместилось
plt.show() #Отображаем график

"""
# Пример вывода информации об отделе и первом сотруднике в нем
print(departments["Development"]) # Нам выведут число работников отдела разработки
if departments["Development"].employees:
    print(departments["Development"].employees[0])

print("Тип departments:", type(departments))
for department_name, department in departments.items():
    print(f"  Отдел: {department_name}, Тип: {type(department)}")
    print(f"    Количество сотрудников: {len(department.employees)}, Тип списка сотрудников: {type(department.employees)}")
    if department.employees:
        print(f"      Тип первого сотрудника: {type(department.employees[0])}")

save_employees_to_csv(departments)  # Сохраняем сгенерированных сотрудников

# Очистка существующих отделов и загрузка данных из Excel
for department in departments.values(): # Очищаем списки сотрудников в отделах
    department.employees = []

loaded_departments = load_employees_from_csv() # Загружаем из файла

# Проверка загруженных данных
if loaded_departments:
    for department_name, department in loaded_departments.items():
        print(f"Department: {department_name}, Number of employees: {len(department.employees)}")
        if department.employees:
            print(f"  First employee: {department.employees[0]}") # Выводим информацию о первом сотруднике
else:
    print("Не удалось загрузить данные о сотрудниках.")
"""
