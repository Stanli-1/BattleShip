# REFERENCE:
#   https://www.chegg.com/homework-help/questions-and-answers/instructions-assignment-need-place-player-s-ships-board-many-functions-want-use-highly-rec-q41858600


import random

# Global Variables
ship_lengths = [5,4,3,3,2]
ship_names = ['aircraft carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
ship_codings = ['a', 'b', 'c', 's', 'd']

def board(level):
    # --- construct initial board
    period_str = '.'
    asterisk_str = '*'
    game_board = []
    board_size = 10 + (level - 1) * 2   # 8 + level * 2

    # creating a two-dimentional list
    for n in range (1, board_size + 1):
        # creating a row in the table
        row = []
        for k in range (1, board_size + 1):
            if n < board_size // 2 + 1:
                row.append(period_str)
            else:
                row.append(asterisk_str)
        # appending each row to the game_board 
        game_board.append(row)
        
    return(game_board)
    
def displayBoard(game_board):
    # ---- display a board
    board_size = len(game_board)
    
    print('\nGame Board ...\n')
    print(format(' ', '<3'), end='')

    # printing the letters for the columns' header
    for inc in range(0, board_size):
        print(format(chr(ord('A') + inc), '^3'), end='')
    print('\n')

    # printing the actual board using a nested loops
    for row in range(0, board_size):
        print(format(row + 1, '<3'), end='')

        for col in range(0, board_size):
            print(format(game_board[row][col], '^3'), end='')   

        # label each side of game board
        if row == 2:
            print(format(' ', '<6'), "PLAYER'S SHIPS", end='')
        elif row == board_size // 2 + 2:
            print(format(' ', '<6'), "COMPUTER'S SHIPS", end='')

        # display blank line between player's and computer's sides of board
        if row == board_size // 2 - 1:
            print('\n')
        else:
            print()
    print()

def colHeading(gameboard):
    boardSize = len(gameboard)
    colHeading = []
    for i in range(boardSize):
        colHeading.append(chr(65+i))
    return colHeading

def verticalCollision(col, startRow, endRow, game_board):
    collision_found = False
    for row in range(startRow, endRow+1):                
        if game_board[row][col] not in ['.', '*']:
            collision_found = True
    return collision_found

def horizontalCollision(row, startCol, endCol, game_board):
    # check for collisions
    collision_found = False
    for col in range(startCol, endCol+1):                
        if game_board[row][col] not in ['.', '*']:
            collision_found = True
    return collision_found

# i index # to access values in the ship_lengths, ship_names, ship_codings
# start and end are userInput after the split
def validate(i, start, end, game_board):    
    # get the column headings as a list
    heading = colHeading(game_board)
    
    # validate you have numbers before converting them to int
    # validate ship is in column range
    size = len(game_board)
    try:
        int(start[1:])
        int(end[1:])
        col = heading.index(start[0])
        col = heading.index(end[0])
    except:
        print('Either row or column numbers are out of range')
        print('-'*60,'\nTry again...')
        return True
        
    # validate ship in upper half
    if not ((0 < int(start[1:]) <= size//2) and (0 < int(end[1:]) <= size//2)):
        print('Trying to place your ship on the computer section')
        print('-'*60,'\nTry again...')
        return True

    invalidInput = False    
    if start[0]==end[0]: # vertical
        col = heading.index(start[0])
        startRow = min(int(start[1:])-1, int(end[1:])-1)
        endRow = max(int(start[1:])-1, int(end[1:])-1)
        collision_found = verticalCollision(col, startRow, endRow , game_board)
        user_shipsize = endRow - startRow + 1

    elif start[1:]==end[1:]: # horizontal
        # figuring out the row number
        startCol = min(heading.index(start[0]), heading.index(end[0]))
        endCol = max(heading.index(start[0]), heading.index(end[0]))
        row = int(start[1:])-1
        collision_found = horizontalCollision(row, startCol, endCol, game_board)
        user_shipsize = endCol - startCol + 1

    # checking for anything other than vertical or horizontal     
    else:
        invalidInput = True
        print('You can only place your ships vertically or horizontally')
        collision_found = False
    
    if collision_found:
        print('Collision has been detected')
        print('-'*60,'\nTry again...')
        return True
        
    # validate the size of the ship
    if not invalidInput and user_shipsize != ship_lengths[i]:
        print('The size of the ship does not match the given size')
        print('-'*60,'\nTry again...')
        return True

    return False


def openToReadShipInfo():
    shipInfo = open('shipInfo.txt', 'r')
    ships = []
    for ship in shipInfo:
        ships.append(ship)
    shipInfo.close()
    return ships
        
# you only need to complete the following function (playerShipPosition)
def playerShipPosition(game_board):    
    print('Enter location of each of specified size (e.g. A1:A5)')    
    # get an input
    size = len(game_board)   

    # get the column headings as a list
    heading = colHeading(game_board)
    
    for i in range(len(ship_lengths)):
        mesg = ship_names[i] + '(' + str(ship_lengths[i]) + '): ' 
        
        tryAgain = True
        while tryAgain:
            userInput = input(mesg)
            # check for : in user input and
            # the # of input characters 
            if ":" in userInput and (5 <= len(userInput) < 8):
                start, end = userInput.split(':')

                # converting the letters to upper in case input is lower case letters
                start = start[0].upper() + start[1:]
                end = end[0].upper() + end[1:]
                tryAgain = validate(i, start, end, game_board)
            else:
                print('Invalide input - either : is missing or invalid # of chars')
                print('-'*60,'\nTry again...')

        # input is validated and it is safe to put the ship on the board
        # place ship on board
        if start[0]==end[0]: # vertical            
            startRow = min(int(start[1:])-1, int(end[1:])-1)
            endRow = max(int(start[1:])-1, int(end[1:])-1)
            col = heading.index(start[0])
            for row in range(startRow, endRow+1):                
                game_board[row][col] = ship_codings[i]        
            
        elif start[1:]==end[1:]: # horizontal
            # place ship on board    
            startCol = min(heading.index(start[0]), heading.index(end[0]))
            endCol = max(heading.index(start[0]), heading.index(end[0]))
            row = int(start[1:])-1
            for col in range(startCol, endCol+1):                
                game_board[row][col] = ship_codings[i]

        # this following line is only for testing, you don't need to display the
        # board after placing each ship. The displayBoard will be called
        # after all the ships have been placed on the board in the main function. 
        #displayBoard(game_board)
        

def computerShipPosition(game_board):
    # --- randomly position computer's ships
    for current_ship in range(len(ship_names)):
        # get length of current ship
        length = ship_lengths[current_ship]
                    
        # place horizontially or vertically based on even/odd random number
        if random.randint(1,10) % 2 == 0:
            
            # position horizontally
            placed_without_collision = False
            
            while not placed_without_collision:
                # generate random ship location,(row, col),within bottom half
                # of board for horizontal placement, accounting for its length
                loc = (random.randint(len(game_board) // 2, len(game_board) - 1),
                       random.randint(0, len(game_board) - length))
                # check for collisions
                collision_found = False
                col_incr = 0
                while col_incr < ship_lengths[current_ship] and \
                      not collision_found:
                    if game_board[loc[0]][loc[1] + col_incr] != '*':
                        collision_found = True
                    else:
                        col_incr = col_incr + 1
                        
                if not collision_found:
                    placed_without_collision = True

            # place ship on board
            for col_incr in range(ship_lengths[current_ship]):
                game_board[loc[0]][loc[1] + col_incr] = ship_codings[current_ship]
        else:

            # position vertically
            placed_without_collision = False

            while not placed_without_collision:
                
                # generate random location, (row, col), within bottom half
                # of board for vertical placement, accounting for its length
                loc = (random.randint(len(game_board) // 2,
                                      len(game_board) - length),
                       random.randint(0, len(game_board) - 1))
                
                # check for collisions
                collision_found = False
                for row_incr in range(ship_lengths[current_ship]):
                    if game_board[loc[0] + row_incr][loc[1]] != '*':
                        collision_found = True
                        
                if not collision_found:
                    placed_without_collision = True

            # place ship on board
            for row_incr in range(ship_lengths[current_ship]):
                game_board[loc[0] + row_incr][loc[1]] = ship_codings[current_ship]


def validateBombingInput(ui, gameboard):
    size = len(gameboard)
    # The userInput can only be size 2 or 3 (e.g, A9 or A10)
    
    
    # check to see if the first item in userInput is a letter
    

    # making sure the character after the letter can be converted
    # to a number (use exception handling for this)
    
    # make sure the bombing is in the computer side


    # If none of above then
    return None
    
# bombing: This function you takes two parameters, i) the gameboard,
#   and ii) a string ('player' or 'computer'). If the string is 'player',
#   then you need to prompt the user for a grid to bomb. Please validate
#   the input (by calling the validateBombing function). If the string
#   is 'computer', then you will generate two random numbers in the first
#   half (generating row and col numbers), because the computer only bombs
#   the player area. Then you need to check the grid to see if there is
#   'no hit', 'already hit', or 'direct hit';

#  --- if 'no hit', print('no hit'), and replace the content of the cell with X
#  --- if 'already hit', only print('already hit') and
#  --- if 'direct hit', print('direct hit') and replace the content
#           of the cell with '-'+gameboard[row][col]+'-'

def bombing(gameboard, s):    
    heading = colHeading(gameboard)
    
    if s == 'Player':                   
        userInput = input('\nEnter grid location to bomb (e.g. A4): ')


# Traverse over the half of the gameboard (depending on if you are checking
#   the win condition for the player or computer) to make sure no
#   ['a','b','c','s','d'] is left in that area. 
def win(rowList, gameboard):
    
    return None


def main():
    #step1: get the level from user and error handling
    level = input('Please enter the level of play (1-9): ')
    while (not level.isdigit()) or int(level) > 9 or int(level) < 1 :
        level = input('Please enter the level of play (1-9): ')
        
    level = int(level)
    game_board = board(level)
    #displayBoard(game_board)
    computerShipPosition(game_board)
    displayBoard(game_board)
       
    playerShipPosition(game_board)
   

    print('\nGAME STARTED...\n')
    displayBoard(game_board)
        
        

    # Game Started
    gameover = False
    boardsize = len(game_board)
    while not gameover:
        # call to bombing function for player
        bombing(game_board, 'Player')
        # check to see if the player won
        if win([boardsize//2-1,boardsize], game_board):
           gameover = True
           print('\nYOU WON...\n')
        # call to bombing function for computer
        bombing(game_board, 'Computer')
        # check to see if the computer won
        if win([0,boardsize//2], game_board):
           gameover = True
           print('\nYOU LOST...\n')

        displayBoard(game_board)
    

main()