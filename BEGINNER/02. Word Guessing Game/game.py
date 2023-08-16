import random

words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print('Welcome to Word Guessing Game\nGuess the word')

guesses = ''

turns = 26

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed += 1
        
    if failed == 0:
        print('\nYou win!!')
        break    

    guess = input('Enter guess: ')
    guesses += guess
    if guess not in word:
        turns-=1
        if turns == 0:
            print('You lose!')
