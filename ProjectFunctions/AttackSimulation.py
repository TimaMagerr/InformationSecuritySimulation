import random
from ProjectFunctions.LogisticFunc import calculate_attack_success_probability


def simulate_attack(employee, attack_type, attack_complexity):
    """Симулирует атаку на сотрудника и возвращает результат (успех/неудача)."""
    probability = calculate_attack_success_probability(employee, attack_type, attack_complexity)
    success = random.random() < probability  # Атака успешна, если случайное число меньше вероятности
    return success, probability