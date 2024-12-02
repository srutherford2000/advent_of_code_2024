from argparse import ArgumentParser

def get_columns(file_path, delimeter=None):
    #create a dictionary for the columns
    col_dict = {}
    with open(file_path, "r") as open_file:
        for line in open_file:
            #get the row as integers
            nums = list(map(int, line.strip().split(delimeter)))

            for i, num in enumerate(nums):
                #if the column is unseen, create a list
                if f'col_{i}' not in col_dict:
                    col_dict[f'col_{i}'] = []
                #add the number to the right column
                col_dict[f'col_{i}'].append(num)

    return col_dict

def _12_01_part_1(col_0, col_1):
    col_0.sort()
    col_1.sort()

    total_dist = 0
    for i in range(len(col_0)):
        total_dist += abs(col_1[i] - col_0[i])

    print(f"Part 1: {total_dist}")


def _12_01_part_2(col_0, col_1):
    counts = 0
    for num in col_0:
        counts += col_1.count(num) * num

    print(f"Part 2: {counts}")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    col_dict = get_columns(args.file_path)
    _12_01_part_1(col_dict["col_0"], col_dict["col_1"])
    _12_01_part_2(col_dict["col_0"], col_dict["col_1"])


