import copy

def main():
    instructions, initial_molecule = get_input()
    part1(instructions, list(initial_molecule))
    part2(instructions, initial_molecule)
    return 0

    
def get_input():
    f = open("input.txt", "r")
    instructions = {}
    all_formulae_saved = False
    for line in f:
        split_line = line.strip().split(" ")
        if len(split_line[0]) == 0:
            all_formulae_saved = True
            continue
        if all_formulae_saved == False:
            if split_line[0] not in instructions:
                instructions[split_line[0]] = set()
            instructions[split_line[0]].add(split_line[2])
        else:
            initial_molecule = split_line[0]
    return instructions, initial_molecule

def part1(instructions, initial_molecule):
    modified_molecules = generate_modified_molecules(instructions, initial_molecule)
    print(len(modified_molecules))
    return 0

def part2(instructions, target_molecule):
    return 0
#     round = 1
#     initial_molecule = "e"
#     current_reviewed_molecules = set()
#     current_reviewed_molecules.add(initial_molecule)
#     while True:
#         new_modified_molecules = set()
#         for elem in current_reviewed_molecules:
#             temp_modified_molecules = generate_modified_molecules(instructions, list(elem))
#             for temp_molecule in temp_modified_molecules:
#                 new_modified_molecules.add(temp_molecule)
#         if target_molecule in new_modified_molecules:
#             print(round)
#             break
#         else:
#             round += 1
#             clensed_molecules = remove_long_molecules(new_modified_molecules, target_molecule)
#             # if round > 3:
#             #     clensed_molecules = remove_molecules_do_not_match(new_modified_molecules, target_molecule)
#             current_reviewed_molecules = clensed_molecules
#         print(round)
#     print("END")
#     return 0

# def remove_molecules_do_not_match(new_modified_molecules, target_molecule):
#     valid_molecules = set()
#     for checked_molecule in new_modified_molecules:
#         for i in range(len(checked_molecule)):
#             pass

# def remove_long_molecules(new_modified_molecules, target_molecule):
#     clensed_molecules = set()
#     for elem in new_modified_molecules:
#         if len(elem) > len(target_molecule):
#             pass
#         else:
#             clensed_molecules.add(elem)
#     return clensed_molecules

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