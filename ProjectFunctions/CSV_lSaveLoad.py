from ProjectClasses.DepartmentC import Department
from ProjectClasses.EmployeeC import Employee
import csv


def save_employees_to_csv(departments, filename="employees.csv"):
    """Сохраняет информацию о сотрудниках из словаря departments в CSV файл."""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')

            # Заголовки столбцов
            headers = ["Name", "Department", "Age", "Experience", "Attentiveness",
                       "Technical Literacy", "Stress Resistance", "Instruction Following",
                       "Learnability", "Social Engineering Awareness", "Reporting Culture",
                       "Authority Respect", "Workload", "Risk Aversion"]
            writer.writerow(headers)  # Записываем заголовки

            for department in departments.values():
                for employee in department.employees:
                    row = [employee.name, employee.department, employee.age, employee.experience,
                           employee.attentiveness, employee.technical_literacy, employee.stress_resistance,
                           employee.instruction_following, employee.learnability, employee.social_engineering_awareness,
                           employee.reporting_culture, employee.authority_respect, employee.workload,
                           employee.risk_aversion]
                    writer.writerow(row)  # Записываем данные сотрудника

        print(f"Сотрудники сохранены в файл {filename}")

    except Exception as e:
        print(f"Произошла ошибка при сохранении в файл {filename}: {e}")


def load_employees_from_csv(filename="employees.csv"):
    """Загружает информацию о сотрудниках из CSV файла и создает объекты Employee.
       Возвращает словарь departments, где ключи - названия отделов, а значения - объекты Department.
    """
    departments = {}
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            headers = next(reader, None)

            if headers is None:
                print(f"Файл {filename} пуст или не содержит заголовков.")
                return {}

            # Проверяем, что заголовки соответствуют ожидаемым
            expected_headers = ["Name", "Department", "Age", "Experience", "Attentiveness",
                               "Technical Literacy", "Stress Resistance", "Instruction Following",
                               "Learnability", "Social Engineering Awareness", "Reporting Culture",
                               "Authority Respect", "Workload", "Risk Aversion"]
            if headers != expected_headers:
                print("Структура CSV файла не соответствует ожидаемой.")
                return {}

            for row in reader:
                try:
                    name, department_name, age, experience, attentiveness, technical_literacy, stress_resistance, instruction_following, learnability, social_engineering_awareness, reporting_culture, authority_respect, workload, risk_aversion = row

                    # Преобразуем типы данных, если это необходимо.
                    age = int(age)
                    experience = int(experience)
                    attentiveness = float(attentiveness)
                    technical_literacy = float(technical_literacy)
                    stress_resistance = float(stress_resistance)
                    instruction_following = float(instruction_following)
                    learnability = float(learnability)
                    social_engineering_awareness = float(social_engineering_awareness)
                    reporting_culture = float(reporting_culture)
                    authority_respect = float(authority_respect)
                    workload = float(workload)
                    risk_aversion = float(risk_aversion)

                    employee = Employee(
                        name=name,
                        department=department_name,
                        age=age,
                        experience=experience,
                        attentiveness=attentiveness,
                        technical_literacy=technical_literacy,
                        stress_resistance=stress_resistance,
                        instruction_following=instruction_following,
                        learnability=learnability,
                        social_engineering_awareness=social_engineering_awareness,
                        reporting_culture=reporting_culture,
                        authority_respect=authority_respect,
                        workload=workload,
                        risk_aversion=risk_aversion
                    )

                    # Получаем или создаем отдел
                    if department_name not in departments:
                        departments[department_name] = Department(department_name)
                    departments[department_name].add_employee(employee)

                except Exception as e:
                    print(f"Ошибка при обработке строки: {row}. Ошибка: {e}")

    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return {}
    except Exception as e:
        print(f"Произошла ошибка при загрузке данных из файла {filename}: {e}")
        return {}

    total_employees = sum(len(dep.employees) for dep in departments.values())
    print(f"Загружено {total_employees} сотрудников из файла {filename} в {len(departments)} отдела.")
    return departments