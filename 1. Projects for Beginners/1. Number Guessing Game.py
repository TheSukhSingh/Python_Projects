import random
import math

def introScreen():
    print("\n\n================================================================")
    print("Welcome to the Game of Guessing! Today, you will be guessing the number.")
    print("----------------------------------------------------------------")
    print("\nThe Rules are:")
    print("1. You can set the upper and lower bound range.")
    print("2. You will get tries depending on the range you have set.")
    print("3. Don't worry, you will get to know the range in the start.")
    print("4. If you guess the number before losing all your tries, You Win!")
    print("5. But if you could not guess the number even after all your tries are lost")
    print("   You lose!\n")
    print("----------------------------------------------------------------")
    print("\n\t\tAll The Best!!\n")
    print("================================================================")

def getInput():
    highCheck, lowCheck = False, False
    global high, low
    print()
    while lowCheck == False:
        low = input("Enter lower bound: ")
        if low.isdigit() == True:
            lowCheck = True
        else:
            print("The entered value is not a number! Enter a number in the lower bound!")

    while highCheck == False:
        high = input("Enter upper bound: ")
        if high.isdigit() == True:
            highCheck = True
        else:
            print("The entered value is not a number! Enter a number in the upper bound!")
    low, high = int(low), int(high)
    print()

def youWon():
    print("Congratulations! You guessed the number correctly.")
    print("YOU WON!!")
    print()
    exit(0)

def youLost():
    print("You lost all your tries!")
    print("YOU LOST!")
    print()
    exit(0)

def printDistance(number, a):

    if a > number:
        if((number - a)/number)*100 <= 10 and ((number - a)/number)*100 >= -10:
            print("Your guess was a bit high!")
        else:
            print("Your guess was high!")

    elif a < number:
        if((number - a)/number)*100 <= 10 and ((number - a)/number)*100 >= -10:
            print("Your guess was a bit low!")
        else:
            print("Your guess was low!")


introScreen()
getInput()

number = random.randint(low, high)
tries = math.ceil(math.log(high - low + 1, 2))

count = 0

while count < tries:
    count += 1
    print(f"Tries left: {tries - count + 1}")
    a = input("Enter your guess: ")
    if a.isdigit() == False:
        continue
    a = int(a)
    if a == number:
        print()
        youWon()
    if a != number:
        printDistance(number, a)
    print()

print()

if a == number:
    youWon()
    
else:
    youLost()


