def victory_checker():
    ''' If there is a winner, victory_checker returns tuple (p,q).
p indicates row, column or diagonal ('r', 'c' and 'd' respectively).
q indicates which row, column or diagonal.

If there isn't a winner, victory_checker returns False.'''
    lines = board_to_lines()

    for key in range(len(lines)):
        if lines[key][0] != empty \
           and lines[key].count(lines[key][0]) == gridsize:
            winline = key
            break

    if winline <= 2:
        return ('r',winline), lines[winline][0]
            
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
