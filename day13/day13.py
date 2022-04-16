import itertools

def main():
    instructions = get_input()
    part1(instructions)
    part2(instructions)
    return 0

def get_input():
    f = open("input.txt", "r")
    relationships = {}
    for line in f:
        split_line = line.strip().split()
        person = split_line[0]
        change_symbol = split_line[2]
        if change_symbol == "lose":
            change_value = int(split_line[3]) * -1
        else:
            change_value = int(split_line[3])
        neighbour = split_line[-1][:-1]
        if person not in relationships:
            relationships[person] = {}
            relationships[person][neighbour] = change_value
        else:
            relationships[person][neighbour] = change_value
    return relationships

def part1(instructions):
    calculation_helper(instructions)
    return 0

def part2(instructions):
    instructions = insert_me(instructions)
    calculation_helper(instructions)
    return 0

def calculation_helper(instructions):
    list_of_seating_arrangements = create_lists_of_seating_arrangements(instructions)
    best_seating_value = 0
    for elem in list_of_seating_arrangements:
        current_seating_value = calculate_seating_value(elem, instructions)
        if current_seating_value > best_seating_value:
            best_seating_value = current_seating_value
    print(best_seating_value)
    return 0

def create_lists_of_seating_arrangements(instructions):
    temp_list = []
    for key in instructions.keys():
        temp_list.append(key)
    return itertools.permutations(temp_list)

def calculate_seating_value(seating_arrangement, relationships):
    current_seating_value = 0
    for i in range(len(seating_arrangement)):
        current_person = seating_arrangement[i]
        left_person = seating_arrangement[i-1]
        right_person = seating_arrangement[(i+1) % len(seating_arrangement)]
        current_seating_value += relationships[current_person][left_person]
        current_seating_value += relationships[current_person][right_person]
    return current_seating_value

def insert_me(relationships):
    for key in relationships.keys():
        relationships[key]["me"] = 0
    relationships["me"] = {}
    for key in relationships.keys():
        if key != "me":
            relationships["me"][key] = 0
    return relationships

main()