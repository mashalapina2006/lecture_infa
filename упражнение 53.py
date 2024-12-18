def numeric_to_letter_grade(numeric_grade):
   if numeric_grade < 0 or numeric_grade > 4.0:
        return "Ошибка: оценка должна быть в диапазоне от 0 до 4.0"
    if numeric_grade >= 4.0:
        return "A+"
    elif numeric_grade >= 3.7:
        return "A"
    elif numeric_grade >= 3.3:
        return "A-"
    elif numeric_grade >= 3.0:
        return "B+"
    elif numeric_grade >= 2.7:
        return "B"
    elif numeric_grade >= 2.3:
        return "B-"
    elif numeric_grade >= 2.0:
        return "C+"
    elif numeric_grade >= 1.7:
        return "C"
    elif numeric_grade >= 1.3:
        return "C-"
    elif numeric_grade >= 1.0:
        return "D+"
    elif numeric_grade >= 0.7:
        return "D"
    else:
        return "F"
try:
    user_input = float(input("Введите вашу числовую оценку (от 0 до 4.0): "))
    letter_grade = numeric_to_letter_grade(user_input)
    print(f"Ваша буквенная оценка: {letter_grade}")
except ValueError:
    print("Ошибка: пожалуйста, введите корректное числовое значение.")
