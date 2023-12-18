import random

def pcNum(pcInput):
    if pcInput == "Paper":
        pcInput = 2
    elif pcInput == "Scissors":
        pcInput = 3
    elif pcInput == "Rock":
        pcInput = 1
    return pcInput

def whoWon(userInput, pcInput):
    if pcInput == userInput:
        return "It's a draw!"
    elif pcInput - userInput == 1 or pcInput - userInput == -2:
        return "YOU WON!!"
    elif pcInput - userInput == -1 or pcInput - userInput == 2:
        return "YOU LOSE!!"

def printChoices(userInput, pcInput):
    choices = ["Rock", "Paper", "Scissors"]
    print(f"You chose {choices[userInput - 1]}, PC chose {choices[pcInput - 1]}")

def main():
    gameOptions = ["Paper", "Scissors", "Rock"]

    print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
        + "Rock vs Paper -> Paper wins \n"
        + "Rock vs Scissors -> Rock wins \n"
        + "Paper vs Scissors -> Scissor wins \n")

    while True:
        userInput = input("Enter your choice\n1. Rock\n2. Paper\n3. Scissors\n")
        if userInput.isdigit() == False:
            print("Invalid Input!")
            continue
        userInput = int(userInput)
        if userInput > 3 or userInput < 1:
            print("Invalid Input!")
            continue
        pcInput = random.choice(gameOptions)
        pcInput = pcNum(pcInput)
        printChoices(userInput, pcInput)
        result = whoWon(pcInput, userInput)
        print()
        print(result)
        wannaPlay = input("Do you want to play again? (Y/n) ")
        if wannaPlay.lower() == "y":
            continue
        else:
            break

    print("\n\nThanks for playing!!")


if __name__ == "__main__":
    main()
