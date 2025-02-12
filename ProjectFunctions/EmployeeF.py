from ProjectClasses.DepartmentC import Department
from ProjectClasses.EmployeeC import Employee
import random

# Создание организации
departments = {
    "Development": Department("Development"), # Отдел разработки
    "Accounting": Department("Accounting"), # Отдел бухгалтерии
    "HR": Department("HR"), # Отдел по подбору персонала
    "Marketing": Department("Marketing") # Маркетинговый отдел
}


# Генерация случайных сотрудников
def generate_employees(departments, num_employees):
    """Генерирует случайных сотрудников и распределяет их по существующим отделам."""
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Mallory", "Trent", "Carol", "Mary", "Piter", "Vladi", "Alex"]  # Пример списка имен
    department_names = list(departments.keys())  # Получаем список названий отделов

    for i in range(num_employees):
        department_name = random.choice(department_names) # Выбираем случайный отдел
        employee = Employee(
            name = random.choice(names) + "_" + str(i), # Добавляем номер, чтобы имена не повторялись
            department = department_name,
            age = random.randint(22, 60),
            experience = random.randint(0, 20),
            attentiveness = random.random(),
            technical_literacy = random.random(),
            stress_resistance = random.random(),
            instruction_following = random.random(),
            learnability = random.random(),
            social_engineering_awareness = random.random(),
            reporting_culture = random.random(),
            authority_respect = random.random(),
            workload = random.random(),
            risk_aversion = random.random()
        )
        departments[department_name].add_employee(employee) # Добавляем сотрудника в выбранный отдел
    print(f"Сгенерировано {num_employees} случайных сотрудников и распределены по отделам.")