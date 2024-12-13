from argparse import ArgumentParser
import re
from sympy import symbols, Eq, solve
from math import floor

def get_text_row(row):
    str_x, str_y = re.findall(r"X[+=](\d+), Y[+=](\d+)", row)[0]
    return (int(str_x), int(str_y))

def get_rows(file_path):
    rows = []
    with open(file_path, "r") as open_file:
        all_lines = open_file.readlines()
        for i in range(0, len(all_lines), 4):
            rows.append((get_text_row(all_lines[i]), get_text_row(all_lines[i+1]), get_text_row(all_lines[i+2])))
    return rows

def get_min_token(buttonA, buttonB, prize, is_part1):
    x, y = symbols('x y')
    eq1 = Eq(buttonA[0]*x + buttonB[0]*y, prize[0])
    eq2 = Eq(buttonA[1]*x + buttonB[1]*y, prize[1])

    solutions = solve((eq1, eq2), (x, y))

    if (solutions[x] != floor(solutions[x])) or (solutions[y] != floor(solutions[y])) or (0 > solutions[x]) or (0 > solutions[y]):
        return 0
    elif is_part1 and ((solutions[x] > 100) or ( solutions[y]>100)):
        
        return 0
    else:
        return solutions[x]*3 + solutions[y]


def _12_13(rows, is_part1):
    total = 0
    for i, (a,b,prize) in enumerate(rows):
        if (not is_part1):
            prize = (prize[0] + 10000000000000, prize[1] + 10000000000000)
        total += get_min_token(a,b,prize, is_part1)
    return total

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    rows = get_rows(args.file_path)
    
    print(f"Part 1: {_12_13(rows, True)}")
    print(f"Part 2: {_12_13(rows, False)}")
        