class Employee:
    def __init__(self, name, department, age, experience, attentiveness, technical_literacy, stress_resistance, instruction_following, learnability,
                 social_engineering_awareness, reporting_culture, authority_respect, workload, risk_aversion):
        """
        Конструктор класса Employee (Сотрудник).

        Args:
            name (str): Имя сотрудника.
            department (str): Отдел, в котором работает сотрудник.
            age (int): Возраст сотрудника.
            experience (int): Стаж работы сотрудника в годах.

            "Ниже приведенные параметры имеют вариацию значений от 0.0 до 1.0."
            attentiveness (float): Внимательность сотрудника (вероятность заметить опасность)
            technical_literacy (float): Техническая грамотность сотрудника (понимание основ ИБ)
            stress_resistance (float): Стрессоустойчивость сотрудника (способность сохранять спокойствие в стрессовых ситуациях)
            instruction_following (float): Склонность сотрудника следовать инструкциям и правилам
            learnability (float): Обучаемость сотрудника (скорость обучения новым навыкам)
            social_engineering_awareness (float): Осведомленность сотрудника о методах социальной инженерии
            reporting_culture (float): Готовность сотрудника сообщать об инцидентах безопасности
            authority_respect (float): Наивная вера в авторитетное мнение (склонность СЛЕПО подчиняться указаниям, - чем выше, тем хуже (под соц инженерию)).
            workload (float): Рабочая нагрузка сотрудника (уровень загруженности работой)
            risk_aversion (float): Склонность сотрудника к риску (чем выше, тем больше склонен к рискованному поведению)
        """
        self.name = name
        self.department = department
        self.age = age
        self.experience = experience
        self.attentiveness = attentiveness
        self.technical_literacy = technical_literacy
        self.stress_resistance = stress_resistance
        self.instruction_following = instruction_following
        self.learnability = learnability
        self.social_engineering_awareness = social_engineering_awareness
        self.reporting_culture = reporting_culture
        self.authority_respect = authority_respect
        self.workload = workload
        self.risk_aversion = risk_aversion
        self.attack_stats = {
            "phishing": {"success_count": 0, "total_attacks": 0},
            "malware": {"success_count": 0, "total_attacks": 0},
            "social_engineering": {"success_count": 0, "total_attacks": 0} }

    def __str__(self):
        """
        Метод для строкового представления объекта Employee (для удобного вывода информации).

        Returns:
            str: Строковое представление объекта Employee.
        """
        return (f"Name: {self.name}, Department: {self.department}, Age: {self.age}, Experience: {self.experience}, "
                f"Attentiveness: {self.attentiveness:.2f}, Technical Literacy: {self.technical_literacy:.2f}, "
                f"Stress Resistance: {self.stress_resistance:.2f}, Instruction Following: {self.instruction_following:.2f}, "
                f"Learnability: {self.learnability:.2f}, Social Engineering Awareness: {self.social_engineering_awareness:.2f}, "
                f"Reporting Culture: {self.reporting_culture:.2f}, Authority Respect: {self.authority_respect:.2f}, "
                f"Workload: {self.workload:.2f}, Risk Aversion: {self.risk_aversion:.2f}")