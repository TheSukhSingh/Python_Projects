import random

def starting():
    print("====================================================================")
    print("\tWelcome to Word Guessing Game!")
    print("--------------------------------------------------------------------")
    print("RULES:")
    print("1. Guess the word right to win.")
    print("2. If you guess it wrong, it will cost you a life.")
    print("3. If you guess it right, you won't be charged.")
    print("4. You have 12 tries.")
    print("--------------------------------------------------------------------")
    print("\t\tGOOD LUCK!")
    print("====================================================================")

def printGuessed(word, guesses):
    for i in word:
        if i in guesses:
            print(i, end=" ")
        else:
            print("_", end=" ")
    print()

def checkGuess(word, guess, guesses):
    if guess in word:
        if guess in guesses:
            return 0, "Already Guessed! Try Again!"
        else:
            return 1, "You guessed this correctly!"
    else:
        return 0, "Wrong Guess! Try again!"

def gameWon():
    print("You guessed the word correctly!")
    print("YOU WON!")

def gameLost(word):
    print(f"You could not guess the word! The word was {word}")
    print("YOU LOSE!")


words = '''rainbow computer science programming python mathematics player condition reverse water board geeks drink food mouse keyboard normal good luck'''
words = words.split(" ")

word = random.choice(words)

starting()

guesses = ''
isGuessed = False
tries = 12

while isGuessed == False and tries > 0:
    tries -= 1
    printGuessed(word, guesses)
    print(f"Lives left: {tries + 1}")
    guess = input("Enter your guess (Only one character): ")
    if len(guess) != 1:
        print("Invalid input!")
        continue
    print()
    a, b = checkGuess(word, guess, guesses)
    if a == 1:
        tries += 1
    print(b)
    guesses += guess

    isGuessed = True

    for i in word:
        if i not in guesses:
            isGuessed = False
    print()

if tries == 0:
    gameLost(word)
    exit(0)

elif isGuessed == True:
    gameWon()
    exit(0)