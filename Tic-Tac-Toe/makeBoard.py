# Board as a dictionary
Board = {1: ' ', 2:' ', 3:' ',
         4:' ', 5: ' ', 6:' ',
         7: ' ', 8: ' ', 9: ' '}

# prevent repitition
def horizDividers():
    print('.' + '_____' + '.' +'_____' + '.' +'_____' + '.')

#prevent repitition
def vertDividers(b, startNum):
    for x in range(3):
        print('|' + '  ' + b[startNum], end ='  ')
        startNum = startNum + 1
    print('|')

# prints the board
def outBoard():
    list = [1, 4, 7]
    for x in range(3):
        horizDividers()
        vertDividers(Board, list[x])
    horizDividers()

def loadBoard(file):
    with open('Saved_Games/'+file, 'r') as f:
        content = f.readlines()
        player1 = content[0]
        player2 = content[1]
        turn = content[10] # get who's current turn it was

        lines = [4,6,8] # contains the index of the rows that could contain X or O
        columns = [3,9,15] # columns of the rows that could contain X or O
        boardKey = 1 # current key in Board
        for x in range(3):
            for y in range(3):
                if content[lines[x]][columns[y]] == 'X' or content[lines[x]][columns[y]] == 'O':
                    Board[boardKey] = content[lines[x]][columns[y]]
                boardKey = boardKey + 1
    f.close()
    return player1, player2, turn