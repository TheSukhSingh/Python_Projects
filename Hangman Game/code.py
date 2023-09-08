import random

def printword(word, guess):
    
    print()

someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split(' ')

word = random.choice(someWords)

print('This is a Game. Guess the word and win prizes')
leng = len(word)
tries = leng + 2
print(f'This is {leng} letter word! So you get {tries} tries!')
guess = ''

while tries:
    tries -= 1
    printword(word, guess)

