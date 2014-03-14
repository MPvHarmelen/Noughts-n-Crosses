def make_a_move(event):
    if turn == player:
        co = player_stuff(event)
    
    elif turn == computer:
        co = computer_stuff()

    if return_cell(co) == empty:
        change_cell(co, turn)
        
        # Change turns
        if turn == X:
            turn = O
        else:
            turn = X

def player_stuff(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        column_clicked = pos[0]//(cellsize[0]+margin)
        row_clicked = pos[1]//(cellsize[1]+margin)
        return (column_clicked, row_clicked)
        
def computer_stuff():
    empty_list = empty_cells(gamedict)
    if empty_list != []
        return random.choice(empty_list)
        
