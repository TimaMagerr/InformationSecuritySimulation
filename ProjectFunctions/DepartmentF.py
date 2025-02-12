class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def __str__(self):  # Для удобного вывода информации об отделе
        return f"Department: {self.name}, Number of employees: {len(self.employees)}"