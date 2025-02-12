class Department:
    def __init__(self, name):
        """
        Конструктор класса Department (Отдел).

        Args:
            name (str): Название отдела.
        """
        self.name = name  # Название отдела
        self.employees = []  # Список сотрудников, работающих в этом отделе (изначально пустой)

    def add_employee(self, employee):
        """
        Метод для добавления сотрудника в отдел.

        Args:
            employee (Employee): Объект класса Employee, который нужно добавить в отдел.
        """
        self.employees.append(employee)  # Добавляем сотрудника в список сотрудников отдела

    def __str__(self):
        """
        Метод для строкового представления объекта Department (для удобного вывода информации).

        Returns:
            str: Строковое представление объекта Department, содержащее название отдела и количество сотрудников в нем.
        """
        return f"Department: {self.name}, Number of employees: {len(self.employees)}"