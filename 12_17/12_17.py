from argparse import ArgumentParser
import math

def strip_and_split(line):
    _, data = line.strip().split(": ")
    return data

def get_prog_info(file_name):
    register_a = None
    register_b = None
    register_c = None
    opcodes = None

    with open(file_name, "r") as open_file:
        register_a = int(strip_and_split(open_file.readline()))
        register_b = int(strip_and_split(open_file.readline()))
        register_c = int(strip_and_split(open_file.readline()))

        open_file.readline()

        opcodes = [int(i) for i in strip_and_split(open_file.readline()).split(",")]

    return register_a, register_b, register_c, opcodes


def get_super_operand(code,  a, b, c):
    if code == 0:
        return 0
    elif code == 1:
        return 1
    elif code == 2:
        return 2
    elif code == 3:
        return 3
    elif code == 4:
        return a
    elif code == 5:
        return b
    elif code == 6:
        return c
    else:
        return None
    
def run_program(a,b,c, opcodes):
    outputs = []
    ip = 0

    try:
        while True:
            if opcodes[ip] == 0:
                a = math.floor( a / 2** get_super_operand(opcodes[ip+1], a, b, c))
                ip += 2
            elif opcodes[ip] == 1:
                b = b ^ opcodes[ip+1]
                ip += 2
            elif opcodes[ip] == 2:
                b = get_super_operand(opcodes[ip+1], a, b, c) % 8
                ip += 2
            elif opcodes[ip] == 3:
                if a != 0:
                    ip = opcodes[ip+1]
                else:
                    ip += 2
            elif opcodes[ip] == 4:
                b = b ^ c
                ip+=2
            elif opcodes[ip] == 5:
                outputs.append(get_super_operand(opcodes[ip+1], a, b, c) % 8)
                ip+=2
            elif opcodes[ip] == 6:
                b = math.floor( a / 2** get_super_operand(opcodes[ip+1], a, b, c))
                ip += 2
            elif opcodes[ip] == 7:
                c = math.floor( a / 2** get_super_operand(opcodes[ip+1], a, b, c))
                ip += 2
    except:
        pass

    return outputs

def part_2(a,b,c,opcodes):
    new_a = 0

    while True:
        if (opcodes == run_program(new_a,b,c,opcodes)):
            break
        new_a += 1

    return new_a


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    a,b,c,opcodes = get_prog_info(args.file_path)

    print(f"Part 1: {','.join([str(i) for i in run_program(a,b,c,opcodes)])}")
    print(f"Part 2: {part_2(a,b,c,opcodes)}")



