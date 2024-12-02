from argparse import ArgumentParser

def get_columns(file_path):

    col_0 = []
    col_1 = []

    with open(file_path, "r") as open_file:
        for line in open_file:
            num_0, num_1 = map(int, line.strip().split())
            col_0.append(num_0)
            col_1.append(num_1)

    return (col_0, col_1)

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
    parser.add_argument("file_path")
    args = parser.parse_args()

    col0, col1 = get_columns(args.file_path)
    _12_01_part_1(col0, col1)
    _12_01_part_2(col0, col1)


