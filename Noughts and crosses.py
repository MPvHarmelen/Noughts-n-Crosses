import sys
import pygame
import functions
import random

debug = None
# Define some colors
black = (   0,   0,   0)
white = ( 255, 255, 255)
red   = ( 255,   0,   0)
green = (   0, 255,   0)
blue  = (   0,   0, 255)

# Set sizes, speed & caption
gridsize = 3
cellsize = (30,30)
margin   = 1
speed    = 24
caption  = "Noughts and crosses"

# Define empty, X, O & the winning line (winline)
empty = white
X = blue
O = red
winline = green

# Ask who starts
if input("Do you want to start? (y/n): ") == "y":
    player = X
    computer = O
else:
    player = O
    computer = X

# Define datatype functions
def change_cell(coordinates, value):
    '''Changes the cell at the given coordinates to value'''
    gameboard[coordinates] = value

def return_cell(coordinates):
    '''Returns the value of the given coordinates'''
    return gameboard.get(coordinates)

def empty_cells(gameboard):
    '''Returns a list with coordinates of all empty cells.'''
    empty_cells = []
    for co in gameboard.keys():
        if gameboard[co] == empty:
            empty_cells.append(co)
    return empty_cells

def initialize_game():
    '''Returns an empty gameboard and X'''
    return (functions.dict_maker((gridsize,gridsize), empty), X)

# Define game logic functions
def make_a_move(mover):
    co = None
    if mover == player:
        co = player_stuff(event)
    elif mover == computer:
        co = computer_stuff()
       
    if return_cell(co) == empty:
        change_cell(co, turn)

        # Change turns
        if turn == X:
            return O
        else:
            return X
        
    else:
        return turn

def player_stuff(event):
    pos = pygame.mouse.get_pos()
    column_clicked = pos[0]//(cellsize[0]+margin)
    row_clicked = pos[1]//(cellsize[1]+margin)
    return (column_clicked, row_clicked)
        
def computer_stuff():
    lines = board_to_lines()
    empty_list = empty_cells(gameboard)
    co = None

    # For defensive strategy, occupy middle asap
    if (gridsize//2,gridsize//2) in empty_list:
            return (gridsize//2, gridsize//2)
    
    # Check if the computer can win
    for index in range(len(lines)):
        if lines[index].count(empty) == 1\
           and lines[index].count(computer) == gridsize -1:
                co = (index, lines[index].index(empty))
                if debug == 'computer_stuff':
                    print('I was trying to win and co =', co)

    # Check if the computer must block
    if co == None:
        for index in range(len(lines)):
            if lines[index].count(empty) == 1 \
               and lines[index].count(player) == gridsize -1:
                    co = (index, lines[index].index(empty))
                    if debug == 'computer_stuff':
                        print('I was stopping you from winning & co =', co)

    if co == None:
        index_buffer = []
        for index in range(len(lines)):
            if lines[index].count(player) == 0:
                index_buffer.append(index)
        
        if index_buffer != []:
            count_buffer = []
            for index in index_buffer:
                count_buffer.append(( lines[index].count(computer) , index ))
            
            best_index = sorted(count_buffer)[-1][1]
            co = (best_index, lines[best_index].index(empty))

    

    # Make (x,y) coordinates of co
    if co != None:
        if co[0] < gridsize:
            if debug == 'computer_stuff': print('r')
            return co[1],co[0]
        elif co[0] < gridsize *2:
            if debug == 'computer_stuff': print('c')
            return co[0] - gridsize, co[1]
        elif co[0] == gridsize *2:
            if debug == 'computer_stuff': print('d',0,'co[1] =',co[1])
            return (co[1],co[1])
        elif co[0] == gridsize *2 +1:
            if debug == 'computer_stuff': print('d',1,'co[1] =',co[1])
            return (co[1],(gridsize-1)-co[1])
        else:
            if debug == 'computer_stuff': print("Couldn't find smart")
            empty_list = empty_cells(gameboard)
            if empty_list != []:
                print('oops')
                return random.choice(empty_list)
    else: # if we couldn't do anything smart
        if debug == 'computer_stuff': print('Nothing smart to do')
        if empty_list != []:
            return random.choice(empty_list)
    
def victory_checker():
    ''' If there is a winner, victory_checker returns tuple (p,q).
p indicates row, column or diagonal ('r', 'c' and 'd' respectively).
q indicates which row, column or diagonal.

If there isn't a winner, victory_checker returns False.'''
    lines = board_to_lines()
    winline = None # will contain the key of the winning line

    # Find a winning line
    for key in range(len(lines)):
        if lines[key][0] != empty \
           and lines[key].count(lines[key][0]) == gridsize:
            winline = key
            break

    # Return position of winning line and who won
    if winline != None:
        if winline < gridsize: # the winning line is a row
            return ('r',winline), lines[winline][0]
        elif gridsize <= winline < gridsize*2: # column
            return ('c',winline-gridsize), lines[winline][0]
        elif winline == gridsize *2: # 1st diagonal
            return ('d',0), lines[winline][0]
        else: # 2nd diagonal
            return ('d',1), lines[winline][0]
    else: # No winning line
        return False

def board_to_lines():
    lines = []

    # Rows
    for y_co in range(gridsize):
        lines.append([])
        for x_co in range(gridsize):
            lines[y_co].append(return_cell((x_co,y_co)))
    
    # Columns
    for x_co in range(gridsize):
        lines.append([])
        for y_co in range(gridsize):
            lines[gridsize + x_co].append(return_cell((x_co,y_co)))

    # 1st diagonal
    lines.append([])
    for co in range(gridsize):
        lines[gridsize*2].append(return_cell((co,co)))
    
    # 2nd diagonal
    lines.append([])
    for co in range(gridsize):
        lines[gridsize*2 +1].append(return_cell((co,(gridsize-1)-co)))

    return lines

# Define utility functions
def draw_screen():
    for x_co in range(gridsize):
        for y_co in range(gridsize):
            color = return_cell((x_co,y_co))
            pygame.draw.rect(screen,color,[margin+(cellsize[0]+margin)*x_co,
                                           margin+(cellsize[1]+margin)*y_co,
                                           cellsize[0],cellsize[1]])
def YesNo():
    exit_loop = False
    while exit_loop == False:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                exit_loop = True
                return False # Flag that we are done so we exit the programme
            if event.type == pygame.KEYDOWN:
                if event.unicode == 'y':
                    exit_loop = True
                    return True
                if event.unicode == 'n':
                    exit_loop = True
                    return False
        clock.tick(speed)
    
  
# --- Shit needed for pygame to work, with
#     a function I wrote to size the screen
pygame.init()
screen = pygame.display.set_mode(
    functions.screen_sizer((gridsize,gridsize), cellsize, margin)
    )
pygame.display.set_caption(caption)

# --- initiating the main loop
gameboard, turn = initialize_game()

#Loop until the user clicks the close button.
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

# -------- Main Program Loop -----------
while done==False:       
        
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit the programme
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'r':
                gameboard, turn = initialize_game()

        if turn == player and event.type == pygame.MOUSEBUTTONDOWN:
            turn = make_a_move(player)
        elif turn == computer:
            turn = make_a_move(computer)

    # Set the screen background
    screen.fill(black)

    # Draw the screenn
    draw_screen()
    
    # Limit to [speed] frames per second
    clock.tick(speed)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Check for winner
    victory = victory_checker()
    if victory:
        place, winner = victory
        if winner == computer:
            print ('Yeah! I won at', place,"Do you want to play again? (y/n)")
        elif winner == player:
            print ('NO! You won at', place,"Do you want to play again? (y/n)")
        
        if YesNo() == True:
            gameboard, turn = initialize_game()
        else:
            done = True
        
    # Check for draw
    if empty_cells(gameboard) == []:
        print("It's a draw, do you want to play again? (y/n)")
        if YesNo() == True:
            gameboard, turn = initialize_game()
        else:
            done = True
    
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()

'''


een val dreigt als:
2 lijnen, met elke 2 vakjes leeg, overlappen op een leeg vak




Rules for the computer, in this order:

+ if the computer has captured two squares in a line, place the third one
+ elif the player has captured two squares in a line, place the third one
- elif place in a spot that isn't in line with any of player's pieces,
    and is in line with as many of computer's pieces as possible.
- elif place in a spot that is in line with the least number of player's pieces,
    and is in line with a many of computer's pieces as possible.
- else place randomly

c,p
0,0
0,1
1,0
1,1
'''


















