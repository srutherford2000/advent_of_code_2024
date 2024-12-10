from argparse import ArgumentParser

DIRECTIONS = [(1,0), (0,1),(-1,0),(0,-1)]

def get_rows_and_trailheads(file_path):
    rows = []
    trail_heads = []

    with open(file_path, "r") as open_file:
        for y, line in enumerate(open_file):
            rows.append(list(line.strip()))
            try:
                i = 0
                for _ in range(line.count("0")):
                    x = line.index("0",i)
                    trail_heads.append((x, y))
                    i = x+1
            except ValueError:
                pass

    return rows, trail_heads

def num_trails(x,y, rows):
    if rows[y][x] == "9":
        return [(x,y)]
    else:
        paths_out = []
        for dx,dy in DIRECTIONS:
            if (0<=x+dx<len(rows[0])) and (0<=y+dy<len(rows)) and (int(rows[y+dy][x+dx])-int(rows[y][x]) == 1):
                paths_out += num_trails(x+dx, y+dy, rows)
        return paths_out

def _12_09(input_data):
    rows, trail_heads = input_data

    p1_total = 0 
    p2_total = 0
    for x,y in trail_heads:
        endpoint_list = num_trails(x,y,rows)
        p1_total += len(set(endpoint_list))
        p2_total += len(endpoint_list)

    return p1_total, p2_total

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    in_data = get_rows_and_trailheads(args.file_path)

    ans1,ans2 = _12_09(in_data)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")