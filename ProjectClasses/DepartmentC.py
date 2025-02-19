"""
class Department:
    def __init__(self, name):

        #Конструктор класса Department (Отдел).

        #Args:
        #    name (str): Название отдела.

        self.name = name  # Название отдела
        self.employees = []  # Список сотрудников, работающих в этом отделе (изначально пустой)

    def add_employee(self, employee):

        #Метод для добавления сотрудника в отдел.

        #Args:
        #   employee (Employee): Объект класса Employee, который нужно добавить в отдел.

        self.employees.append(employee)  # Добавляем сотрудника в список сотрудников отдела

    def __str__(self):

        #Метод для строкового представления объекта Department (для удобного вывода информации).

        #Returns:
        #    str: Строковое представление объекта Department, содержащее название отдела и количество сотрудников в нем.

        return f"Department: {self.name}, Number of employees: {len(self.employees)}"
    """

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.attack_stats = {
            "phishing": {"success_probability": 0.0, "success_count": 0, "total_attacks": 0},
            "malware": {"success_probability": 0.0, "success_count": 0, "total_attacks": 0},
            "social_engineering": {"success_probability": 0.0, "success_count": 0, "total_attacks": 0}
        }  # ВВЕСТИ ДЛЯ СОТРУДНИКОВ

    def add_employee(self, employee):
        self.employees.append(employee)

    def __str__(self):
        return f"Отдел {self.name}: {len(self.employees)} сотрудников"

# Создание организации
departments = {
    "Development": Department("Development"), # Отдел разработки
    "Accounting": Department("Accounting"), # Отдел бухгалтерии
    "HR": Department("HR"), # Отдел по подбору персонала
    "Marketing": Department("Marketing") # Маркетинговый отдел
}