from argparse import ArgumentParser

UP_DOWN_LEFT_RIGHT = [(-1,0),(1,0),(0,-1),(0,1)]
DIAGONAL = [(-1,-1),(-1,1),(1,-1),(1,1)]

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
           (arr[i + mult_i*2][j + mult_j*2] == "A") and \
           (arr[i + mult_i*3][j + mult_j*3] == "S")

def find_mas(arr, i, j):
    counts = 0

    potential_dirs = UP_DOWN_LEFT_RIGHT + DIAGONAL
    
    for i_mult, j_mult in potential_dirs:
        if check_match(arr, i, j, i_mult, j_mult):
            counts += 1

    return counts


def valid_x(arr, i, j):
    #the x will need +/- 1 from i and j, so ensure it fits
    if (0 < j < len(arr[i])-1) and (0 < i < len(arr)-1):

        vals = [arr[i+a][j+b] for a,b in DIAGONAL]

        if (2 == vals.count("M")) and (2 == vals.count("S")) and \
           (arr[i-1][j-1]!=arr[i+1][j+1]) and (arr[i-1][j+1]!= arr[i+1][j-1]):
            return True

    return False

def _12_04_part1(input_data):
    num_xmas_found = 0

    for i, line in enumerate(input_data):
        for j, letter in enumerate(line):
            if "X" == letter:
                num_xmas_found += find_mas(arr, i, j)
    
    return num_xmas_found

def _12_04_part2(input_data):
    num_xmas_found = 0

    for i, line in enumerate(input_data):
        for j, letter in enumerate(line):
            if "A" == letter:
                num_xmas_found += 1 if valid_x(arr, i, j) else 0
    
    return num_xmas_found

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    arr = get_2D_arr(args.file_path)
    print(f"Part 1: {_12_04_part1(arr)}")
    print(f"Part 2: {_12_04_part2(arr)}")


