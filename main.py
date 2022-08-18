import os

PLAYER_1 = 'X'
PLAYER_2 = 'O'

grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
actual_marker = PLAYER_1
is_on = True


def draw_grid(grid):
    return f'''
     |     |  
  {grid[0][0]}  |  {grid[0][1]}  |  {grid[0][2]} 
_____|_____|_____
     |     |   
  {grid[1][0]}  |  {grid[1][1]}  |  {grid[1][2]}
_____|_____|_____
     |     |   
  {grid[2][0]}  |  {grid[2][1]}  |  {grid[2][2]}
     |     |
'''


def check_grid(grid):
    # check columns
    for item in range(3):
        if grid[0][item] != ' ':
            if grid[0][item] == grid[1][item] == grid[2][item]:
                return True

    # check rows
    for list in grid:
        if list[0] != ' ':
            if list[0] == list[1] == list[2]:
                return True

    # check diagonals
    if grid[1][1] != ' ':
        if grid[0][0] == grid[1][1] == grid[2][2]:
            return True
        elif grid[0][2] == grid[1][1] == grid[2][0]:
            return True

print(draw_grid(grid))
while not check_grid(grid):
    line_raw = input('Type a line (1, 2 or 3): ')
    if line_raw.isdigit():
        line = int(line_raw)    
        column_raw = input('Type a column(1, 2 or 3): ')
        if column_raw.isdigit():
            column = int(column_raw)   
            if column > 3 or line > 3:
                print('Out of range')
            elif grid[line - 1][column - 1] == ' ':
                grid[line - 1][column - 1] = actual_marker
                if actual_marker == PLAYER_1:
                    actual_marker = PLAYER_2
                else:
                    actual_marker = PLAYER_1
            else:
                print('This place is already taken')
        else:
            pass
    else:
        pass

    print(draw_grid(grid))
