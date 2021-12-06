# Guessing game based on random number generation

#################################################


import random

def computer_guessing(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = guess = low

        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)?").lower()
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess +1

    print(f"Yay, the computer guessed your number {guess} correctly!")


computer_guessing(10000)

