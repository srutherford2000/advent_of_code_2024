from argparse import ArgumentParser

UP_DOWN_LEFT_RIGHT = [(-1,0),(1,0),(0,-1),(0,1)]
DIAGONAL = [(-1,-1),(-1,1),(1,-1),(1,1)]

def get_rows(file_path):
    rows = []
    with open(file_path, "r") as open_file:
        for line in open_file:
            rows.append(line.strip())
    return rows

#generalizes function that makes sure MAS are the next in a specific direction
#mult_i and mult_j should be -1, 0 or 1. And correspond to wether the direction
#should go up/same y/down or left/same x/or right
def check_match(arr, i, j, mult_i, mult_j):
    return (0<= i+mult_i*3 < len(arr)) and \
           (0<= j+mult_j*3 < len(arr[0])) and \
           (arr[i + mult_i][j + mult_j] == "M") and \
           (arr[i + mult_i*2][j + mult_j*2] == "A") and \
           (arr[i + mult_i*3][j + mult_j*3] == "S")

#given an x position (i,j) go ahead and see how many xmas can be spelled in the
#various positions
def find_mas(arr, i, j):
    counts = 0

    potential_dirs = UP_DOWN_LEFT_RIGHT + DIAGONAL
    
    for i_mult, j_mult in potential_dirs:
        if check_match(arr, i, j, i_mult, j_mult):
            counts += 1

    return counts

#given an a position(i,j) go ahead and verify that the x is comprised of two
#overlaping "MAS"es
def valid_x(arr, i, j):
    #the x will need +/- 1 from i and j, so ensure it fits
    if (0 < j < len(arr[i])-1) and (0 < i < len(arr)-1):

        vals = [arr[i+a][j+b] for a,b in DIAGONAL]

        #make sure we have the right number of M's and S's and that each 
        #diagonal has one of each
        if (2 == vals.count("M")) and (2 == vals.count("S")) and \
           (arr[i-1][j-1]!=arr[i+1][j+1]) and (arr[i-1][j+1]!= arr[i+1][j-1]):
            return True

    return False

def _12_04_part1(input_data):
    num_xmas_found = 0

    for i, line in enumerate(input_data):
        for j, letter in enumerate(line):
            if "X" == letter:
                num_xmas_found += find_mas(input_data, i, j)
    
    return num_xmas_found

def _12_04_part2(input_data):
    num_xmas_found = 0

    for i, line in enumerate(input_data):
        for j, letter in enumerate(line):
            if "A" == letter:
                num_xmas_found += 1 if valid_x(input_data, i, j) else 0
    
    return num_xmas_found

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    rows = get_rows(args.file_path)
    print(f"Part 1: {_12_04_part1(rows)}")
    print(f"Part 2: {_12_04_part2(rows)}")


