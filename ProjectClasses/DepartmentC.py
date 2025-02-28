class Department:
    """
    # Конструктор класса Department (Отдел).
    #Args:
        name(str): название отдела
        employees(list): список сотрудников
    """
    def __init__(self, name):
        self.name = name
        self.employees = []

    # Метод для добавления сотрудника в отдел.
    def add_employee(self, employee):
        self.employees.append(employee)

    # Метод для вывода информации
    def __str__(self):
        return f"Отдел {self.name}: {len(self.employees)} сотрудников"

# Создание организации
departments = {
    "Development": Department("Development"), # Отдел разработки
    "Accounting": Department("Accounting"), # Отдел бухгалтерии
    "HR": Department("HR"), # Отдел по подбору персонала
    "Marketing": Department("Marketing") # Маркетинговый отдел
}