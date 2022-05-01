def main():
    instructions = get_input()
    part1(instructions)
    instructions = get_input()
    part2(instructions)
    return 0

def get_input():
    f = open("input.txt", "r")
    instructions = []
    for line in f:
        instructions.append(list(line.strip()))
    return instructions

def part1(instructions):
    neighbours_db = generate_neighbour_db(instructions)
    for i in range(100):
        instructions = run_one_round(instructions, neighbours_db)
    print(count_lights_on(instructions))
    return 0

def part2(instructions):
    neighbours_db = generate_neighbour_db(instructions)
    instructions = update_corners(instructions)
    for i in range(100):
        instructions = run_one_round(instructions, neighbours_db)
        instructions = update_corners(instructions)
    print(count_lights_on(instructions))
    return 0

def run_one_round(initial_instructions, neighbours_db):
    updated_instructions = initialise_updated_instructions(initial_instructions)
    for i in range(len(initial_instructions)):
        for j in range(len(initial_instructions[0])):
            current_coordinate = (i,j)
            neighbours_on = count_neighbours_on(initial_instructions, current_coordinate, neighbours_db)
            if initial_instructions[i][j] == "#":
                if neighbours_on == 2 or neighbours_on == 3:
                    updated_instructions[i][j] = "#"
                else:
                    updated_instructions[i][j] = "."
            elif initial_instructions[i][j] == ".":
                if neighbours_on == 3:
                    updated_instructions[i][j] = "#"
                else:
                    updated_instructions[i][j] = "."
    return updated_instructions

def initialise_updated_instructions(initial_instructions):
    updated_instructions = []
    for i in range(len(initial_instructions)):
        temp_line = []
        for j in range(len(initial_instructions[0])):
            temp_line.append(None)
        updated_instructions.append(temp_line)
    return updated_instructions

def generate_neighbour_db(initial_instructions):
    neighbours_db = {}
    for i in range(len(initial_instructions)):
        for j in range(len(initial_instructions[0])):
            current_coordinate = (i,j)
            temp_neighbour_list = generate_neighbouring_coordinates(current_coordinate)
            valid_neighbour_list = generate_valid_neighbours(initial_instructions, temp_neighbour_list)
            neighbours_db[current_coordinate] = valid_neighbour_list
    return neighbours_db

def generate_neighbouring_coordinates(current_coordinate):
    NW = (current_coordinate[0] - 1, current_coordinate[1] - 1)
    N = (current_coordinate[0] - 1, current_coordinate[1])
    NE = (current_coordinate[0] - 1, current_coordinate[1] + 1)
    W = (current_coordinate[0], current_coordinate[1] - 1)
    E = (current_coordinate[0], current_coordinate[1] + 1)
    SW = (current_coordinate[0] + 1, current_coordinate[1] - 1)
    S = (current_coordinate[0] + 1, current_coordinate[1])
    SE = (current_coordinate[0] + 1, current_coordinate[1] + 1)
    return [NW, N, NE, W, E, SW, S, SE]

def generate_valid_neighbours(initial_instructions, temp_neighbour_list):
    valid_coordinates = []
    for elem in temp_neighbour_list:
        if elem[0] < 0 or elem[1] < 0 or elem[0] >= len(initial_instructions) or elem[1] >= len(initial_instructions[0]):
            pass
        else:
            valid_coordinates.append(elem)
    return valid_coordinates

def count_neighbours_on(initial_instructions, current_coordinate, neighbours_db):
    counter = 0
    for neighbouring_coordinate in neighbours_db[current_coordinate]:
        if initial_instructions[neighbouring_coordinate[0]][neighbouring_coordinate[1]] == "#":
            counter += 1
    return counter

def count_lights_on(instructions):
    counter = 0
    for i in range(len(instructions)):
        for j in range(len(instructions[0])):
            if instructions[i][j] == "#":
                counter += 1
    return counter

def update_corners(instructions):
    instructions[0][0] = "#"
    instructions[len(instructions) - 1][0] = "#"
    instructions[0][len(instructions) - 1] = "#"
    instructions[len(instructions) - 1][len(instructions) - 1] = "#"
    return instructions

main()