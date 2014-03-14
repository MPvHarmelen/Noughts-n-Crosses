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
caption  = "Naughts and crosses"

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
    empty_list = empty_cells(gameboard)
    if empty_list != []:
        return random.choice(empty_list)

def victory_checker(gameboard):
    ''' If there is a winner, victory_checker returns tuple (p,q).
p indicates row, column or diagonal ('r', 'c' and 'd' respectively).
q indicates which row, column or diagonal.

If there isn't a winner, victory_checker returns False.'''
    # Check for winning columns
    for x_co in range(gridsize):
        if return_cell((x_co,0)) != empty:
            flag = True
            for y_co in range(gridsize):
                if return_cell((x_co,y_co)) != return_cell((x_co,0)):
                     flag = False
                     break
            if flag:
                return ('c',x_co)

    # Rows
    for y_co in range(gridsize):
        if return_cell((0,y_co)) != empty:
            flag = True
            for x_co in range(gridsize):
                if return_cell((x_co,y_co)) != return_cell((0,y_co)):
                     flag = False
                     break
            if flag:
                return ('r',y_co)

    # 1st diagonal
    if return_cell((0,0)) != empty:
        flag = True
        for co in range(gridsize):
            if return_cell((co,co)) != return_cell((0,0)):
                flag = False
                break
        if flag:
            return ('d',0)

    # 2nd diagonal
    if return_cell((gridsize-1,0)) != empty:
        flag = True
        for co in range(gridsize):
            if return_cell((co,(gridsize-1)-co)) != return_cell((0,0)):
                flag = False
                break
        if flag:
            return ('d',1)
    
    # Default
    return False

# Define utility functions
def draw_screen():
    for x_co in range(gridsize):
        for y_co in range(gridsize):
            color = return_cell((x_co,y_co))
            pygame.draw.rect(screen,color,[margin+(cellsize[0]+margin)*x_co,
                                           margin+(cellsize[1]+margin)*y_co,
                                           cellsize[0],cellsize[1]])
    
  
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
            if event.key == r: # the r key
                gameboard, turn = initialize_game()

        if turn == player and event.type == pygame.MOUSEBUTTONDOWN:
            turn = make_a_move(player)
        elif turn == computer:
            turn = make_a_move(computer)

    # Check for winner
    victory = victory_checker(gameboard)
    if victory:
        print(victory, "Let's play again")
        gameboard, turn = initialize_game()
        
    # Check for draw
    if empty_cells(gameboard) == []:
        print("It's a draw, let's play again!")
        gameboard, turn = initialize_game()
    
    # Set the screen background
    screen.fill(black)

    # Draw the screenn
    draw_screen()
    
    # Limit to [speed] frames per second
    clock.tick(speed)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()

'''
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


















