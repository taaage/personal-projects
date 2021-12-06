# Rock, paper, scissors game with classic rules

###############################################

import random


def play():
    user = input("Rock, paper or scissor? ").lower()
    computer =random.choice(['rock', 'paper', 'scissor'])

    if user == computer:
        return "Tie"
    
    # r > s, s > p, p > r

    if is_win(user, computer):
        return "You win"

    return "You lose"

    
def is_win(user, computer):
    
# r > s, s > p, p > r

    if (user == 'rock' and computer == 'scissor') or (user == 'scissor' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
        return True

print(play())




