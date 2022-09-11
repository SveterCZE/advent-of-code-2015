def main():
    instructions = get_instructions()
    part1(instructions)
    part2(instructions)

def get_instructions():
    f = open("input.txt", "r")
    list_of_instructions = []
    for line in f:
        temp_line = line.strip().split()
        if temp_line[0] == "jio" or temp_line[0] == "jie":
            list_of_instructions.append((temp_line[0], temp_line[1][0], int(temp_line[2])))
        elif temp_line[0] == "jmp":
            list_of_instructions.append((temp_line[0], int(temp_line[1])))
        else:
            list_of_instructions.append((temp_line[0], temp_line[1]))
    return list_of_instructions
    
def part1(instructions):
    registers = {}
    registers["a"] = 0
    registers["b"] = 0
    instruction_pointer = 0
    while True:
        registers, instruction_pointer, valid_step = run_instructions(registers, instruction_pointer, instructions)
        if valid_step == False:
            break
    print(registers)
    return 0

def part2(instructions):
    registers = {}
    registers["a"] = 1
    registers["b"] = 0
    instruction_pointer = 0
    while True:
        registers, instruction_pointer, valid_step = run_instructions(registers, instruction_pointer, instructions)
        if valid_step == False:
            break
    print(registers)
    return 0

def run_instructions(registers, instruction_pointer, instructions):
    if instruction_pointer >= len(instructions):
        return registers, instruction_pointer, False
    executed_instruction = instructions[instruction_pointer]
    if executed_instruction[0] == "hlf":
        registers[executed_instruction[1]] = registers[executed_instruction[1]] // 2
        return registers, instruction_pointer + 1, True
    
    elif executed_instruction[0] == "tpl":
        registers[executed_instruction[1]] = registers[executed_instruction[1]] * 3
        return registers, instruction_pointer + 1, True
    
    elif executed_instruction[0] == "inc":
        registers[executed_instruction[1]] = registers[executed_instruction[1]] + 1
        return registers, instruction_pointer + 1, True
    
    elif executed_instruction[0] == "jmp":
        offset = executed_instruction[1]
        return registers, instruction_pointer + offset, True

    elif executed_instruction[0] == "jie":
        if registers[executed_instruction[1]] % 2 == 0:
            return registers, instruction_pointer + executed_instruction[2], True
        else:
            return registers, instruction_pointer + 1, True
    
    elif executed_instruction[0] == "jio":
        if registers[executed_instruction[1]] == 1:
            return registers, instruction_pointer + executed_instruction[2], True
        else:
            return registers, instruction_pointer + 1, True

main()