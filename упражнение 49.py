zodiac_animals = [
    "Обезьяна",  # 0
    "Петух",     # 1
    "Собака",    # 2
    "Свинья",    # 3
    "Крыса",     # 4
    "Бык",       # 5
    "Тигр",      # 6
    "Кролик",    # 7
    "Дракон",     # 8
    "Змея",      # 9
    "Лошадь",    # 10
    "Коза"       # 11
]
year = int(input("Введите ваш год рождения: "))
index = (year - 2000) % 12
animal = zodiac_animals[index]
print(f"Ваше животное по китайскому гороскопу: {animal}.")
