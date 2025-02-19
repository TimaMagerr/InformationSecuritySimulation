import random

from ProjectFunctions.LogisticFunc import calculate_attack_success_probability



def simulate_attack(employee, attack_type, attack_complexity):
    """Симулирует атаку на сотрудника и возвращает результат (успех/неудача)."""
    probability = calculate_attack_success_probability(employee, attack_type, attack_complexity) # Рассчитываем вероятность успеха атаки
    success = probability > 0.55  # Атака успешна, если ее вероятность больше 0.5
    return success, probability

def perform_department_attack_simulation(department, attack_type, num_attacks):
    """Симулирует несколько атак на отдел и обновляет статистику."""
    total_success_probability = 0
    success_count = 0

    for employee in department.employees:
        for _ in range(num_attacks):
            attack_complexity = random.random()
            success, probability = simulate_attack(employee, attack_type, attack_complexity)

            total_success_probability += probability
            if success:
                success_count += 1

    # Обновляем статистику отдела
    total_attacks = num_attacks * len(department.employees)
    success_probability = total_success_probability / total_attacks if total_attacks > 0 else 0

    department.attack_stats = {
        "phishing": {"success_probability": 0, "success_count": 0, "total_attacks": 0},
        "malware": {"success_probability": 0, "success_count": 0, "total_attacks": 0},
        "social_engineering": {"success_probability": 0, "success_count": 0, "total_attacks": 0}
    }

    department.attack_stats[attack_type]["total_attacks"] = total_attacks
    department.attack_stats[attack_type]["success_count"] = success_count
    department.attack_stats[attack_type]["success_probability"] = success_probability

    return department  #Возвращаем department с обновленной статистикой

