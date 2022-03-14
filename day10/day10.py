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
    result = instructions
    for i in range(40):
        result = apply_counter(result)
    print(len(result))
    return 0

def apply_counter(instructions):
    modified_string = []
    letter_rider = 0
    counter_rider = 0
    while True:
        letter_repetitions = 0
        while instructions[counter_rider] == instructions[letter_rider]:
            letter_repetitions += 1
            counter_rider += 1
            if counter_rider >= len(instructions):
                break
        modified_string.append(letter_repetitions)
        modified_string.append(instructions[letter_rider])
        letter_rider = counter_rider
        if letter_rider >= len(instructions):
            break
    return ''.join([str(elem) for elem in modified_string])

def part2(instructions):
    result = instructions
    for i in range(50):
        result = apply_counter(result)
    print(len(result))
    return 0

main()