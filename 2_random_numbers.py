# Guessing game based on random number generation

#################################################


import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a random number between 1 and {x}: "))
       
        if random_number < guess:
            print("Guess too high, guess again.")
        elif random_number > guess:
            print("Guess too low, guess again.")

    print (f"Guess correct, {random_number} is the correct number!")

guess(10)

       

