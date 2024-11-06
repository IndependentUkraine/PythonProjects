# Task 1
message = "First message"
print(message)

message = "Second"
print(message)

# Task 2
user_name = "Denys"

print(f"Hello, {user_name}, would you like to learn some Python today?")

# Task 3
famous_person = "Albert Einstein"

message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'

print(message)

# Task 4
user_name = "\t Denys \n"

print(user_name)
print(user_name.lstrip())
print(user_name.rstrip())
print(user_name.strip())

# Task 5
print("Денис Ільків")        
print("Україна")               
print("01001")                 
print("Львів")                  
print("вул. Городоцька")        
print("буд. 10, кв. 5")

# Task 6
# Запитуємо значення дистанції
distance_meters = float(input("Введіть дистанцію в метрах: "))

# Конвертуємо метри в інші одиниці вимірювання
distance_inches = distance_meters * 39.3701
distance_feet = distance_meters * 3.28084
distance_miles = distance_meters * 0.000621371
distance_yards = distance_meters * 1.09361

# Виводимо результат з форматуванням до двох знаків після крапки
print("Відстань у дюймах: {}".format(format(distance_inches, ".2f")))
print("Відстань у футах: {}".format(format(distance_feet, ".2f")))
print("Відстань у милях: {}".format(format(distance_miles, ".2f")))
print("Відстань у ярдах: {}".format(format(distance_yards, ".2f")))

# Task 7
duration_days = int(input("Введіть тривалість події: "))

duration_hours = duration_days * 24
duration_minutes = duration_hours * 60
duration_seconds = duration_minutes * 60

print("{:<10} {:<10}".format("Години:", duration_hours))
print("{:<10} {:<10}".format("Хвилини:", duration_minutes))
print("{:<10} {:<10}".format("Секунди:", duration_seconds))

# Task 8
temperature_celsius = float(input("Введіть значення температури: "))

temperature_fahrenheit = 32 + (9 / 5) * temperature_celsius
temperature_kelvin = temperature_celsius + 273.15

print("{:^15}".format("Температура"))
print("{:^15} {:^15}".format("Цельсій", format(temperature_celsius, ".2f")))
print("{:^15} {:^15}".format("Фаренгейт", format(temperature_fahrenheit, ".2f")))
print("{:^15} {:^15}".format("Кельвін", format(temperature_kelvin, ".2f")))

# Task 9
# Запитуємо число
number = int(input("Введіть чотирьохзначне число: "))

# Отримуємо окремі цифри числа
thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10

# Обчислюємо суму цифр
sum_digits = thousands + hundreds + tens + ones

# Виводимо результат у форматованому вигляді990
print(f"{thousands} + {hundreds} + {tens} + {ones} = {sum_digits}")

# Task 10
import math

x1 = 39.9075000
y1 = 116.3972300

x2 = 50.4546600
y2 = 30.5238000

x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

radius_of_earth = 6371.032
distance = radius_of_earth * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

print("{:>10} {:>10} {:>10}".format("Відстань", "км", format(distance, ".3f")))

# Task 11, Changes in tasks 6 - 9 are done.

# Task 12, Comments are added in tasks 6 and 9


