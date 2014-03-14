# --- initiating the main loop

#Loop until the user clicks the close button.
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

# Used to determen who's turn it is
turn = X

# -------- Main Program Loop -----------
while done==False:
    
    for event in pygame.event.get(): # User did something
        
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit the programme
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column_clicked = pos[0]//(cellsize[0]+margin)
            row_clicked = pos[1]//(cellsize[1]+margin)
            try: # sometimes the below raises an error,
                # so this is to prevent a crash
                if grid[row_clicked][column_clicked] == empty:
                    if turn == X:
                        grid[row_clicked][column_clicked] = X
                    else:
                        grid[row_clicked][column_clicked] = O
                    # Change turns
                    if turn == X:
                        turn = O
                    else:
                        turn = X
            except: pass
        
        if event.type == pygame.KEYDOWN:
            if event.key == 114: # the r key
                # reset the grid
                grid = functions.grid_maker(gridsize, empty)
                
                
    # Set the screen background
    screen.fill(black)

    # Draw the screen
    for row in range(gridsize[1]):
        for column in range(gridsize[0]):
            color = grid[row][column]
            pygame.draw.rect(screen,color,[margin+(cellsize[0]+margin)\
                                           *column,margin+(cellsize[1]+margin)\
                                           *row,cellsize[0],cellsize[1]])
    # Limit to [speed] frames per second
    clock.tick(speed)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
