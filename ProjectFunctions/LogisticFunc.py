import math

def logistic_function(z):
  return 1 / (1 + math.exp(-z))

def calculate_attack_success_probability(employee, attack_type, attack_complexity):
    b0 = 0.5  # Базовая вероятность успеха атаки
    b1 = 1.0  # Влияние внимательности
    b2 = 0.8  # Влияние технической грамотности
    b3 = 1.2  # Влияние сложности атаки
    b4 = 0.7  # Влияние осведомленности о социальной инженерии
    b5 = 0.9  # Влияние уважения к авторитетам (чем выше, тем хуже)
    b6 = 0.6  # Влияние рабочей нагрузки

    z = (b0 - b1 * employee.attentiveness - b2 * employee.technical_literacy +
         b3 * attack_complexity - b4 * employee.social_engineering_awareness +
         b5 * employee.authority_respect + b6 * employee.workload)

    probability = logistic_function(z)
    return probability