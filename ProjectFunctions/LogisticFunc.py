import math

def logistic_function(z):
  return 1 / (1 + math.exp(-z))

def calculate_attack_success_probability(employee, attack_type, attack_complexity):
    """
    Рассчитывает вероятность успеха атаки на сотрудника с использованием логистической функции.

    Args:
        employee (Employee): Объект класса Employee, представляющий сотрудника.
        attack_type (str): Тип атаки (например, "phishing", "malware", "social_engineering").
        attack_complexity (float): Сложность атаки (от 0.0 до 1.0).

    Returns:
        float: Вероятность успеха атаки (от 0.0 до 1.0). Ближе к 1 - успех атаки, к 0 - провал
    """

    # Базовая вероятность успеха атаки (зависит от типа атаки) - bn коэффициенты
    if attack_type == "phishing":
        b0 = 0.6  # Фишинг
    elif attack_type == "malware":
        b0 = 0.8  # Заражение вредоносным ПО
    elif attack_type == "social_engineering":
        b0 = 0.5  # Зависит от социальной инженерии
    else:
        b0 = 0.3  # Для неизвестных типов атак - более низкая вероятность

    # Коэффициенты, определяющие влияние параметров сотрудника и атаки
    b1 = 1.0   # Влияние внимательности (Attentiveness)
    b2 = 0.8   # Влияние технической грамотности (Technical Literacy)

    b3 = 1.2   # Влияние сложности атаки (Attack Complexity)

    b4 = 0.7   # Влияние осведомленности о социальной инженерии (Social Engineering Awareness)
    b5 = 0.8   # Влияние уважения к авторитетам (Authority Respect)
    b6 = 0.6   # Влияние рабочей нагрузки (Workload)
    b7 = 0.5   # Влияние стрессоустойчивости (Stress Resistance)
    b8 = 0.4   # Влияние склонности следовать инструкциям (Instruction Following)
    b9 = 0.1   # Влияние обучаемости (Learnability) - посредственное влияние (отдельная зависимость)
    b10 = 0.05  # Влияние готовности сообщать об инцидентах (Reporting Culture) - аналогично обучаемости
    b11 = 0.8  # Влияние склонности к риску (Risk Aversion)

    # Линейная комбинация факторов
    z = (b0
         - b1 * employee.attentiveness
         - b2 * employee.technical_literacy
         + b3 * attack_complexity
         - b4 * employee.social_engineering_awareness
         + b5 * employee.authority_respect
         + b6 * employee.workload
         - b7 * employee.stress_resistance
         - b8 * employee.instruction_following
         - b9 * (1 - employee.learnability)
         + b10 * (1 - employee.reporting_culture)
         + b11 * employee.risk_aversion)

    # Расчет логистической функции
    probability = logistic_function(z)
    return probability
