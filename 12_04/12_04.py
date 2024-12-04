from argparse import ArgumentParser
import re

def get_2D_arr(file_path):
    arr = []
    with open(file_path, "r") as open_file:
        for line in open_file:
            arr.append(list(line.strip()))
    return arr

def check_match(arr, i, j, mult_i, mult_j):
    return (0<= i+mult_i*3 < len(arr)) and \
           (0<= j+mult_j*3 < len(arr[0])) and \
           (arr[i + mult_i][j + mult_j] == "M") and \
           (arr[i+ mult_i*2][j + mult_j*2] == "A") and \
           (arr[i+mult_i*3][j+mult_j*3] == "S")

def find_matches_normal(arr, i, j):
    counts = 0

    potential_dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    
    for i_mult, j_mult in potential_dirs:
        if check_match(arr, i, j, i_mult, j_mult):
            counts += 1

    return counts


def find_matches_x(arr, i, j):
    if ((j-1) >= 0) and ((j+1) < len(arr[i])) and ((i-1) >= 0) and ((i+1) < len(arr)):
        vals = [arr[i-1][j-1], arr[i-1][j+1], arr[i+1][j-1], arr[i+1][j+1] ]
        if (2 == vals.count("M")) and (2 == vals.count("S")) and \
           (arr[i-1][j-1]!=arr[i+1][j+1]) and (arr[i-1][j+1]!= arr[i+1][j-1]):
            return 1

    return 0

def _12_04_part1(input_data):
    num_xmas_found = 0

    for i, line in enumerate(input_data):
        for j, letter in enumerate(line):
            if "X" == letter:
                num_xmas_found += find_matches_normal(arr, i, j)
    
    return num_xmas_found

def _12_04_part2(input_data):
    num_xmas_found = 0

    for i, line in enumerate(input_data):
        for j, letter in enumerate(line):
            if "A" == letter:
                num_xmas_found += find_matches_x(arr, i, j)
    
    return num_xmas_found

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    arr = get_2D_arr(args.file_path)
    print(f"Part 1: {_12_04_part1(arr)}")
    print(f"Part 2: {_12_04_part2(arr)}")


