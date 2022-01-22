def main():
    instructions = get_input()
    part1(instructions)
    part2(instructions)
    return 0

def get_input():
    f = open("input.txt", "r")
    for line in f:
        return list(line)

def part1(instructions):
    floor = 0
    for elem in instructions:
        if elem == ")":
            floor -= 1
        elif elem == "(":
            floor += 1
    print(floor)
    return 0

def part2(instructions):
    floor = 0
    for i in range (len(instructions)):
        if instructions[i] == ")":
            floor -= 1
        elif instructions[i] == "(":
            floor += 1
        if floor < 0:
            print(i + 1)
            break
    return 0

main()