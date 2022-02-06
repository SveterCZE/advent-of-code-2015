def main():
    instructions = get_input()
    part1(instructions)
    part2(instructions)
    return 0

def get_input():
    f = open("input.txt", "r")
    instructions = []
    for line in f:
        temp_line = line.strip().split()
        instructions.append((temp_line[-4], temp_line[-3].split(","), temp_line[-1].split(",")))
    return instructions

def part1(instructions):
    grid = [[0 for x in range(1000)] for y in range(1000)]
    for instruction in instructions:
        execute_instruction(grid, instruction)
    print(count_bulbs_on(grid))
    return 0

def execute_instruction(grid, instruction):
    if instruction[0] == "toggle":
        toggle(grid, instruction[1:])
    elif instruction[0] == "on":
        turn_switches(grid, instruction[1:], 1)
    elif instruction[0] == "off":
        turn_switches(grid, instruction[1:], 0)

def toggle(grid, instruction):
    for x in range(int(instruction[0][0]), int(instruction[1][0]) + 1):
        for y in range(int(instruction[0][1]), int(instruction[1][1]) + 1):
            if grid[x][y] == 0:
                grid[x][y] = 1
            else:
                grid[x][y] = 0

def turn_switches(grid, instruction, mode):
    for x in range(int(instruction[0][0]), int(instruction[1][0]) + 1):
        for y in range(int(instruction[0][1]), int(instruction[1][1]) + 1):
            grid[x][y] = mode

def count_bulbs_on(grid):
    bulbs_on = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                bulbs_on += 1
    return bulbs_on

def part2(instructions):
    grid = [[0 for x in range(1000)] for y in range(1000)]
    for instruction in instructions:
        execute_instruction_part2(grid, instruction)
    print(count_bightness(grid))
    return 0

def execute_instruction_part2(grid, instruction):
    if instruction[0] == "toggle":
        turn_switches_p2(grid, instruction[1:], 2)
    elif instruction[0] == "on":
        turn_switches_p2(grid, instruction[1:], 1)
    elif instruction[0] == "off":
        turn_switches_p2(grid, instruction[1:], -1)

def turn_switches_p2(grid, instruction, mode):
    for x in range(int(instruction[0][0]), int(instruction[1][0]) + 1):
        for y in range(int(instruction[0][1]), int(instruction[1][1]) + 1):
            grid[x][y] += mode
            if grid[x][y] < 0:
                grid[x][y] = 0

def count_bightness(grid):
    brightness = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            brightness += grid[x][y]
    return brightness

main()