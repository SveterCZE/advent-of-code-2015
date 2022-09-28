import copy
import random

def main():
    instructions, instructions_reversed, initial_molecule = get_input()
    part1(instructions, list(initial_molecule))
    part2(instructions_reversed, initial_molecule)
    return 0

    
def get_input():
    f = open("input.txt", "r")
    instructions = {}
    reversed_instructions_list = []
    all_formulae_saved = False
    for line in f:
        split_line = line.strip().split(" ")
        if len(split_line[0]) == 0:
            all_formulae_saved = True
            continue
        if all_formulae_saved == False:
            # First direction of instructions
            if split_line[0] not in instructions:
                instructions[split_line[0]] = set()
            instructions[split_line[0]].add(split_line[2])
            # Second direction of instructions
            reversed_instructions_list.append((split_line[2], split_line[0]))
        else:
            initial_molecule = split_line[0]
    random.shuffle(reversed_instructions_list)
    return instructions, reversed_instructions_list, initial_molecule

def part1(instructions, initial_molecule):
    modified_molecules = generate_modified_molecules(instructions, initial_molecule)
    print(len(modified_molecules))
    return 0

def part2(instructions, initial_molecula):
    target_molecule = "e"
    while True:
        step_count = random_molecule_generation(initial_molecula, target_molecule, instructions)
        if step_count != None:
            print(step_count)
            break
    return 0

def random_molecule_generation(initial_molecula, target_molecule, instructions):
    counter = 0
    while True:
        match_found = False
        for elem in instructions:
            if elem[0] in initial_molecula:
                initial_molecula = initial_molecula.replace(elem[0], elem[1], 1)
                random.shuffle(instructions)
                match_found = True
                break
        if match_found == False:
            return None
        counter += 1
        if initial_molecula == target_molecule:
            return counter


def generate_modified_molecules(instructions, initial_molecule):
    modified_molecules = set()
    for i in range(len(initial_molecule)):
        # CASE 1 - Lenght 1 molecule
        if initial_molecule[i] in instructions:
            for elem in instructions[initial_molecule[i]]:
                new_molecule_rider = copy.deepcopy(initial_molecule)
                new_molecule_rider[i] = elem
                new_molecule_string = "".join(new_molecule_rider)
                modified_molecules.add(new_molecule_string)
        # CASE 2 - Length 2 molecule
        if i == len(initial_molecule) - 1:
            pass
        else:
            len_2_molecule = initial_molecule[i] + initial_molecule[i+1]
            if len_2_molecule in instructions:
                for elem in instructions[len_2_molecule]:
                    new_molecule_rider = copy.deepcopy(initial_molecule)
                    new_molecule_rider[i] = elem
                    new_molecule_rider[i + 1] = ""
                    new_molecule_string = "".join(new_molecule_rider)
                    modified_molecules.add(new_molecule_string)
    return modified_molecules


main()