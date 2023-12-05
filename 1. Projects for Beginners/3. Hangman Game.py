import random 
  
someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split(' ')

word = random.choice(someWords)

def printing(word, guesses):
    for i in word:
        if i in guesses:
            print(i, end = "")
        else:
            print("-", end = "")

def checkGuess(word, guess, guesses, tries):
    if guess in word:
        if guess in guesses:
            print("Already Guessed!!")
            tries += 1
        else:
            print("You guessed that correctly!!")
    else:
        print("Wrong Guess!!")
        tries += 1
    return tries
        

print("===========================================================")
print("                    HANGMAN GAME")
print("This is a game of Hangman. Find your answer and win prizes")
print("1. Guess the name of fruit")
print("2. You will get 5 chances!")
print("3. If you guessed the letter correct, you will get another chance!")
print("4. If you guess wrong, chance will be deducted.")
print("5. Find the word and win!")
print("                    BEST OF LUCK")
print("===========================================================")

guesses = ""
guess = ""

unguessed = 1
tries = 0

while unguessed != 0 and tries < 5:
    print('Tries: ', tries)
    unguessed = 0
    printing(word, guesses)
    print()
    guess = input("Enter your guess: ")
    tries = checkGuess(word, guess, guesses, tries)
    guesses += guess
    for i in word:
        if i not in guesses:
            unguessed += 1
    print('Unguessed: ', unguessed)
    print('_______________________')

if unguessed > 0:
    print("You lost!!")
else:
    print("You won!!")



















