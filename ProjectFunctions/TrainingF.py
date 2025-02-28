import random

def apply_training(employee, training_type, intensity):
    """
    Применяет тренинг к сотруднику и изменяет его параметры в зависимости от типа тренинга.
    Учитывает фактор "успешности обучения", чтобы имитировать ситуацию, когда сотрудник
    может не усвоить материал, даже пройдя тренинг.

    Args:
        employee (Employee): Объект сотрудника, к которому применяется тренинг.
        training_type (str): Тип тренинга ("phishing", "password", "data_handling", "stress", "social_engineering").
        intensity (float): Интенсивность тренинга (0.0 - 1.0).  Чем выше значение, тем более интенсивный тренинг.
    """

    # Вероятность успешного усвоения материала тренинга (основано на случайности)
    training_success_rate = 0.4  # Граница неуспеха

    if random.random() > training_success_rate: #Если число больше границы - тренинг успешен
        if training_type == "phishing":
            # Тренинг по осведомленности о фишинге
            employee.attentiveness = min(1.0, employee.attentiveness + 0.2 * intensity * employee.learnability) # Повышаем внимательность
            employee.technical_literacy = min(1.0, employee.technical_literacy + 0.15 * intensity * employee.learnability) # Повышаем тех. грамотность
            employee.social_engineering_awareness = min(1.0, employee.social_engineering_awareness + 0.2 * intensity * employee.learnability) # Повышаем осведомленность в соц.инженерии

        elif training_type == "password":
            # Тренинг по управлению надежными паролями
            employee.instruction_following = min(1.0, employee.instruction_following + 0.25 * intensity * employee.learnability) # Повышаем следование инструкциям
            employee.technical_literacy = min(1.0, employee.technical_literacy + 0.1 * intensity * employee.learnability) # Повышаем тех. грамотность
            employee.risk_aversion = min(1.0, employee.risk_aversion - 0.05 * intensity * employee.learnability) #Понижаем склонность к риску

        elif training_type == "data_handling":
            # Тренинг по безопасной обработке данных
            employee.instruction_following = min(1.0, employee.instruction_following + 0.2 * intensity * employee.learnability) # Повышаем следование инструкциям
            employee.technical_literacy = min(1.0, employee.technical_literacy + 0.15 * intensity * employee.learnability) # Повышаем тех. грамотность
            employee.attentiveness = min(1.0, employee.attentiveness + 0.1 * intensity * employee.learnability) # Повышаем внимательность

        elif training_type == "stress":
            # Тренинг по управлению стрессом и сообщениям об инцидентах
            employee.stress_resistance = min(1.0, employee.stress_resistance + 0.3 * intensity * employee.learnability) # Повышаем стрессоустойчивость
            employee.reporting_culture = min(1.0, employee.reporting_culture + 0.2 * intensity * employee.learnability) # Повышаем отзывчивость сотрудника на опасность
            employee.attentiveness = min(1.0, employee.attentiveness + 0.05 * intensity * employee.learnability) #Незначительно повышаем бдительность

        elif training_type == "social_engineering":
            # Тренинг по защите от социальной инженерии
            employee.social_engineering_awareness = min(1.0, employee.social_engineering_awareness + 0.3 * intensity * employee.learnability) # Повышаем осведомленность в соц.инженерии
            employee.attentiveness = min(1.0, employee.attentiveness + 0.15 * intensity * employee.learnability) # Повышаем внимательность
            employee.authority_respect = min(1.0, employee.authority_respect - 0.2 * intensity * employee.learnability) #Уменьшаем уважение к авторитетам, но не меньше 0
            employee.risk_aversion = min(1.0, employee.risk_aversion - 0.1 * intensity * employee.learnability) #Понижаем склонность к риску
        print(f"Тренинг типа '{training_type}' успешно применен к сотруднику {employee.name}")
    else: # Если меньше границы - не усвоили тренинг
        print(f"Тренинг типа '{training_type}' не оказал влияния на сотрудника {employee.name}")


def perform_department_training(department, training_type, intensity):
    """Применяет тренинг указанного типа ко всем сотрудникам отдела."""
    for employee in department.employees:
        apply_training(employee, training_type, intensity)
    return department

