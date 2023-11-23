import random

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']
word_to_guess = random.choice(words)

print('-----------------------------------------------------')
print('This is a WORD GUESSING GAME!!')
print('-----------------------------------------------------')
print('INSTRUCTIONS:')
print('1. You will get 12 tries. If you guess the word right, you will win the game.')
print('2. Else you will lose.')
print('3. If there are more than one repitions of the same letter, you have to write that only once.')
print('All the best!!')
print('-----------------------------------------------------')

max_tries = 12
guesses = ''

tries = 0
not_guessed = 1

while tries < max_tries and not_guessed != 0:
    for i in word_to_guess:
        if i in guesses:
            print(i, end=" ")
        else:
            print('_', end=" ")
    print()
    print(f'You have {max_tries - tries} tries left!')
    guess = input('Enter your guess: ')
    if len(guess) > 1:
        print('Too many letters! Try Again!')
        continue 
    if guess not in word_to_guess:
        tries+= 1
        print('Wrong Guess!')
    elif guess in word_to_guess:
        if guess in guesses:
            print('You guessed this letter already!')
            tries += 1
        else:
            print('You guessed the word correctly!')
    guesses += guess
    not_guessed = 0
    for i in word_to_guess:
        if i not in guesses:
            not_guessed += 1

if not_guessed == 0:
    print('YOU WON!!')
    print(f'You guessed the right word! ({word_to_guess})')
else:
    print(f'The correct word was: {word_to_guess}')
    print('Better Luck Next Time!')


