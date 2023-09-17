import random

fruits = '''muskmelon watermelon apple banana guava lemon strawberry papaya mango orange grape peach berry'''
fruits = fruits.split(' ')

fruit = random.choice(fruits)

length = len(fruit)
tries = length + 2
print(f'Welcome to Hangman Game.\nThe word is {length} letters long, and you get {tries} tries.')

guessed = ''
while tries:
    chk = 0
    for word in fruit:
        if word in guessed:
            print(f'{word}', end = " ")
        else:
            print('-', end = " ")
            chk += 1
    print(f'\n{chk}')
    if chk == 0:
        break
    else:
        pass
    guess = input('\nEnter your guess: ')
    guessed += guess
    if guess in fruit:
        print('Correct Guess')
    else:
        tries -= 1
        print(f'Wrong guess\nYou have {tries} tries')
    
if chk > 0:
    print(f'You lost! The word was: {fruit}')
else:
    print(f'You won! The word was {fruit}')

