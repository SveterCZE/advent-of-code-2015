import itertools

def main():
    instructions = get_input()
    part1(instructions)
    part2(instructions)
    return 0

def get_input():
    f = open("input.txt", "r")
    figures = []
    for line in f:
        figures.append(int(line.strip()))
    return figures

def part1(instructions):
    counter = 0
    possible_combinations = []
    for i in range(1, len(instructions) + 1):
        for elem in itertools.combinations(instructions, i):
            possible_combinations.append(elem)
    for elem in possible_combinations:
        if sum(elem) == 150:
            counter += 1
    print(counter)
    return 0

def part2(instructions):
    counter = 0
    for i in range(1, len(instructions) + 1):
        possible_combinations = []
        for elem in itertools.combinations(instructions, i):
            possible_combinations.append(elem)
        for elem in possible_combinations:
            if sum(elem) == 150:
                counter += 1
        if counter > 0:
            print(counter)
            break
    return 0

main()