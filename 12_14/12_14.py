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

def make_2d_arr(width, height):
    rows = []
    for _ in range(height):
        rows.append(["O"]*width)
    return rows

def _12_14_part2(rows, width, height):
    with open("out.txt", "w") as out_file:
        for second in range(1000):
            new_image = Image.new("RGB", (width, height), "white")
            pixels = new_image.load()
            for (px,py,vx,vy) in rows:
                end_x = (px + (second*vx)) % width
                end_y = (py + (second*vy)) % height
                pixels[end_x, end_y] = (0,255,0)
           
            new_image.save(f"image_folder/{second}.png")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    rows = get_text_row(args.file_path)
    
    print(f"Part 1: {_12_14_part1(rows, 101, 103)}")
    print(f"Part 2: {_12_14_part2(rows, 101, 103)}")
        