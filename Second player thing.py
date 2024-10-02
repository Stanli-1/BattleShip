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


grid2 = [[]]
#grid size (length and width)
grid_size = 10
#Number of enemy ships
num_of_ships2 = 8
#bullets left
bullets_left = 50
#game over?
game_over = False
#number of ships sunk
num_of_ships_sunk2 = 0
#defines where ships are
ship_positions2 = [[]]
#Alphabet (horizontal rows)
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


def create_grid2():
    """Will create a 10x10 grid and randomly place down ships
       of different sizes in different directions"""
    global grid2
    global grid_size
    global num_of_ships2
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

    while num_of_ships_placed != num_of_ships2:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid2(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1

###################################

def print_grid2():
    """Will print the grid with rows A-J and columns 0-9"""
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

def accept_valid_bullet_placement2():
    """Will get valid row and column to place bullet shot"""
    global alphabet2
    global grid2

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
        placement2 = input("Enter row (A-J) and column (0-9) such as A3: ")
        placement2 = placement2.upper()
        if len(placement2) <= 0 or len(placement2) > 2:
            print("\nError: Please enter only one row and column such as A3")
            continue
        elif len(placement2) == 1:
            print("Error: Please enter only one row and column such as A3")
            continue
        row = placement2[0]
        col = placement2[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        row = alphabet2.find(row)
        if not (-1 < row < grid_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        col = int(col)
        if not (-1 < col < grid_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        if grid2[row][col] == "#" or grid2[row][col] == "X":
            print("You have already shot a bullet here, pick somewhere else")
            continue
        if grid2[row][col] == "." or grid2[row][col] == "O":
            is_valid_placement = True

    return row, col


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
    global grid2
    global num_of_ships_sunk2
    global bullets_left

    row, col = accept_valid_bullet_placement2()
    print("")
    print("----------------------------")

    if grid2[row][col] == ".":
        os.system('clear')
        print("You missed, no ship was shot")
        grid2[row][col] = "#"
    elif grid2[row][col] == "O":
        os.system('clear')
        print("You hit!", end=" ")
        grid2[row][col] = "X"
        if check_for_ship_sunk2(row, col):
            print("A ship was completely sunk!")
            num_of_ships_sunk2 += 1
        else:
            os.system('clear')
            print("A ship was shot")

    bullets_left -= 1


def check_for_game_over():
    """If all ships have been sunk or we run out of bullets its game over"""
    global num_of_ships_sunk2
    global num_of_ships2
    global bullets_left
    global game_over

    if num_of_ships2 == num_of_ships_sunk2:
        print("Congrats you won!")
        game_over = True
    elif bullets_left <= 0:
        print("Sorry, you lost! You ran out of bullets, try again next time!")
        game_over = True


def main():
    """Main entry point of application that runs the game loop"""
    global game_over

    print("-----Welcome to Battleships-----\n")
    print("You have 50 bullets to take down 8 ships, may the battle begin!")

    create_grid2()

    while game_over is False:
        print_grid2()
        print("\nNumber of ships remaining: " + str(num_of_ships2 - num_of_ships_sunk2))
        print("Number of bullets left: " + str(bullets_left))
        shoot_bullet()
        print("----------------------------")
        print("")
        check_for_game_over()


if __name__ == '__main__':
    main()