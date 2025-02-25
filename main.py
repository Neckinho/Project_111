#projekt_1.py: první projekt do Engeto Online Python Akademie

#author: Radek Neckař
#email: radekneckar@seznam.cz


import string

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

acces = [
    {"bob", "123"},
    {"ann", "pass123"},
    {"mike", "password13"},
    {"liz", "pass123"}
]

line = "-" * 41
name = input("username: ")
last_name = input("password: ")
print(line)
user = {name, last_name}

if user in acces:
    print(f"Welcome to the app, {name} \nWe have 3 texts to be analyzed.")
    text_number = input("Enter a number btw. 1 and 3 to select: ")
     
    if text_number.isdigit():
        text_number = int(text_number)
        if 1 <= text_number <= 3:
            text = TEXTS[text_number - 1]
            
            # Rozdělení slov
            raw_words = text.split()
            
            # Odstranění interpunkcí
            words = []
            for w in raw_words:
                # běžná interpunkce
                cleaned_word = w.strip(string.punctuation)
                # přidání slov (neprázdných)
                if cleaned_word:
                    words.append(cleaned_word)

            count_words = len(words)
            titlecase_words = sum(1 for word in words if word.istitle())
            uppercase_words = sum(1 for word in words if word.isupper())
            lowercase_words = sum(1 for word in words if word.islower())
            isnumeric = sum(1 for word in words if word.isnumeric())
            numeric_sum = sum(int(word) for word in words if word.isnumeric())

            print(line)
            print(f"There are {count_words} words in the selected text.")
            print(f"There are {titlecase_words} titlecase words.")
            print(f"There are {uppercase_words} uppercase words.")
            print(f"There are {lowercase_words} lowercase words.")
            print(f"There are {isnumeric} numeric strings.")
            print(f"The sum of all the numbers {numeric_sum}")

            # Slovník pro délky slov
            word_lengths = {}
            for word in words:
                length = len(word)
                word_lengths[length] = word_lengths.get(length, 0) + 1

            print(line)
            print(f"{'LEN':<3} | {'OCCURENCES':<12} | {'NR.':<3}")
            print(line)

            # Seřazení podle délky
            for length in sorted(word_lengths):
                count = word_lengths[length]
                stars = "*" * count
                print(f"{length:<3} | {stars:<12} | {count:<3}")

        else:
            print("Invalid selection. Please enter a number between 1 and 3.")
    else:
        print("Invalid input. Please enter a number.")
else:
    print("Unregistered user, terminating the program.")
