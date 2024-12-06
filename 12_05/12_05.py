from argparse import ArgumentParser

def get_input_file(file_path):
    rules = {}
    updates = []
    with open(file_path, "r") as open_file:
        for line in open_file:
            if "|" in line:
                a,b = line.strip().split("|")
                if a not in rules:
                    rules[a] = []
                rules[a].append(b)
            elif "," in line:
                updates.append(line.strip().split(","))
    return rules, updates

def get_valid_and_invalid_rows(rules, updates):
    valid_updates = []
    invalid_updates = []
    
    for update in updates:
        valid_update = True

        for i, num in enumerate(update):
            if (num in rules) and (set(rules[num]).intersection(set(update[:i]))):
                valid_update = False
                break
        
        if valid_update:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    return valid_updates, invalid_updates



def _12_04_part1(rules, updates):
    valid_updates, _ = get_valid_and_invalid_rows(rules, updates)

    return sum([int(update[len(update)//2]) for update in valid_updates]) 

def fix_row(rules, row):
    things_to_fix = True

    while(things_to_fix):
        things_to_fix = False

        for i, num in enumerate(row):
            if num in rules:
                for rule in rules[num]:
                    if rule in row[:i]:
                        things_to_fix = True
                        row[row.index(rule)] = num
                        row[i] = rule
                        break
                if things_to_fix:
                    break

def _12_04_part2(rules, updates):
    _, invalid_updates = get_valid_and_invalid_rows(rules, updates)

    for row in invalid_updates:
        fix_row(rules, row)
    
    return sum([int(update[len(update)//2]) for update in invalid_updates]) 




if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    rules, rows = get_input_file(args.file_path)
    print(f"Part 1: {_12_04_part1(rules, rows)}")
    print(f"Part 2: {_12_04_part2(rules, rows)}")


