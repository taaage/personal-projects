# Guessing Game

###############################################


play = input('Welcome to the game. Do you want to play? ')
if play.lower() == 'yes':
    print('Ok lets start with the questions!')
else: 
    print('Ok maybe some other time.')

# Score counter
score = 0

answer = input('What is my favorite sports? ')
if answer.lower() == 'tennis':
    print ('Correct!')
    score += 1
else:
    print('Wrong answer!')

answer = input('What is my favorite food? ')
if answer.lower() == 'pasta':
    print ('Correct!')
    score += 1
else:
    print('Wrong answer!')

answer = input('What is my favorite city? ')
if answer.lower() == 'paris':
    print ('Correct!')
    score += 1
else:
    print('Wrong answer!')

answer = input('What is my favorite animal? ')
if answer.lower() == 'cat':
    print ('Correct!')
    score += 1
else:
    print('Wrong answer!')


print('Thank you for playing, your score is: ' + str(score))
print('You got ' + str(score / 4 * 100) + ' percent correct.')



