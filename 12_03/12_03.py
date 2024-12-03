from argparse import ArgumentParser
import re

def get_regex_matches(file_path):
    matches = {"do()":[], "don't()":[]}
    next_mode = {"do()":"don't()", "don't()":"do()"}
    mode = "do()"
    with open(file_path, "r") as open_file:
        for line in open_file:
            ind = 0
            next_index = line.find(next_mode[mode])
            while (next_index != -1):
                matches[mode] += re.findall('mul\(\d+,\d+\)', line[ind:next_index])
                mode = next_mode[mode]
                ind = next_index+1
                next_index = line.find(next_mode[mode], ind)
            
            matches[mode] += re.findall('mul\(\d+,\d+\)', line[ind:])
    return matches

def _12_03(regex_matches):
    total_sum = 0
    for match in regex_matches:
        num1,num2 = match[4:-1].split(",")
        total_sum+=int(num1)*int(num2)
    
    return total_sum

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    regex_matches = get_regex_matches(args.file_path)
    x = regex_matches['do()']+regex_matches["don't()"]
    print(f"Part 1: {_12_03(x)}")
    print(f"Part 2: {_12_03(regex_matches['do()'])}")


