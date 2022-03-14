def main():
    instructions = get_input()
    part1(instructions)
    part2(instructions)
    return 0

def get_input():
    f = open("input.txt", "r")
    flight_database = {}
    for line in f:
        split_line = line.split()
        dest1, dest2, distance = split_line[0], split_line[2], split_line[4]
        print(dest1, dest2, distance)
    return flight_database

def part1(instructions):
    print(instructions)
    return 0 

def part2(instructions):
    print(instructions)
    return 0

main()