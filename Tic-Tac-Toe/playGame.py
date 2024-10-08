from makeBoard import *

def saveGame(player1, player2, turn): # save game as a text file
    while True:
        try:
            fileName = input("Input new file name: ")
            break
        except FileExistsError:
            print("File already exists!")
    
    with open('Saved_Games/'+ fileName + '.txt', 'w') as f:
        f.write(player1+'\n')
        f.write(player2+'\n')
        startNum = [1,4,7]
        for x in range(3):
            f.write('\n.' + '_____' + '.' +'_____' + '.' +'_____' + '.\n')
            for y in range(3):
                print('|' + '  ' + Board[startNum[x]+y], end ='  ', file = f)
            f.write('|')
        f.write('\n.' + '_____' + '.' +'_____' + '.' +'_____' + '.')
        f.write('\n'+str(turn))
    f.close()
    print("Saved successfully!")
    exit()

def winCheck():
    horizontal = [1,4,7] # check if there is a horizontal win
    for x in range(3):
        if Board[horizontal[x]] != ' ':
            if Board[horizontal[x]] == Board[horizontal[x]+1] and Board[horizontal[x]] == Board[horizontal[x]+2]:
                return Board[horizontal[x]]
    
    vertical = [1,2,3] # check if there is a column win
    for x in range(3):
        if Board[vertical[x]] != ' ':
            if Board[vertical[x]] == Board[vertical[x]+3] and Board[vertical[x]] == Board[vertical[x]+6]:
                return Board[vertical[x]]
        
    # check for across right win
    if Board[1] != ' ':
        if Board[1] == Board[5] and Board[1] == Board[9]:
            return Board[1]
        
    # check for across left win
    if Board[7] != ' ':
        if Board[7] == Board[5] and Board[7] == Board[3]:
            return Board[7]
    return None

def tie():
    print("It's a tie!")
    exit()

def gameWin(winner, player1, player2):
    if winner == 'X':
        print(player1 + " has won!")
    else:
        print(player2 + " has won!")
    exit()

def game(player1, player2, turn):
    x = int(turn) # get who's turn it is (from loaded file)
    while x < 9:
        outBoard()
        if winCheck() != None: # if there is a win
            gameWin(winCheck(), player1, player2)
            break
        
        if x % 2 == 0:
            print("It's " + player1 + "'s turn")
            symbol = 'X'
        else:
            print("It's " + player2 + "'s turn")
            symbol = 'O'
        
        while True:
            try:
                print("(Type 10 to save game)")
                pos = int(input("What's your move? "))
                if pos > 10 or pos < 0:
                    print("invalid move")
                elif pos == 10:
                    saveGame(player1, player2, x)
                    break
                elif Board[pos] != ' ':
                    print("Space is already occupied")
                else:
                    break
            except ValueError: # if move is not an int
                print("Invalid move type")
        Board[pos] = symbol
        x = x + 1
    outBoard()
    tie()
