from argparse import ArgumentParser
from math import ceil
import functools

def get_nums(file_path):
    nums = []
    with open(file_path, "r") as open_file:
        for line in open_file:
            nums += [int(i) for i in line.strip().split()]

    return nums

@functools.cache
def recusive_calc(num, blinks):
    if 0 == blinks: 
        return 1
    
    if 0 == num:
        return recusive_calc(1, blinks-1)
    elif len(str(num)) % 2 == 0:
        str_num = str(num)
        return recusive_calc(int(str_num[: ceil(len(str_num)/2)]), blinks-1) + recusive_calc(int(str_num[ceil(len(str_num)/2):]), blinks-1)
    else:
        return recusive_calc(num*2024, blinks-1)

    


def _12_11(nums, blinks):
    total = 0
    for num in nums:
        total += recusive_calc(num, blinks)
    return total



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    numbers = get_nums(args.file_path)

    print(f"Part 1: {_12_11(numbers, 25)}")
    print(f"Part 2: {_12_11(numbers, 75)}")