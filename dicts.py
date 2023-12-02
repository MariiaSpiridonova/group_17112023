students = {
    "Іван Петров": {
        "Пошта": "Ivan@gmail.com",
        "Вік": 14,
        "Номер телефону": "+380987771221",
        "Середній бал": 95.8,
    },
    "Женя Курич": {
        "Пошта": "Geka@gmail.com",
        "Вік": 16,
        "Номер телефону": None,
        "Середній бал": 64.5,
    },
    "Маша Кера": {
        "Пошта": "Masha@gmail.com",
        "Вік": 18,
        "Номер телефону": "+380986671221",
        "Середній бал": 80,
    },
}

students["Вася Калуш"] = {
    "Пошта": "Vasya@gmail.com",
    "Вік": 39,
    "Номер телефону": "+380979876543",
    "Середній бал": 78.9,
}

sum_mark = 0
for student, data in students.items():
    sum_mark += data["Середній бал"]

avg_mark = round(sum_mark / len(students), 1)

students["Іван Петров"]["bank_account_number"] = None

salary_of_selected_student = students["Женя Курич"].get("Зарплата", 0.0)
