import random

print('\tWelcome to NUMBER GUESSING GAME!\n')
print('-------------------------------------------------')
print('INSTRUCTIONS:')
print('1. You can choose the range in which number will be generated.')
print('2. You will get a maximum of 6 tries for this game.')
print('3. If you guess the number, YOU WIN!')
print('4. If you could not guess the number and the tries are finished, YOU LOSE!')
print("GOOD LUCK!!")
print('-------------------------------------------------')

print()
low = int(input('Enter the lower bound of the range: '))
high = int(input('Enter the higher bound of the range: '))
randomNumber = random.randint(low, high)
print()

max_tries = 6
tries = 0

while tries < max_tries:
    tries += 1
    player_guess = int(input(f'Enter your {tries} try: '))
    if player_guess == randomNumber:
        break
    elif player_guess / 1.2 > randomNumber:
        print('Your guess was too high')
    elif player_guess > randomNumber:
        print('Your guess was bit high')
    elif player_guess * 1.2 < randomNumber:
        print('Your guess was too low')
    elif player_guess < randomNumber:
        print('Your guess was bit low')

print()
if player_guess == randomNumber:
    print('You guessed the number right! YOU WON!!')
else:
    print(f'You did not guess the number! YOU LOST!!\nThe number was {randomNumber}')