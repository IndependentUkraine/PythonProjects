# Task 1
glossary = {
    "Функція": "Блок коду, який виконує певну задачу і може бути викликаний у різних частинах програми.",
    "Список": "Змінний тип даних, який зберігає колекцію елементів, що може бути змінена.",
    "Кортеж": "Незмінний тип даних, що зберігає набір елементів у певному порядку.",
    "Цикл": "Конструкція для багаторазового виконання блоку коду до виконання певної умови.",
    "Словник": "Змінний тип даних, що зберігає пари ключ-значення для швидкого доступу до значень за ключами."
}

for term, definition in glossary.items():
    print(f"{term}:\n\t{definition}\n")


# Task 2
rivers = {
    "Amazon": "South America",
    "Nile": "Africa",
    "Yangtze": "Asia"
}

for river, region in rivers.items():
    print(f"The {river} runs through {region}.")


# Task 3
languages = {
    "Python": "Guido van Rossum",
    "JavaScript": "Brendan Eich",
    "Java": "James Gosling",
    "Ruby": "Yukihiro Matsumoto"
}

for language, developer in languages.items():
    print(f"My favorite programming language is {language}. It was created by {developer}.")

del languages["JavaScript"]

print("\nUpdated dictionary:")
print(languages)


# Task 4
e2g = {
    "stork": "storch",
    "hawk": "falke",
    "woodpecker": "specht",
    "owl": "eule"
}

print("English-German Dictionary:", e2g)

print("\nGerman word for 'owl':", e2g["owl"])

e2g["sparrow"] = "spatz"
e2g["eagle"] = "adler"

print("\nUpdated Dictionary:", e2g)

keys_list = list(e2g.keys())
values_list = list(e2g.values())

print("\nKeys:", keys_list)
print("Values:", values_list)


# Task 5
bella = {"type": "dog", "owner": "Alex"}
milo = {"type": "cat", "owner": "Emily"}
charlie = {"type": "parrot", "owner": "Michael"}
luna = {"type": "rabbit", "owner": "Sarah"}

pets = [bella, milo, charlie, luna]

for pet in pets:
    print(f"{pet['owner']} is the owner of a pet - a {pet['type']}.")


# Task 6
morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..'
}

letter = input("Enter a letter: ").upper()

if letter in morse:
    print(f"The Morse code for '{letter}' is {morse[letter]}.")
else:
    print("The entered character is not a valid letter in the Morse code dictionary.")


# Task 7
subjects = {
    'science': {
        'physics': ['nuclear physics', 'optics', 'thermodynamics'],
        'computer science': {},
        'biology': {}
    },
    'humanities': {},
    'public': {}
}

# Виведення ключів для subjects['science']
print("Keys in subjects['science']:", list(subjects['science'].keys()))

# Виведення значень для subjects['science']['physics']
print("Values in subjects['science']['physics']:", subjects['science']['physics'])


# Task 8
cities = {
    'Kyiv': {
        'country': 'Ukraine',
        'population': '2.8 million',
        'fact': 'It is one of the oldest cities in Eastern Europe, with over 1,400 years of history.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '14 million',
        'fact': 'Tokyo is the most populous metropolitan area in the world.'
    },
    'Cairo': {
        'country': 'Egypt',
        'population': '9.5 million',
        'fact': 'Cairo is home to the Great Pyramid of Giza, one of the Seven Wonders of the Ancient World.'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city}")
    print(f" Country: {info['country']}")
    print(f" Population: {info['population']}")
    print(f" Fact: {info['fact']}")


# Task 9
teams = {
    'New York Knicks': [22, 7, 6, 9, 45],
    'Los Angeles Lakers': [24, 15, 0, 9, 55],
    'Chicago Bulls': [20, 10, 2, 8, 50],
    'Boston Celtics': [23, 14, 1, 8, 58]
}

for team, stats in teams.items():
    print(team.upper(), *stats)


# Task 10
things = {
    'key': 3, 
    'mace': 1, 
    'gold coin': 24, 
    'lantern': 1,
    'stone': 10}

print('Equipment:')
for term, definition in things.items():
    print(f"{term} {definition}")
