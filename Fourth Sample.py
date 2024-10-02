#REFERENCE: https://www.drcodie.com/battleships/

from random import randrange
import random
  
def check_ok(boat,taken):
      
    boat.sort()
    for i in range(len(boat)):
        num = boat[i]
        if num in taken:
            boat = [-1]
            break          
        elif num < 0 or num > 99:
            boat = [-1]
            break
        elif num % 10 == 9 and i < len(boat)-1:
            if boat[i+1] % 10 == 0:
                boat = [-1]
                break
        if i != 0:
            if boat[i] != boat[i-1]+1 and boat[i] != boat[i-1]+10:
                boat = [-1]
                break
  
    return boat
  
def get_ship(long,taken):
  
    ok = True
    while ok:      
        ship = []
        #ask the user to enter numbers
        print("enter your ship of length ",long)
        for i in range(long):
            boat_num = input("please enter a number")
            ship.append(int(boat_num))       
        #check that ship
        ship = check_ok(ship,taken)
        if ship[0] != -1:
            taken = taken + ship
            break
        else:
           print("error - please try again") 
          
    return ship,taken
          
def create_ships(taken,boats):
  
    ships = []
    #boats = [5,4,3,3,2,2]
      
    for boat in boats:
        ship,taken = get_ship(boat,taken)
        ships.append(ship)
          
    return ships,taken
  
def check_boat(b,start,dirn,taken):
      
    boat = []
    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
    elif dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)
    boat = check_ok(boat,taken)           
    return boat  
  
def create_boats(taken,boats):
  
    ships = []
    #boats = [5,4,3,3,2,2]
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1,4)
            #print(b,boat_start,boat_direction)
            boat = check_boat(b,boat_start,boat_direction,taken)
        ships.append(boat)
        taken = taken + boat
        #print(ships)
      
    return ships,taken
  
def show_board_c(taken):
    print("            battleships    ")
    print("     0  1  2  3  4  5  6  7  8  9")
  
    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in taken:
                ch = " o " 
            row = row + ch
            place = place + 1
              
        print(x," ",row)
  
def get_shot_comp(guesses,tactics):
      
    ok = "n"
    while ok == "n":
        try:
            if len(tactics) > 0:
                shot = tactics[0]
            else:
                shot = randrange(99)
            if shot not in guesses:
                ok = "y"
                guesses.append(shot)
                break
        except:
            print("incorrect entry - please enter again")
              
    return shot,guesses
  
def show_board(hit,miss,comp):
    print("            battleships    ")
    print("     0  1  2  3  4  5  6  7  8  9")
  
    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in miss:
                ch = " x "
            elif place in hit:
                ch = " o "
            elif place in comp:
                ch = " O " 
            row = row + ch
            place = place + 1
              
        print(x," ",row)
  
def check_shot(shot,ships,hit,miss,comp):
      
    missed = 0
    for i in range(len(ships)):      
        if shot in ships[i]:
            ships[i].remove(shot)
            if len(ships[i]) > 0:
                hit.append(shot)
                missed = 1
            else:
                comp.append(shot)
                missed = 2                            
    if missed == 0:
        miss.append(shot)
                  
    return ships,hit,miss,comp,missed
  
def calc_tactics(shot,tactics,guesses,hit):
      
    temp = []
    if len(tactics) < 1:
        temp = [shot-1,shot+1,shot-10,shot+10]
    else:
        if shot-1 in hit:
            temp = [shot+1]
            for num in [2,3,4,5,6,7,8]:
                if shot-num not in hit:
                    temp.append(shot-num) 
                    break
        elif shot+1 in hit:
            temp = [shot-1]
            for num in [2,3,4,5,6,7,8]:
                if shot+num not in hit:
                    temp.append(shot+num) 
                    break
        if shot-10 in hit:
            temp = [shot+10]
            for num in [20,30,40,50,60,70,80]:
                if shot-num not in hit:
                    temp.append(shot-num) 
                    break
        elif shot+10 in hit:
            temp = [shot-10]
            for num in [20,30,40,50,60,70,80]:
                if shot+num not in hit:
                    temp.append(shot+num) 
                    break
    #tactics longer
    cand =[]
    for i in range(len(temp)):
        if temp[i] not in guesses and temp[i] < 100 and temp[i] > -1:
            cand.append(temp[i])
    random.shuffle(cand)
      
    return cand
  
def get_shot(guesses):
      
    ok = "n"
    while ok == "n":
        try:
            shot = input("please enter your guess")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("incorrect number, please try again")
            elif shot in guesses:
                print("incorrect number, used before")                
            else:
                ok = "y"
                break
        except:
            print("incorrect entry - please enter again")
              
    return shot
  
def check_if_empty_2(list_of_lists):
    return all([not elem for elem in list_of_lists ])
  
  
#before game
hit1 = []
miss1 = []
comp1 = []
guesses1 = []  
missed1 = 0
tactics1 = []
taken1 = []
taken2 = []
hit2 = []
miss2 = []
comp2 = []
guesses2 = []  
missed2 = 0
tactics2 = []
  
battleships = [5,4,3,3,2,2]
# game amount of ships
#computer creates a board for player 1
ships1,taken1 = create_boats(taken1,battleships)
#user creates the board for player 2 - show board
ships2,taken2 = create_ships(taken2,battleships)
show_board_c(taken2)
  
#loop
for i in range(80):
  
#player shoots
    guesses1 = hit1 + miss1 + comp1
    shot1 = get_shot(guesses1)
    ships1,hit1,miss1,comp1,missed1 = check_shot(shot1,ships1,hit1,miss1,comp1)
    show_board(hit1,miss1,comp1)
#repeat until ships empty
    if check_if_empty_2(ships1):
        print("end of game - winner in",i)
        break  
#computer shoots
    
    shot2,guesses2 = get_shot_comp(guesses2,tactics2)
    ships2,hit2,miss2,comp2,missed2 = check_shot(shot2,ships2,hit2,miss2,comp2)
    show_board(hit2,miss2,comp2)
      
    if missed2 == 1:
        tactics2 = calc_tactics(shot2,tactics2,guesses2,hit2)
    elif missed2 == 2:
        tactics2 = []
    elif len(tactics2) > 0:
        tactics2.pop(0)
  
    if check_if_empty_2(ships2):
        print("end of game - computer wins",i)
        break

