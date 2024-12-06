from argparse import ArgumentParser

DIRECTIONS = [(-1,0),(0,1),(1,0),(0,-1)]

def get_rows_and_start(file_path):
    rows = []
    start_x = -1
    start_y = -1

    with open(file_path, "r") as open_file:
        for y, line in enumerate(open_file):
            rows.append(list(line.strip()))
            try:
                start_x = line.index("^")
                start_y = y
            except ValueError:
                pass

    return rows, (start_x, start_y)

def get_path(rows, start_ind):
    x,y = start_ind
    found_loop = False
    dir = 0
    visited = set()
    while (0<=x<len(rows[0])) and (0<=y<len(rows)):
        
        if (x,y,dir) in visited:
            found_loop = True
            break

        dy,dx = DIRECTIONS[dir]
        visited.add((x,y,dir))
        if(0<=x+dx<len(rows[0])) and (0<=y+dy<len(rows)) and (rows[y+dy][x+dx] == "#"):
            dir = (dir+1)%len(DIRECTIONS)
        else:
            y+=dy
            x+=dx

    return found_loop, visited


def _12_06_part1(rows, start_ind):
    _,path = get_path(rows, start_ind)   

    visited_no_dir = set()
    for (x,y,_) in path:
        visited_no_dir.add((x,y))

    return len(visited_no_dir)

def _12_06_part2(rows, start_ind):
    
    possible_obs_loc = []
    for j, row in enumerate(rows):
        for i in range(len(row)):
            if row[i] == ".":
                possible_obs_loc.append((i,j))

    loops = 0
    for a,b in possible_obs_loc:
        rows[b][a] = '#'
        
        in_loop, _ = get_path(rows, start_ind)

        loops += 1 if in_loop else 0

        rows[b][a] = '.'

    return loops


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    rows, start_ind = get_rows_and_start(args.file_path)
    
    print(f"Part 1: {_12_06_part1(rows,start_ind)}")
    print(f"Part 2: {_12_06_part2(rows,start_ind)}")


