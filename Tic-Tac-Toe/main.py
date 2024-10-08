from makeBoard import loadBoard
from playGame import game
from os import listdir
from os.path import isfile, join

def loadFile():
    gameFiles = [f for f in listdir('Saved_Games/') if isfile(join('Saved_Games/', f))]
    for number, letter in enumerate(gameFiles): # prints ordered list of files
        print(number, letter)
    while True: # file selection
        try:
            fileNum = int(input("Select the file by typing their number: "))
            if fileNum > len(gameFiles) - 1 or fileNum < len(gameFiles) - 1:
                print("Such file doesn't exist")
            else:
                break
        except ValueError:
            print("Invalid input")
    p1, p2, turn = loadBoard(gameFiles[fileNum])
    game(p1, p2, turn) 


def menu():
    print("1. Play new game\n2. Load a game") # options
    while True: # so while input is invalid
        try:
            choice = int(input("Select choice: "))
            if choice == 1 or choice == 2:
                break # stops loop
            print("Invalid Choice")
        except ValueError: # if choice is not an int
            print("Invalid choice type")
    print('\n')
    if choice == 2:
        loadFile()
    else:
        player1 = input("Player 1 Name: ")
        while True:
            player2 = input("Player 2 Name: ")
            if player2 != player1:
                break
            else:
                print("Please choose a different name")  
    game(player1, player2, 0)

menu()