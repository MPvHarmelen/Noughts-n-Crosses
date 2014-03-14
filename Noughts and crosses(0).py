import sys
import pygame
import functions
import random

debug = False
# Define some colors
black = (   0,   0,   0)
white = ( 255, 255, 255)
red   = ( 255,   0,   0)
green = (   0, 255,   0)
blue  = (   0,   0, 255)

# Define some keys
r = 114

# Set sizes, speed & caption
gridsize = 3
cellsize = (30,30)
margin   = 1
speed    = 24
caption  = "Notes and crosses"

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

# Define some functions
def change_cell(coordinates, value):
    '''Changes the cell at the given coordinates to value'''
    gamedict[coordinates] = value

def return_cell(coordinates):
    '''Returns the value of the given coordinates'''
    return gamedict.get(coordinates)

def empty_cells(gamedict):
    '''Returns a list with coordinates of all empty cells.'''
    empty_cells = []
    for co in gamedict.keys():
        if gamedict[co] == empty:
            empty_cells.append(co)
    return empty_cells
    
def victory_checker(gamedict):
    ''' If there is a winner, victory_checker returns tuple (p,q).
p indicates row, column or diagonal ('r', 'c' and 'd' respectively).
q indicates which row, column or diagonal.

If there isn't a winner, victory_checker returns False.'''
    keylist = sorted(gamedict.keys())
    # The below is to check if a player has captured a whole row
    for y_co in range(gridsize):
        if gamebord != empty\
           and gamebord[y_co].count(gamebord[y_co][0]) == len(gamebord):
            return ('r',y_co)

    # This is to check for columns
    for x_co in range(gridsize):
        buffer = []
        for y_co in  range(gridsize):
            buffer.append(gamebord[y_co][x_co])
        if buffer[0] != empty\
           and buffer.count(buffer[0]) == gridsize:
            return ('c',x_co)

    # Here we do the first diagonal, from top left to bottom right
    buffer = []
    for co in range(gridsize):
        buffer.append(gamebord[co][co])
    if buffer[0] != empty\
       and buffer.count(buffer[0]) == gridsize:
        return ('d',0)

    # Finally, the second diagonal
    buffer = []
    mirror = lambda x: -1*(x+1)
    for co in range(gridsize):
        buffer.append(gamebord[co][mirror(co)])
    if buffer[0] != empty\
       and buffer.count(buffer[0]) == gridsize:
        return ('d',1)
        
    return False
            
def initialize_game():
    '''Returns an empty gamedict and X'''
    return (functions.dict_maker((gridsize,gridsize), empty), X)

gamedict, turn = initialize_game()
if debug: print('turn = ',turn)

def make_a_move(event):
    co = None
    if debug: print(1, turn, player)
    if turn == player:
        if event.type == pygame.MOUSEBUTTONDOWN:
            co = player_stuff(event)
        if debug: print(2)
    elif turn == computer:
        co = computer_stuff()
        if debug: print(3)
    if return_cell(co) == empty:
        if debug: print(4)
        change_cell(co, turn)
        if debug: print ('turn = ',turn)
        # Change turns
        if turn == X:
            return O
            if debug: print('it should have changed by now', turn)
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
    empty_list = empty_cells(gamedict)
    if empty_list != []:
        return random.choice(empty_list)
  
# --- Shit needed for pygame to work, with
#     a function I wrote to size the screen
pygame.init()
screen = pygame.display.set_mode(
    functions.screen_sizer((gridsize,gridsize), cellsize, margin)
    )
pygame.display.set_caption(caption)

# --- initiating the main loop

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
            if event.key == r: # the r key
                gamedict, turn = initialize_game()
                
        turn = make_a_move(event)
        
                        
    # Set the screen background
    screen.fill(black)

    # Draw the screenn
    for x_co in range(gridsize):
        for y_co in range(gridsize):
            color = return_cell((x_co,y_co))
            pygame.draw.rect(screen,color,[margin+(cellsize[0]+margin)*x_co,
                                           margin+(cellsize[1]+margin)*y_co,
                                           cellsize[0],cellsize[1]])
    # Limit to [speed] frames per second
    clock.tick(speed)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

##    # Check for winner
##    victory = victory_checker(grid)
##    if victory:
##        print(victory, "Let's play again")
##        grid, turn = initialize_game()
##        
##    # Check for draw
##    if empty_cells(grid) == []:
##        print("It's a draw, let's play again!")
##        grid, turn = initialize_game()

    
        
    
        
         
    
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()

'''
Remove duplicate at indicated place.
Make uniform treatment of x & y coordinates (y,x), not (x,y)!!
make funtion of draw screen


Rules for the computer, in this order:

- if the computer has captured two squares in a line, place the third one
- elif the player has captured two squares in a line, place the third one
- elif place in a spot with the most possible
- elif place in a spot that isn't in line with any of player's pieces,
    and is in line with as many of computer's pieces as possible.
- elif place in a spot that is in line with the least number of player's pieces,
    and is in line with a many of computer's pieces as possible.
- else place randomly

0,0
0,1
0,2
1,0
1,1
1,2
2,0
2,1
'''


















