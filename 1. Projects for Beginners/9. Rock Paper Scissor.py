import random

game_elements = '''rock paper scissors'''
game_elements = game_elements.split(" ")

def taking_human_input():
    human_turn = int(input('Enter your choice: 1. Rock 2. Paper 3. Scissors\n'))
    return human_turn

def final_text(pc_input, human_input):
    if pc_input.lower() == 'rock':
        if human_input.lower() == 'rock':
            print(f'You both chose {pc_input}. Try Again!')
            return False
        elif human_input.lower() == 'paper':
            print(f'PC: {pc_input}, You: {human_input}\nYou Won!')
            return True
        elif human_input.lower() == 'scissors':
            print(f'PC: {pc_input}, You: {human_input}\nYou Lost!')
            return True
    elif pc_input.lower() == 'paper':
        if human_input.lower() == 'paper':
            print(f'You both chose {pc_input}. Try Again!')
            return False
        elif human_input.lower() == 'scissors':
            print(f'PC: {pc_input}, You: {human_input}\nYou Won!')
            return True
        elif human_input.lower() == 'rock':
            print(f'PC: {pc_input}, You: {human_input}\nYou Lost!')
            return True
    elif pc_input.lower() == 'scissors':
        if human_input.lower() == 'scissors':
            print(f'You both chose {pc_input}. Try Again!')
            return False
        elif human_input.lower() == 'rock':
            print(f'PC: {pc_input}, You: {human_input}\nYou Won!')
            return True
        elif human_input.lower() == 'paper':
            print(f'PC: {pc_input}, You: {human_input}\nYou Lost!')
            return True

def playing():
    pc_turn = random.choice(game_elements)
    human_turn = taking_human_input()
    human_turn_text = ''
    if human_turn == 1:
        human_turn_text = 'rock'
    elif human_turn == 2:
        human_turn_text = 'paper'
    elif human_turn == 3:
        human_turn_text = 'scissors'
    else:
        print('Wrong input! Bye!')
        exit()
    game_over = final_text(pc_turn, human_turn_text)
    return game_over
    

print("---------------------------------------------")
print('    Welcome to Rock Scissors Paper Game!')
print("---------------------------------------------")
print('Instructions: ')
print('1. Rock beats scissors')
print('2. Scissors beat paper')
print('3. Paper beats rock')
print("---------------------------------------------")

print()

continue_playing = True

while continue_playing:
    is_game_over = playing()
    print()
    while is_game_over == False:
        playing()
    wanna_play = input('Do you want to play another game? (Y/n): ')
    if wanna_play.lower() == 'y':
        continue_playing = True
    elif wanna_play.lower() == 'n':
        continue_playing = False
    else:
        print('Wrong input!')
        continue_playing = False

print('Thanks for playing!')