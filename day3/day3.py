def main():
    instructions = get_input()
    part1(instructions)
    part2(instructions)
    return 0

def get_input():
    f = open("input.txt", "r")
    # instructions = []
    for line in f:
        return list(line.strip())

def part1(instructions):
    coord = (0,0)
    visited_houses = {}
    visited_houses[coord] = 1
    for movement in instructions:
        coord = execute_movement(coord, movement)
        if coord in visited_houses:
            visited_houses[coord] += 1
        else:
            visited_houses[coord] = 1
    print(len(visited_houses))
    return 0

def execute_movement(coord, movement):
    if movement == "^":
        return (coord[0], coord[1] + 1)
    elif movement == "v":
        return (coord[0], coord[1] - 1)
    elif movement == ">":
        return (coord[0] + 1, coord[1])
    elif movement == "<":
        return (coord[0] - 1, coord[1])

def part2(instructions):
    santa_coord = (0,0)
    robo_santa_coord = (0,0)
    visited_houses = {}
    visited_houses[santa_coord] = 2
    for i in range(len(instructions)):
        if i % 2 == 0:
            santa_coord = execute_movement(santa_coord, instructions[i])
            if santa_coord in visited_houses:
                visited_houses[santa_coord] += 1
            else:
                visited_houses[santa_coord] = 1
        else:
            robo_santa_coord = execute_movement(robo_santa_coord, instructions[i])
            if robo_santa_coord in visited_houses:
                visited_houses[robo_santa_coord] += 1
            else:
                visited_houses[robo_santa_coord] = 1
    print(len(visited_houses))

main()