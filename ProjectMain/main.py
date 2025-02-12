import random
import math
from ProjectFunctions.EmployeeF import *
from ProjectFunctions.CSV_lSaveLoad import save_employees_to_csv, load_employees_from_csv
import openpyxl

# Создаем 100 сотрудников
generate_employees(departments, 100)

# Пример вывода информации об отделе и первом сотруднике в нем
print(departments["Development"])
if departments["Development"].employees:
    print(departments["Development"].employees[0])

print("Тип departments:", type(departments))
for department_name, department in departments.items():
    print(f"  Отдел: {department_name}, Тип: {type(department)}")
    print(f"    Количество сотрудников: {len(department.employees)}, Тип списка сотрудников: {type(department.employees)}")
    if department.employees:
        print(f"      Тип первого сотрудника: {type(department.employees[0])}")

save_employees_to_csv(departments)  # Сохраняем сгенерированных сотрудников

# 4. (Опционально) Очистка существующих отделов и загрузка данных из Excel (демонстрация)
for department in departments.values(): # Очищаем списки сотрудников в отделах
    department.employees = []

loaded_departments = load_employees_from_csv() # Загружаем из Excel

# 5. Проверка загруженных данных
if loaded_departments:
    for department_name, department in loaded_departments.items():
        print(f"Отдел: {department_name}, Количество сотрудников: {len(department.employees)}")
        if department.employees:
            print(f"  Первый сотрудник: {department.employees[0]}") # Выводим информацию о первом сотруднике
else:
    print("Не удалось загрузить данные о сотрудниках.")
