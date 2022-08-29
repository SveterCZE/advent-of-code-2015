import re

def main():
    instructions = get_instructions()
    part1(instructions)

def get_instructions():
    f = open("input.txt", "r")
    for line in f:
        instructions = re.findall(r'\d+', line)
        return (int(instructions[0]), int(instructions[1]))

def part1(instructions):
    # instructions = (6,4)
    last_coordinate = (1,1)
    last_coordinate_value = 20151125
    while True:
        last_coordinate, last_coordinate_value, solution_found = build_diagonal(last_coordinate, last_coordinate_value, instructions)
        if solution_found == True:
            break

def build_diagonal(last_coordinate, coordinate_value, instructions):
    next_coordinate = (last_coordinate[1] + 1, 1)
    while next_coordinate[0] >= 1:
        coordinate_value = (coordinate_value * 252533) % 33554393
        # Check if we are at the final destination
        if final_dest_reached(next_coordinate, instructions) == True:
            print(coordinate_value)
            return None, None, True

        # If not, continue
        last_coordinate = next_coordinate
        next_coordinate = (last_coordinate[0] - 1, last_coordinate[1] + 1)

    return last_coordinate, coordinate_value, False

def final_dest_reached(next_coordinate, instructions):
    if next_coordinate == instructions:
        return True
    else:
        return False

main()