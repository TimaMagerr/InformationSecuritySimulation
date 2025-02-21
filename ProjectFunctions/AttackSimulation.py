import random

from ProjectFunctions.LogisticFunc import calculate_attack_success_probability



def simulate_attack(employee, attack_type, attack_complexity):
    """Симулирует атаку на сотрудника и возвращает результат (успех/неудача)."""
    probability = calculate_attack_success_probability(employee, attack_type, attack_complexity) # Рассчитываем вероятность успеха атаки
    success = random.random() < probability
    return success, probability

def perform_department_attack_simulation(department, attack_type, num_attacks):
    """Симулирует несколько атак на отдел и обновляет статистику для *каждого сотрудника*."""
    for employee in department.employees:
        success_count = 0

        for _ in range(num_attacks):
            # Повыбирать различную сложность атаки
            attack_complexity = random.random()
            success, _ = simulate_attack(employee, attack_type, attack_complexity)

            if success:
                success_count += 1

        # Обновляем статистику сотрудника
        employee.attack_stats[attack_type]["total_attacks"] += num_attacks
        employee.attack_stats[attack_type]["success_count"] += success_count
    print(f"Атака типа '{attack_type}' успешно проведена на отдел")

    return department

