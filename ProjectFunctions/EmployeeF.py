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
def generate_employees(num_employees):
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Mallory", "Trent", "Carol", "Harry", "Piter", "Miles", "Rid", "Johny"]  # Список имен
    for i in range(num_employees):
        department_name = random.choice(list(departments.keys()))
        employee = Employee(
            name = random.choice(names) + "_" + str(i), # Добавляем номер, чтобы имена не повторялись
            department=department_name,
            age=random.randint(22, 60),
            experience=random.randint(0, 20),
            attentiveness=random.random(),
            technical_literacy=random.random(),
            stress_resistance=random.random(),
            instruction_following=random.random(),
            learnability=random.random(),
            social_engineering_awareness=random.random(),
            reporting_culture=random.random(),
            authority_respect=random.random(),
            workload=random.random(),  # Или random.randint(1,10) для целочисленного значения
            risk_aversion=random.random()
        )
        departments[department_name].add_employee(employee)