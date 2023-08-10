import random

min = int(input("Enter starting range: "))
max = int(input("Enter ending range: "))

randomNumber = random.randint(min, max)

print('\nYou will get 3 chances to guess the number!')

tries = 3

guess = None

while (tries != 0) and (guess != randomNumber):
    tries-=1
    print('\nGuess a number between', min,'and ', max)
    guess=int(input())
    
    if guess > randomNumber :
        temp = guess * 0.1
        if guess + temp > randomNumber:
            print('Guess is too high!')
        else:
            print('Guess is a bit high!')

    if guess < randomNumber :
        temp = guess * 0.1
        if guess + temp < randomNumber:
            print('Guess is too low!')
        else:
            print('Guess is a bit low!')

if guess == randomNumber:
    print("\nCongratulations! You guessed it right!\n")
else:
    print ("\nSorry you lost.\n")
