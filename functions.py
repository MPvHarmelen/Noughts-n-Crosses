import sys

def print_dict(dic, sort_by=0, ljust=10):
    '''prints a dict sorted by key (if sort_by == 0) or by value (if sort_by == 1)
the size of the justification can be changed by giving a different value for ljust'''
    li = sorted(dic.items(), key=lambda s: s[sort_by])
    for sett in li:
        key,thingy = sett
        print (str(key).ljust(ljust), thingy)

def screen_sizer(gridsize, cellsize, margin=0, margin_on_outside=True):
    '''Takes the amount columns & rows and the width & height of each cell.
Optionally takes a margin, of which you can state if you want it on the outsides or not.
Returns a tuple of the screen size (x,y)'''
    #if outisde is true, screen_width is set to margin, else screen_width is set to -margin
    screen_width = screen_height = (margin_on_outside and [margin] or [margin * -1])[0]
    for i in range(gridsize[0]):
        screen_width += cellsize[0] + margin
    for i in range(gridsize[1]):
        screen_height += cellsize[1] + margin
    return (screen_width, screen_height)

def print_grid(grid):
    '''Neatly prints a grid, with numbering on the sides.
I don't think it's flipped, but if you do notice, please tell me.'''
    print (end='   ')
    #print the numbers at the top
    for i in range(len(grid[0])):
        print (i,end='  ')
    #print a whitespace
    print()
    #print the row number, then the row itself
    for i in range(len(grid)):
        print(i,grid[i])

def grid_maker(gridsize, cell_fill):
    '''Returns a grid with the given size
and fills each sell with the given fill.
[gridsize] must be a tuple of at least two terms
(only the first two will be used).
[cell_fill] can be anything.

A grid consists of a list for the y coordinates
and for each y coordinate a list for the x coordinates. Like so:

1 2 3
a b c
p q r

is

[[1,2,3],['a','b','c'],['p','q','r']]

A grid can be viewed more easily by using
functions.print_grid(grid)'''
    grid = []
    for row in range(gridsize[1]):
        grid.append([])
        for column in range(gridsize[0]):
            grid[row].append(cell_fill)
    return grid

def dict_maker(gridsize, fill):
    '''Returns a dict where the keys are 2d coordinates (x,y),
and alle the values are the given fill'''
    bordlist = []
    for x_co in range(gridsize[0]):
        for y_co in range(gridsize[1]):
            bordlist.append(((x_co,y_co),fill))
    return dict(bordlist)

def strip(string, chars):
    '''Returns a string stripped of all characters in chars'''
    output = ''
    for c in string:
        if c not in chars:
            output += c
    return output

def print_list(list):
        for i in list:
            print (i, end=', ')
