# Task 1
# Список мов
languages = ["Ukrainian", "French", "Bulgarian", "Norwegian", "Latvian"]

# Вивести список до застосування функцій
print("Список до сортування:", languages)

# Використовуємо функцію sorted() 
sorted_languages = sorted(languages)
print("Список після sorted():", sorted_languages)

# Використовуємо функцію reverse()
languages.reverse()
print("Список після reverse():", languages)

# Використовуємо функцію sort() (зміна оригіналу)
languages.sort()
print("Список після sort():", languages)

# Вивести остаточний результат
print("Фінальний список:", languages)


# Task 2
# Читання введеного рядка
input_string = input("Введіть числа через пробіл: ")

# Розділяємо рядок на окремі числа
numbers = map(int, input_string.split())

# Обчислюємо суму чисел
total_sum = sum(numbers)

# Виводимо результат
print(f"Сума чисел: {total_sum}")


# Task 3
# Список міст
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']

# Повідомлення
message = ", ".join(cities[:-1]) + " and " + cities[-1]

# Виводимо результат
print(message)


# Task 4
# Зчитуємо рядок
input_string = input("Введіть 5 цифр, розділених пробілами: ")

# Розділяємо рядок 
digits = input_string.split()

# Створюємо копію списку
reversed_digits = digits[::-1]

# Об'єднуємо елементи списку у одне число
result = "".join(reversed_digits)

# Виводимо результат
print("Число, яке утворюється: ", result)


# Task 5
professions = ["doctor", "engineer", "teacher", "artist", "nurse"]
professions.append("scientist")
professions.remove("teacher")
professions.sort()
professions.reverse()
profession_sorted = sorted(professions)
profession_str = ", ".join(professions)
professions_length = len(professions)
index_of_teacher = professions.index("artist")
count_of_nurse = professions.count("nurse") # скільки раз зустрічається
removed_proffesion = professions.pop(2)
professions.clear()

# Task 6
keywords = ('for', 'if', 'else', 'in', 'is')

def visualize_code_structure(code_lines):
    for line in code_lines:
        indent_level = line.count('    ')
        indent = ' ' * (indent_level * 4)
        print(f"{indent}{line.strip()}")

code_structure = [
    f"{keywords[0]} each token {keywords[3]} the postfix expression :",
    f"    {keywords[1]} the token {keywords[4]} a number :",
    "        print('Convert it to an integer and add it to the end of values')",
    f"    {keywords[2]}",
    "        print('Append the result to the end of values')"
]

visualize_code_structure(code_structure)
