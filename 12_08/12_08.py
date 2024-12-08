from argparse import ArgumentParser
from itertools import combinations

def get_rows(file_path):
    antinode_locs = {}
    with open(file_path, "r") as open_file:

        for y, line in enumerate(open_file):
            for x, char in enumerate(line.strip()):
                if "." != char:
                    if char not in antinode_locs:
                        antinode_locs[char] = []
                    antinode_locs[char].append((x,y))

    return antinode_locs, x, y

def _12_08_part1(antinode_locs, x, y ):
    antinodes = set()
    for antinode_loc in antinode_locs.values():
        for (x1,y1), (x2,y2) in list(combinations(antinode_loc, 2)):
            dx = x2-x1
            dy = y2-y1
            if(0<= x2+dx <= x) and (0<= y2+dy <= y):
                antinodes.add((x2+dx, y2+dy))
            if(0<= x1-dx <= x) and (0<= y1-dy <= y):
                antinodes.add((x1-dx, y1-dy))

    return len(antinodes)

def _12_08_part2(antinode_locs, x, y ):
    antinodes = set()
    for antinode_loc in antinode_locs.values():
        for (x1,y1), (x2,y2) in list(combinations(antinode_loc, 2)):
            antinodes.add((x1,y1))
            antinodes.add((x2,y2))
            dx = x2-x1
            dy = y2-y1
            while (0<= x2+dx <= x) and (0<= y2+dy <= y):
                x2 = x2+dx
                y2 = y2+dy
                antinodes.add((x2, y2))
            while (0<= x1-dx <= x) and (0<= y1-dy <= y):
                x1 = x1-dx
                y1 = y1-dy
                antinodes.add((x1, y1))

    return len(antinodes)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    antinode_locs, x, y = get_rows(args.file_path)

    print(f"Part 1: {_12_08_part1(antinode_locs, x, y )}")
    print(f"Part 2: {_12_08_part2(antinode_locs, x, y )}")