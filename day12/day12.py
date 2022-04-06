import ast

def main():
    instructions = get_input()
    part1(instructions)
    part2(instructions)
    return 0

def get_input():
    f = open("input.txt", "r")
    for line in f:
        return line.strip()

def part1(instructions):
    converted_elements = ast.literal_eval(instructions)
    total_sum = count_total_sum_recursive_helper(converted_elements)
    print(total_sum)
    return 0

def count_total_sum_recursive_helper(converted_elements):
        interim_sum = 0
        if isinstance(converted_elements, int):
            interim_sum += converted_elements
        if isinstance(converted_elements, str):
            pass
        if isinstance(converted_elements, list):
            for elem in converted_elements:
                interim_sum += count_total_sum_recursive_helper(elem)
        if isinstance(converted_elements, dict):
            temp_list = []
            for key, value in converted_elements.items():
                temp = [key,value]
                temp_list.append(temp)
            interim_sum += count_total_sum_recursive_helper(temp_list)
        return interim_sum

def part2(instructions):
    converted_elements = ast.literal_eval(instructions)
    total_sum = count_total_sum_recursive_helper_no_red(converted_elements)
    print(total_sum)
    return 0

def count_total_sum_recursive_helper_no_red(converted_elements):
        interim_sum = 0
        if isinstance(converted_elements, int):
            interim_sum += converted_elements
        if isinstance(converted_elements, str):
            pass
        if isinstance(converted_elements, list):
            for elem in converted_elements:
                interim_sum += count_total_sum_recursive_helper_no_red(elem)
        if isinstance(converted_elements, dict):
            if contains_red(converted_elements) == False:
                temp_list = []
                for key, value in converted_elements.items():
                    temp = [key,value]
                    temp_list.append(temp)
                interim_sum += count_total_sum_recursive_helper_no_red(temp_list)
        return interim_sum

def contains_red(converted_elements):
    for key, value in converted_elements.items():
        if key == "red" or value == "red":
            # print(converted_elements)
            return True
    return False

main()
