import random
import time

num = random.randrange(1000,10000)

print('Welcome to the Mastermind game!\nThere is a number between 1000 and 10000, if you choose the number correctly within first five tries, you will be crowned as a mastermind!')
print('Choosing number...')
time.sleep(0.5)
print('Number is chosen!')
tries = 5
while True:
    number = ['x', 'x', 'x', 'x']
    guess_number=int(input("Enter your guess: "))
    tries -= 1
    unrealnr = guess_number
    realnr = num
    if (guess_number == realnr):
        print('Wow! You found the number in the first try!\n You are the MASTERMIND!')
        exit(0)
    correct_count = 0
    index = 3
    while realnr != 0:
        if realnr % 10 == unrealnr % 10:
            correct_count += 1
            number[index] = realnr % 10
        index -= 1
        realnr //= 10
        unrealnr //=10
    if correct_count == 4:
        print('Congratulations!! You found the number', *number, '. You are the MASTERMIND.')
        exit(0)
    elif correct_count > 0 and correct_count < 4:
        print('Not quite the number. But you found some digits: ', *number)
    else:
        print('You did not find any digits. Try again')

    if tries == 0:
        print('Out of tries! You lose!\nThe real number was',num)
        exit(0)