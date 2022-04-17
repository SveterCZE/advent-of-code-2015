import copy

def main():
    instructions = get_input()
    part1(instructions)
    part2(instructions)
    return 0

def get_input():
    f = open("input.txt", "r")
    ingredients_properties = {}
    for line in f:
        split_line = line.strip().split()
        ingredients_properties[split_line[0].strip()] = (int(split_line[2][:-1]), int(split_line[4][:-1]), int(split_line[6][:-1]), int(split_line[8][:-1]), int(split_line[10]))
    return(ingredients_properties)

def part1(instructions):
    possible_combinations = create_possible_combinations(instructions)
    find_best_combination(possible_combinations, instructions)
    return 0

def part2(instructions):
    possible_combinations = create_possible_combinations(instructions)
    possible_combinations_calories = find_target_calories_combination(possible_combinations, instructions, 500)
    find_best_combination(possible_combinations_calories, instructions)
    return 0

def create_possible_combinations(ingredients_properties):
    target_sum = 100
    posssible_combinations = []
    current_combination = []
    create_possible_combinations_recursive_helper(ingredients_properties, target_sum, posssible_combinations, current_combination)
    return posssible_combinations
    
def create_possible_combinations_recursive_helper(ingredients_properties, target_sum, posssible_combinations, current_combination):
    # BASE CASE --- Last item to be inserted
    if (len(current_combination) == len(ingredients_properties) - 1):
        current_sum = sum_current_list(current_combination)
        current_combination.append(target_sum-current_sum)
        posssible_combinations.append(current_combination)
        return 0
    # RECURSIVE CASE --- Build the possible combinations
    current_sum = sum_current_list(current_combination)
    for i in range(target_sum + 1):
        if (i + current_sum) <= target_sum:
            new_temp_combination = copy.deepcopy(current_combination)
            new_temp_combination.append(i)
            create_possible_combinations_recursive_helper(ingredients_properties, target_sum, posssible_combinations, new_temp_combination)
    return 0

def sum_current_list(current_combination):
    current_sum = 0
    for elem in current_combination:
        current_sum += elem
    return current_sum

def find_best_combination(possible_combinations, instructions):
    best_combination = 0
    for combination in possible_combinations:
        combination_value = count_combination_value(combination, instructions)
        if combination_value > best_combination:
            best_combination = combination_value
    print(best_combination)
    return 0

def find_target_calories_combination(possible_combinations, instructions, target_calories):
    permitted_calories = []
    for combination in possible_combinations:
        calorie_value = count_calories(combination, instructions)
        if calorie_value == target_calories:
            permitted_calories.append(combination)
    return permitted_calories

def count_combination_value(combination, instructions):
    capacity = count_capacity(combination, instructions)
    durability = count_durability(combination, instructions)
    flavour = count_flavour(combination, instructions)
    texture = count_texture(combination, instructions)
    return capacity * durability * flavour * texture

def count_capacity(combination, instructions):
    capacity = 0
    rider = 0
    for value in instructions.values():
        capacity += combination[rider] * value[0]
        rider += 1
    if capacity < 0:
        capacity = 0
    return capacity

def count_durability(combination, instructions):
    durability = 0
    rider = 0
    for value in instructions.values():
        durability += combination[rider] * value[1]
        rider += 1
    if durability < 0:
        durability = 0
    return durability

def count_flavour(combination, instructions):
    flavour = 0
    rider = 0
    for value in instructions.values():
        flavour += combination[rider] * value[2]
        rider += 1
    if flavour < 0:
        flavour = 0
    return flavour

def count_texture(combination, instructions):
    texture = 0
    rider = 0
    for value in instructions.values():
        texture += combination[rider] * value[3]
        rider += 1
    if texture < 0:
        texture = 0
    return texture

def count_calories(combination, instructions):
    calories = 0
    rider = 0
    for value in instructions.values():
        calories += combination[rider] * value[4]
        rider += 1
    return calories

main()