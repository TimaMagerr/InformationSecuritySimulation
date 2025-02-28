from ProjectClasses.DepartmentC import Department
from ProjectClasses.EmployeeC import Employee
import csv
import tkinter as tk
from tkinter import filedialog


def save_employees_to_csv(departments, filename="employees.csv"):
    """Сохраняет информацию о сотрудниках из словаря departments в CSV файл."""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')

            # Заголовки
            headers = ["Name", "Department", "Age", "Experience", "Attentiveness",
                       "Technical Literacy", "Stress Resistance", "Instruction Following",
                       "Learnability", "Social Engineering Awareness", "Reporting Culture",
                       "Authority Respect", "Workload", "Risk Aversion"]
            writer.writerow(headers)

            for department in departments.values():
                for employee in department.employees:
                    row = [employee.name, employee.department, employee.age, employee.experience,
                           employee.attentiveness, employee.technical_literacy, employee.stress_resistance,
                           employee.instruction_following, employee.learnability, employee.social_engineering_awareness,
                           employee.reporting_culture, employee.authority_respect, employee.workload,
                           employee.risk_aversion]
                    writer.writerow(row)

        print(f"Сотрудники сохранены в файл {filename}")

        save_all_department_data(departments)

    except Exception as e:
        print(f"Произошла ошибка при сохранении в файл {filename}: {e}")


def load_employees_from_csv(departments):
    """
    Загружает информацию о сотрудниках из CSV файла, выбранного пользователем,
    и создает объекты Employee.
    Возвращает словарь departments, где ключи - названия отделов,
    а значения - объекты Department.
    """

    # Открываем диалоговое окно для выбора файла
    filename = filedialog.askopenfilename(
        initialdir=".",  # Начальная директория
        title="Выберите CSV файл с данными о сотрудниках",  # Заголовок окна
        filetypes=(("CSV files", "*.csv"), ("all files", "*.*"))  # Фильтр файлов
    )

    # Если пользователь не выбрал файл, возвращаем пустой словарь
    if not filename:
        print("Загрузка отменена пользователем.")
        return {}

    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';') # Использовать разделитель, который у вас в CSV
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
                print("Структура CSV файла некорректна!")
                return {}

            for row in reader:
                try:
                    name, department_name, age, experience, attentiveness, technical_literacy, stress_resistance, instruction_following, learnability, social_engineering_awareness, reporting_culture, authority_respect, workload, risk_aversion = row

                    # Преобразуем типы данных
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
        print(f"Файл {filename} не найден!")
        return {}
    except Exception as e:
        print(f"Произошла ошибка при загрузке данных из файла {filename}: {e}")
        return {}

    total_employees = sum(len(dep.employees) for dep in departments.values())
    print(f"Загружено {total_employees} сотрудников из файла {filename} в {len(departments)} отдела.")
    save_all_department_data(departments)
    return departments

def save_department_data_to_csv(department, filename=None):
    """
    Сохраняет информацию об отделе (сотрудники и статистика) в CSV файл.

    Args:
        department (Department): Объект отдела, данные которого нужно сохранить.
        filename (str, optional): Имя файла для сохранения. Если не указано, будет предложено выбрать файл.
    """

    if filename is None:
        filename = filedialog.asksaveasfilename(
            initialdir=".",
            title=f"Сохранить данные отдела '{department.name}' в CSV",
            filetypes=(("CSV files", "*.csv"), ("Все файлы", "*.*"))
        )
        if not filename:
            print("Сохранение отменено пользователем.")
            return

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            """
            # Заголовки столбцов (сотрудники)
            employee_headers = ["Имя", "Возраст", "Стаж", "Внимательность",
                               "Тех. грамотность", "Стрессоустойчивость", "Следование инструкциям",
                               "Обучаемость", "Осведомленность о социальной инженерии", "Культура отчетности",
                               "Уважение к авторитетам", "Рабочая нагрузка", "Склонность к риску"]

            # Заголовки столбцов (статистика)
            attack_headers = ["Вероятность успеха фишинга", "Количество успешных фишинг-атак", "Всего фишинг-атак",
                             "Вероятность успеха вредоносного ПО", "Количество успешных атак вредоносного ПО", "Всего атак вредоносного ПО",
                             "Вероятность успеха социальной инженерии", "Количество успешных атак социальной инженерии", "Всего атак социальной инженерии"]
            """

            # Разделяем заголовки на заголовки сотрудников и статистики
            employee_headers = ["Name", "Age", "Experience", "Attentiveness",
                                "Technical Literacy", "Stress Resistance", "Instruction Following",
                                "Learnability", "Social Engineering Awareness", "Reporting Culture",
                                "Authority Respect", "Workload", "Risk Aversion"]
            attack_headers = ["Phishing Success Count", "Phishing Total Attacks",
                              "Malware Success Count", "Malware Total Attacks",
                              "Social Engineering Success Count",
                              "Social Engineering Total Attacks"]

            writer.writerow(["Department:", department.name])  # Записываем название отдела в первой строке
            writer.writerow(employee_headers + attack_headers)  # Записываем заголовки во второй строке

            # Записываем информацию о сотрудниках и статистику
            for employee in department.employees:
                # Данные сотрудника
                row = [employee.name, employee.age, employee.experience,
                       employee.attentiveness, employee.technical_literacy, employee.stress_resistance,
                       employee.instruction_following, employee.learnability, employee.social_engineering_awareness,
                       employee.reporting_culture, employee.authority_respect, employee.workload,
                       employee.risk_aversion]

                attack_stats = [employee.attack_stats["phishing"]["success_count"],
                                employee.attack_stats["phishing"]["total_attacks"],
                                employee.attack_stats["malware"]["success_count"],
                                employee.attack_stats["malware"]["total_attacks"],
                                employee.attack_stats["social_engineering"]["success_count"],
                                employee.attack_stats["social_engineering"]["total_attacks"]]

                writer.writerow(row + attack_stats)  # Записываем строку с данными сотрудника и статистикой отдела

        print(f"Данные отдела '{department.name}' сохранены в файл {filename}")

    except Exception as e:
        print(f"Произошла ошибка при сохранении в файл {filename}: {e}")


def save_all_department_data(departments):
    """Сохраняет данные каждого отдела в отдельный CSV файл."""
    for department_name, department in departments.items():
        # Создаем имя файла на основе имени отдела (можно добавить префикс или суффикс)
        filename = f"department_{department_name}.csv"
        # и сохраняем данные
        save_department_data_to_csv(department, filename)

def load_department_data_from_csv(filename):
    """Загружает информацию об отделе (сотрудники и статистика) из CSV файла."""
    departments = {}  # словарь для хранения данных (отделов)
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')

            # Читаем название отдела
            first_row = next(reader, None)
            if first_row is None or len(first_row) < 2 or first_row[0] != "Department:":
                print(f"Файл {filename} имеет некорректный формат (отсутствует название отдела).")
                return None

            department_name = first_row[1]

            # Читаем заголовки
            headers = next(reader, None)
            if headers is None:
                print(f"Файл {filename} пуст или не содержит заголовков.")
                return None

            # Разделяем заголовки на заголовки сотрудников и статистики
            employee_headers = ["Name", "Age", "Experience", "Attentiveness",
                                "Technical Literacy", "Stress Resistance", "Instruction Following",
                                "Learnability", "Social Engineering Awareness", "Reporting Culture",
                                "Authority Respect", "Workload", "Risk Aversion"]
            attack_headers = ["Phishing Success Count", "Phishing Total Attacks",
                              "Malware Success Count", "Malware Total Attacks",
                              "Social Engineering Success Count",
                              "Social Engineering Total Attacks"]

            # Проверяем, что заголовки соответствуют ожидаемым
            expected_headers = employee_headers + attack_headers
            if headers != expected_headers:
                print("Структура CSV файла некорректна!")
                return None

            # Создаем отдел
            department = Department(department_name)

            for row in reader:
                try:
                    # Разделяем строку на данные сотрудника и статистику
                    employee_data = row[:len(employee_headers)]  # Берем данные о сотруднике
                    attack_data = row[len(employee_headers):]  # Берем данные об атаках

                    name, age, experience, attentiveness, technical_literacy, stress_resistance, instruction_following, learnability, social_engineering_awareness, reporting_culture, authority_respect, workload, risk_aversion = employee_data  # Распаковываем

                    # Преобразуем типы данных
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

                    # Загружаем статистику об атаках
                    phishing_success_count = int(attack_data[0])
                    phishing_total_attacks = int(attack_data[1])
                    malware_success_count = int(attack_data[2])
                    malware_total_attacks = int(attack_data[3])
                    social_engineering_success_count = int(attack_data[4])
                    social_engineering_total_attacks = int(attack_data[5])

                    employee.attack_stats["phishing"]["success_count"] = phishing_success_count
                    employee.attack_stats["phishing"]["total_attacks"] = phishing_total_attacks
                    employee.attack_stats["malware"]["success_count"] = malware_success_count
                    employee.attack_stats["malware"]["total_attacks"] = malware_total_attacks
                    employee.attack_stats["social_engineering"]["success_count"] = social_engineering_success_count
                    employee.attack_stats["social_engineering"]["total_attacks"] = social_engineering_total_attacks

                    department.add_employee(employee)  # Добавляем сотрудника

                except Exception as e:
                    print(f"Ошибка при обработке строки: {row}. Ошибка: {e}")
                    return None

            print(f"Данные отдела '{department_name}' загружены из файла {filename}")
            departments[department_name] = department
            return departments

    except FileNotFoundError:
        print(f"Файл {filename} не найден!") #Сообщение на русском
        return None
    except Exception as e:
        print(f"Произошла ошибка при загрузке данных из файла {filename}: {e}")
        return None