import ast
import re

def main():
    instructions = get_input()
    part1(instructions)
    part2(instructions)
    return 0

def get_input():
    f = open("input.txt", "r", encoding='utf-8')
    instructions = []
    for line in f:
        instructions.append(line.strip())
    return instructions

def part1(instructions):
    lenght_chars = 0
    lenght_string = 0
    for elem in instructions:
        lenght_chars += len(elem)
        lenght_string += len(ast.literal_eval(elem))
    print(lenght_chars - lenght_string)
    return 0

def part2(instructions):
    lenght_chars = 0
    lenght_new_string = 0
    for elem in instructions:
        lenght_chars += len(elem)
        lenght_new_string += len(elem) + calculate_new_string_len(elem[1:-1]) + 4
    print(lenght_new_string - lenght_chars)
    return 0

def calculate_new_string_len(elem):
    counter = 0
    counter += elem.count('\\')
    counter += elem.count('"')
    return counter


main()