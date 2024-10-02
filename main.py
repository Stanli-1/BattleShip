#References:
#     https://www.youtube.com/watch?v=MgJBgnsDcF0


#https://replit.com/join/spmsbvsx-darrenerasmus
#   https://replit.com/join/dwjfosom-darrenerasmus
### OFFICIAL DUE DATE: FRIDAY

from BorderedText import bordered
import TableIt
from prettytable import PrettyTable 
from colorama import Fore, Style, Back, init
init()

#Standard libraries
import os
import sys
import time
import random



#-------------------------BattleShip--------------------------
# General Rules:
#  - This is a single player game where you have to win within a     certain amount of shots
#  - Grid is 10x10 and their are 8 ships with varying lengths
#  - Ships are randomly placed and CANNOT be diagonal
#  - Tell computer where you would like to shoot with the            corrisponding letter and number Ex. A3
#  - If you sink all ships in 50 shots, you win!


# Legend:
# ' . ' = water or empty space
# ' 0 ' = part of a ship
# ' X ' = part of a ship that has been hit
# ' # ' = a missed shot (hit water)


#-----------------Defining---------------------------

#the grid
#a 2-dimentional array (has x and y axis)
grid = [[]]
grid2 = [[]]
#grid size (length and width)
grid_size = 10
#Number of enemy ships
num_of_ships = 8
#game over?
game_over = False
#number of ships sunk
num_of_ships_sunk = 0
num_of_ships_sunk2 = 0
#defines where ships are
ship_positions = [[]]
ship_positions2 = [[]]
#Alphabet (horizontal rows)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



#------------------------Functions--------------------------


### Code from Video Listed Above ###

### modified to clear the screen, add pipe characters, and accept additional user input errors w/o throwing an error

### --- TO-DO: --- ###
# add in 2-player functionality ( ? )
# maybe remove the O's (batleships are supposed to be secret)
# Graphical display of board using turtle or something like that (maybe).
# Have user(s) be able to place own ships

# Example of Turtle Module being used with snake: https://www.edureka.co/blog/python-turtle-module/



def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """Will check the row or column to see if it is safe to place a ship there"""
    global grid
    global ship_positions

    all_positions_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_positions_valid = False
                break
    if all_positions_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_positions_valid


def validate_grid_and_place_ship2(start_row, end_row, start_col, end_col):
    """Will check the row or column to see if it is safe to place a ship there"""
    global grid2
    global ship_positions2

    all_positions_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid2[r][c] != ".":
                all_positions_valid = False
                break
    if all_positions_valid:
        ship_positions2.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid2[r][c] = "O"
    return all_positions_valid


def try_to_place_ship_on_grid(row, col, direction, length):
    """Based on direction will call helper method to try and place a ship on the grid"""
    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)


def try_to_place_ship_on_grid2(row, col, direction, length):
    """Based on direction will call helper method to try and place a ship on the grid"""
    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_ship2(start_row, end_row, start_col, end_col)

def create_grid():
    """Will create a 10x10 grid and randomly place down ships
       of different sizes in different directions"""
    global grid
    global grid_size
    global num_of_ships
    global ship_positions

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        grid.append(row)

    num_of_ships_placed = 0

    ship_positions = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1

###################################

def create_grid2():
    global grid2
    global grid_size
    global num_of_ships
    global ship_positions2

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    grid2 = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        grid2.append(row)

    num_of_ships_placed = 0

    ship_positions2 = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid2(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1

def print_grid():
    """Will print the grid with rows A-J and columns 0-9"""
    global grid
    global alphabet

    debug_mode = True

    alphabet = alphabet[0: len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=" │")

        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                if debug_mode:
                    print(f"{Fore.GREEN}O{Style.RESET_ALL}", end="│")
                else:
                    print(".", end="│")
            else:
                print(grid[row][col], end="│")
    
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")



def print_grid2():
    global grid2
    global alphabet2

    debug_mode = True

    alphabet2 = alphabet2[0: len(grid2) + 1]

    for row in range(len(grid2)):
        print(alphabet2[row], end=" │")

        for col in range(len(grid2[row])):
            if grid2[row][col] == "O":
                if debug_mode:
                    print(f"{Fore.GREEN}O{Style.RESET_ALL}", end="│")
                else:
                    print(".", end="│")
            else:
                print(grid2[row][col], end="│")
    
        print("")

    print("  ", end=" ")
    for i in range(len(grid2[0])):
        print(str(i), end=" ")
    print("")

def accept_valid_bullet_placement():
    """Will get valid row and column to place bullet shot"""
    global alphabet
    global grid

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
        placement = input("Enter row (A-J) and column (0-9) such as A3: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column such as A3\n")
            continue
        elif len(placement) == 1:
            print("\nError: Please enter only one row and column such as A3")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter letter (A-J) for row and (0-9) for column\n")
            continue
        row = alphabet.find(row)
        if not (-1 < row < grid_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        col = int(col)
        if not (-1 < col < grid_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        if grid[row][col] == "#" or grid[row][col] == "X":
            print("You have already shot a bullet here, pick somewhere else\n")
            continue
        if grid[row][col] == "." or grid[row][col] == "O":
            is_valid_placement = True

    return row, col



def accept_valid_bullet_placement2():
    """Will get valid row and column to place bullet shot"""
    global alphabet2
    global grid2

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
        placement = input("Enter row (A-J) and column (0-9) such as A3: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column such as A3\n")
            continue
        elif len(placement) == 1:
            print("\nError: Please enter only one row and column such as A3")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter letter (A-J) for row and (0-9) for column\n")
            continue
        row = alphabet2.find(row)
        if not (-1 < row < grid_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        col = int(col)
        if not (-1 < col < grid_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        if grid[row][col] == "#" or grid[row][col] == "X":
            print("You have already shot a bullet here, pick somewhere else\n")
            continue
        if grid[row][col] == "." or grid[row][col] == "O":
            is_valid_placement = True

    return row, col

def check_for_ship_sunk(row, col):
    """If all parts of a shit have been shot it is sunk and we later increment ships sunk"""
    global ship_positions
    global grid

    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            # Ship found, now check if its all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
    return True


def check_for_ship_sunk2(row, col):
    """If all parts of a shit have been shot it is sunk and we later increment ships sunk"""
    global ship_positions2
    global grid2

    for position in ship_positions2:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            # Ship found, now check if its all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid2[r][c] != "X":
                        return False
    return True




def shoot_bullet():
    """Updates grid and ships based on where the bullet was shot"""
    global grid
    global num_of_ships_sunk

    row, col = accept_valid_bullet_placement()
    print("")
    print("\n----------------------------")

    if grid[row][col] == ".":
        os.system('clear')
        print("You missed, no ship was shot\n")
        grid[row][col] = "#"
    elif grid[row][col] == "O":
        os.system('clear')
        print("You hit!\n", end=" ")
        grid[row][col] = "X"
        if check_for_ship_sunk(row, col):
            print("A ship was completely sunk!\n")
            num_of_ships_sunk += 1
        else:
            os.system('clear')
            print("A ship was shot!\n")


def shoot_bullet2():
    """Updates grid and ships based on where the bullet was shot"""
    global grid2
    global num_of_ships_sunk2

    row, col = accept_valid_bullet_placement()
    print("")
    print("----------------------------")

    if grid2[row][col] == ".":
        os.system('clear')
        print("You missed, no ship was shot\n")
        grid2[row][col] = "#"
    elif grid2[row][col] == "O":
        os.system('clear')
        print("You hit!\n", end=" ")
        grid2[row][col] = "X"
        if check_for_ship_sunk2(row, col):
            print("A ship was completely sunk!\n")
            num_of_ships_sunk2 += 1
        else:
            os.system('clear')
            print("A ship was shot\n")




def check_for_game_over():
    """If all ships have been sunk or we run out of bullets its game over"""
    global num_of_ships_sunk
    global num_of_ships_sunk2
    global num_of_ships
    global game_over

    if num_of_ships == num_of_ships_sunk:
        print("Congrats player 1 won!")
        game_over = True

    elif num_of_ships == num_of_ships_sunk2:
        print("Congrats player 2 won!")
        game_over = True



def main():
    """Main entry point of application that runs the game loop"""
    global game_over

    print("-----Welcome to Battleships-----\n")
    print("You have 50 bullets to take down 8 ships, may the battle begin!")

    create_grid()
    create_grid2()


    while game_over is False:
        print("Player's 1 Board")
        print_grid2()
        print("\nPlayer's 2 Board")
        print_grid()
        print("\nPlayer 1's turn")
        print("\nNumber of ships remaining: " + str(num_of_ships - num_of_ships_sunk))
        shoot_bullet()
        print("----------------------------")
        print("")
        check_for_game_over()
        if game_over == True:
          break
        
        print("Player's 1 Board")
        print_grid2()
        print("\nPlayer's 2 Board")
        print_grid()
        print("\nPlayer 2's turn")
        print("\nNumber of ships remaining: " + str(num_of_ships - num_of_ships_sunk2))
        shoot_bullet2()
        print("----------------------------")
        print("")
        check_for_game_over()


# if __name__ == '__main__':
#     main()









