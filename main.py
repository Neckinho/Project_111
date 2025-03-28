
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Radek Neckař
email: radekneckar@seznam.cz
"""

import random
import time

line = "-" * 48
print(f"Hi there!\n{line}\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.\n{line}")

# vygenerování čísla bez 0 a každé jiné
while True:
    random_number = random.sample(range(0, 10), 4)
    if random_number[0] != 0:
        break

#print(random_number)  # odkomentuj pro testování

attempts = 0
first_input = True

#  čas
start_time = time.time()  

#smyčka pro hádání 
while True:
    if first_input:
        player_input = input("Enter a number: ")
        print(line)
        first_input = False
    else:
        player_input = input(">>>")

    if not player_input.isdigit() or len(player_input) != 4:
        print("You did not enter 4 numbers.")
        print(line)
        continue
    elif len(set(player_input)) != 4:
        print("Numbers must not repeat.")
        print(line)
        continue
    elif player_input[0] == '0':
        print("The first number cannot be zero.")
        print(line)
        continue

    player_number = [int(digit) for digit in player_input]
    attempts += 1

# Uhodnutí
    if player_number == random_number:
        end_time = time.time()
        duration = end_time - start_time
        minutes = int(duration // 60)
        seconds = int(duration % 60)
        print(f"Correct, you've guessed the right number\nin {attempts} guesses!\nin {minutes} min {seconds} seconds.")
        break


    bulls = 0
    cows = 0
    for i in range(4):
        if player_number[i] == random_number[i]:
            bulls += 1
        elif player_number[i] in random_number:
            cows += 1

    print(f"{bulls} bulls, {cows} cows")
    print(line)
