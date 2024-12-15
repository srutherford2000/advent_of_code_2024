from argparse import ArgumentParser

DIRECTIONS = {"^":(0,-1), ">":(1,0), "v":(0,1), "<":(-1,0)}

START_INDS = {"@":[(0,0)], "O":[(0,0)], "[":[(1,0),(0,0)], "]":[(-1,0),(0,0)]}

DIRECTIONS_TO_CHECK = {"@":{"^":[(0,-1)], ">":[(1,0)], "v":[(0,1)], "<":[(-1,0)]},
                       "O":{"^":[(0,-1)], ">":[(1,0)], "v":[(0,1)], "<":[(-1,0)]},
                       "[":{"^":[(0,-1),(1,-1)], "v":[(0,1),(1,1)], ">":[(2,0)]},
                       "]":{"^":[(0,-1),(-1,-1)], "v":[(0,1),(-1,1)], "<":[(-2,0)]}}


def get_text_row(file_name):
    with open(file_name, "r") as open_file:
        grid, direction = open_file.read().split("\n\n")
    
    expanded_grid = grid.replace("#","##").replace("O","[]").replace(".","..").replace("@","@.")

    return [list(row) for row in grid.split("\n")], [list(row) for row in expanded_grid.split("\n")], direction.replace("\n", "")

def find_start (grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                return x,y

def calc_box_sum(grid, target):
    box_sum = 0
    for i, row in enumerate(grid):
        row_str = "".join(row)
        ind = 0
        while target in row_str[ind:]:
            box_sum += i*100 + row_str.index(target, ind)
            ind = row_str.index(target, ind)+1
    
    return box_sum

def can_move(rows, x, y, dir):
    if rows[y][x] ==".":
        return True
    elif rows[y][x] == "#":
        return False
    else:
        for (d_x,d_y) in DIRECTIONS_TO_CHECK[rows[y][x]][dir]:
            if not can_move(rows, x+d_x,y+d_y, dir):
                return False
        return True


def do_move(rows,x,y,dir):
    #move all the things in the way
    for (d_x,d_y) in DIRECTIONS_TO_CHECK[rows[y][x]][dir]:
        if (rows[y+d_y][x+d_x] != "."):
            do_move(rows, x+d_x,y+d_y, dir)
    
    #move yourself
    for (start_x, start_y) in START_INDS[rows[y][x]]:
        d_x, d_y = DIRECTIONS[dir]
        rows[y+start_y+d_y][x+start_x+d_x] = rows[y+start_y][x+start_x]
        rows[y+start_y][x+start_x] = "."

def _12_15(rows, dirs, target):
    x,y = find_start(rows)
    for dir in dirs:
        if can_move(rows, x, y, dir):
            do_move(rows, x, y, dir)
            x += DIRECTIONS[dir][0]
            y += DIRECTIONS[dir][1]

    return calc_box_sum(rows, target)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    rows, expanded_rows, dirs = get_text_row(args.file_path)

    print(f"Part 1: {_12_15(rows,dirs, 'O')}")
    print(f"Part 2: {_12_15(expanded_rows, dirs, '[]')}")