from argparse import ArgumentParser
from itertools import combinations

def get_files_and_free_spaces(file_path):
    file_and_space = []
    with open(file_path, "r") as open_file:
        id = 0
        for line in open_file:
            for char in line.strip():
                for _ in range(int(char)):
                    if id % 2 == 0:
                        file_and_space.append(id//2)
                    else:
                        file_and_space.append(None)
                id +=1

    return file_and_space

def _12_09_part1(line):
    
    while None in line:
        try:
            line[line.index(None)] = line.pop(-1)
        except:
            pass
    
    check_sum = 0
    for i, num in enumerate(line):
        check_sum += i*num
    
    return check_sum

def _12_09_part2(line):
    for id in range(line[-1], 0, -1):
        search_area = line.index(id)
        count = line.count(id)
        ind = 0
        space_block_ind = line.index(None, ind)

        try:
            while space_block_ind < search_area:
                if (line[space_block_ind:space_block_ind+count] == [None]*count):
                    for _ in range(count):
                        line[line.index(id)] = None
                    for i in range(space_block_ind, space_block_ind+count):
                        line[i] = id
                    break
                else:
                    ind = space_block_ind+1
                    space_block_ind = line.index(None, ind)
        except:
            pass

    check_sum = 0
    for i, num in enumerate(line):
        try:
            check_sum += i*num
        except:
            pass
    
    return check_sum


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    line = get_files_and_free_spaces(args.file_path)

    print(f"Part 1: {_12_09_part1(line.copy())}")
    print(f"Part 2: {_12_09_part2(line.copy())}")