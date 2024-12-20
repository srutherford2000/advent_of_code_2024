from argparse import ArgumentParser
import re
from PIL import Image

def get_text_row(file_name):
    rows = []
    with open(file_name, "r") as open_file:
        for line in open_file:
            str_px, str_py, str_vx, str_vy = re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line.strip())[0]
            rows.append((int(str_px), int(str_py), int(str_vx), int(str_vy)))
    
    return rows

def prod_of_list(items):
    prod = 1
    for item in items:
        prod*=item
    return prod

def _12_14_part1(rows, width, height):
    
    quadrants = [0]*4
    for (px,py,vx,vy) in rows:
        end_x = (px + (100*vx)) % width
        end_y = (py + (100*vy)) % height
        if(end_x < width//2) and (end_y < height//2):
            quadrants[0] += 1
        if(end_x > width//2) and (end_y < height//2):
            quadrants[1] += 1
        if(end_x < width//2) and (end_y > height//2):
            quadrants[2] += 1
        if(end_x > width//2) and (end_y > height//2):
            quadrants[3] += 1

    return prod_of_list(quadrants)

def has_triangle(x,y, end_locs):
    for j in range(5):
        for i in range(j-1, j+2):
            if(x+i, y+j) not in end_locs:
                return False
    return True

def _12_14_part2(rows, width, height):
    found_tree = False
    second = 0

    while not found_tree:
        second += 1
        end_locs = set()
        for (px,py,vx,vy) in rows:
            end_x = (px + (second*vx)) % width
            end_y = (py + (second*vy)) % height
            end_locs.add((end_x, end_y))
        
        for(x,y) in end_locs:
            if(has_triangle(x,y,end_locs)):
                found_tree = True
                break
    
    return second
           

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    rows = get_text_row(args.file_path)
    
    print(f"Part 1: {_12_14_part1(rows, 101, 103)}")
    print(f"Part 2: {_12_14_part2(rows, 101, 103)}")
        