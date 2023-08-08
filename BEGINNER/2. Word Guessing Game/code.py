import random

print('\tWord Guessing Game!\nEvery correct letter guessed will give you one extra chance!\nEvery wrong letter guessed will deduct one chance from you!\n\tAll The Best!')
print('----------------------------------------------------')
words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
length = len(word)
tries = int(length / 2)

print('The length of the word is:', length, 'words. So you will get', tries, 'tries!')

char = None
arr = [0] * length

