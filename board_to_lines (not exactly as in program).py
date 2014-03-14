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
        lines[gridsize*2 -1].append(return_cell((co,co)))
    
    # 2nd diagonal
    lines.append([])
    for co in range(gridsize):
        lines[gridsize*2].append(return_cell((co,(gridsize-1)-co)))

    return lines
