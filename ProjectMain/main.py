import random
import math
from ProjectFunctions.EmployeeF import *

# Создаем 100 сотрудников
generate_employees(100)

# Пример вывода информации об отделе и первом сотруднике в нем
print(departments["Development"])
if departments["Development"].employees:
    print(departments["Development"].employees[0])
