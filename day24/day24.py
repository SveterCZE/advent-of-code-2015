from itertools import combinations

def main():
    instructions = load_input()
    part1(instructions)
    part2(instructions)
    return 0

def load_input():
    f = open("input.txt", "r")
    gift_list = []
    for line in f:
        gift_list.append(int(line.strip()))
    return gift_list

def part1(instructions):
    run_gift_calculation(instructions, 3)
    return 0

def part2(instructions):
    run_gift_calculation(instructions, 4)
    return 0

def calculate_QE(gifts):
    initial_value = 1
    for gift in gifts:
        initial_value = initial_value * gift
    return initial_value

def run_gift_calculation(instructions, number_of_compartments):
    target_packages_size = sum(instructions) // number_of_compartments
    for i in range(len(instructions)):
        possible_combintations = []
        x = combinations(instructions, i)
        for elem in x:
            if sum(elem) == target_packages_size:
                quantum_emntanglement = calculate_QE(elem)
                possible_combintations.append((quantum_emntanglement, elem))
        possible_combintations.sort()
        for tested_combination in possible_combintations:
            if valid_gift_split_generic(tested_combination, instructions, target_packages_size, number_of_compartments - 1) == True:
                print(tested_combination[0])
                return
    return 0

def valid_gift_split_generic(tested_combination, instructions, target_packages_size, remaining_compartments):
    remaining_gifts = [x for x in instructions if x not in tested_combination[1]]
    remaining_gitf_combinations = combinations(remaining_gifts,  (len(instructions) - len(tested_combination[1])) // remaining_compartments )
    for elem in remaining_gitf_combinations:
        if sum(elem) == target_packages_size:
            return True
    return False

main()