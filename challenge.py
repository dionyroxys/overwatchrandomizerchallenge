import PySimpleGUI as sg
from random import  randint, sample, choice
sg.theme('DarkAmber')
def kills(A, B):
    C = randint(A, B)
    D = randint(A, B)
    while C > D:
            C = randint(A, B)
    E = randint(C, D)
    print(f'you must kill {E} times')
    return E

def player():
        damage = [
            'ashe', 
            'bastion', 
            'casidy', 
            'echo', 
            'gengi', 
            'hanzo', 
            'junkrat',
            'mei',
            'pharah',
            'soldier',
            'sojourn',
            'sombra',
            'symmetra',
            'torbjorn',
            'tracer',
            'widow'
        ]
        support = [
            'ana',
            'baptiste',
            'brigette',
            'kiriko',
            'lucio',
            'mercy',
            'moira',
            'zenyatta'
        ]
        tank = [
            'dva',
            'doomfist',
            'junkerqueen',
            'orisa',
            'ramattra',
            'reinhardt',
            'sigma',
            'winston'
        ]
        # Choose one of the lists at random
        chosen_list = choice([damage, support, tank])
        # Choose three elements from the chosen list
        chosen3 = sample(chosen_list, k=3)
        
        print(f'your chosen 3 heros are {chosen3}')
        return ", ".join(chosen3)

def healamount(A, B):
    C = randint(A, B)
    D = randint(A, B)
    while C > D:
            C = randint(A, B)
    E = randint(C, D)
    print(f'you must heal {E} amount of damage')
    return E
# Define the lists of characters
healamount(5000, 12000)
player()
kills(1, 20)

layout = [
    [sg.Text("Player Choices:", size=(15, 1)), sg.Text("", size=(30, 1), key="-PLAYER-")],
    [sg.Button("roll choices", size=(15, 1), key="-ROLLCHOICES-")],
    [sg.Text("Kill Count:", size=(15, 1)), sg.Text("", size=(10, 1), key="-KILLS-")],
    [sg.Button("roll kill count", size=(15, 1), key="-ROLLKILLS-")],
    [sg.Text("Heal Amount:", size=(15, 1)), sg.Text("", size=(10, 1), key="-HEAL-")],
    [sg.Button("roll heal amount", size=(15, 1), key="-ROLLHEALS-")]
]

# Create the window
window = sg.Window("Randomizer", layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break

    elif event == "-ROLLHEALS-":
        heal_amount = healamount(5000, 12000)
        window["-HEAL-"].update(str(heal_amount))
    elif event == "-ROLLCHOICES-":
        player_choice = player()
        window["-PLAYER-"].update(player_choice)
    elif event == "-ROLLKILLS-":
        kill_count = kills(1, 20)
        window["-KILLS-"].update(str(kill_count))


window.close()