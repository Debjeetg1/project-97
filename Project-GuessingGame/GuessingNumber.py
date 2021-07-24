import random

randomNumber = random.randint(1, 10)
chances = 5
print('Number Guessing Game')
print()

print('Enter a number between 1 to 9')

playerInput = int(input(': '))


while chances > 1:

    if playerInput != randomNumber:
        if playerInput > randomNumber:
            print('Your Guess was too high, guess a number below ', playerInput)
            playerInput = int(input('please enter again: '))
        elif playerInput < randomNumber:
            print('Your Guess was too low, guess a number higher ', playerInput)
            playerInput = int(input('please enter again: '))
    elif playerInput == randomNumber:
        print('You have won!!')
        break
    chances -= 1
            
if chances == 0:
    print('You have lost')
    print('The number was: ' , randomNumber)
