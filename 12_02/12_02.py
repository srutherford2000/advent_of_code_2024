from argparse import ArgumentParser

def get_rows(file_path, delimeter=None):
    rows = []
    with open(file_path, "r") as open_file:
        for line in open_file:
            #get the row as integers
            rows.append(list(map(int, line.strip().split(delimeter))))
    return rows

def validate_row(row):
    valid_row = True
    increasing = row[1] > row[0]

    for i in range(1,len(row)):
        if (increasing and row[i] < row[i-1]) or (not increasing and row[i] > row[i-1]) or (abs(row[i]-row[i-1]) not in range(1,4)):
            valid_row = False
            break
    
    return valid_row

def _12_02_part_1(rows):
    num_safe = 0
    for row in rows:
        num_safe += 1 if validate_row(row) else 0

    print(f"Part 1: {num_safe}")

def _12_02_part_2(rows):
    num_safe = 0
    for row in rows:
        valid_row = False
        for i in range(len(row)):
            if validate_row(row[:i] + row[i+1:]):
                valid_row = True
                break
        
        num_safe += 1 if valid_row else 0

    print(f"Part 2: {num_safe}")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    rows = get_rows(args.file_path)
    _12_02_part_1(rows)
    _12_02_part_2(rows)


