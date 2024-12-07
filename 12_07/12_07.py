from argparse import ArgumentParser
from itertools import product 

OPERATORS_1 = "*+"
OPERATORS_2 = "*+|"

def get_rows_data(file_path):
    data = []

    with open(file_path, "r") as open_file:
        for line in open_file:
            total, nums = line.split(":")
            data.append([int(total)]+[int(num) for num in nums.split()])

    return data

def compute_row_no_precedence(row, operators):
    total = row[0]
    for i, operator in enumerate(operators):
        if operator == "*":
            total *= row[i+1]
        elif operator == "+":
            total += row[i+1]
        elif operator == "|":
            total = int(str(total) + str(row[i+1]))

    return total

def calc_valid_rows(rows, operators):
    total_valid = 0
    for row in rows:
        found_match = False
        locs = product(operators, repeat=len(row)-2)
        for loc in locs:
            if row[0] == compute_row_no_precedence(row[1:], loc):
                found_match = True
                break
        total_valid += row[0] if found_match else 0
    return total_valid

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    rows = get_rows_data(args.file_path)

    print(f"Part 1: {calc_valid_rows(rows, OPERATORS_1)}")
    print(f"Part 2: {calc_valid_rows(rows, OPERATORS_2)}")