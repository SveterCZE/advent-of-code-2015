def get_instructions():
    f = open("input.txt", "r")
    instructions = []
    for line in f:
        if "AND" in line:
            temp_split = line.strip().split()
            temp_AND_instruction = AND_instruction(temp_split[0], temp_split[2], temp_split[4])
            instructions.append(temp_AND_instruction)
        elif "OR" in line:
            temp_split = line.strip().split()
            temp_OR_instruction = OR_instruction(temp_split[0], temp_split[2], temp_split[4])
            instructions.append(temp_OR_instruction)
        elif "RSHIFT" in line:
            temp_split = line.strip().split()
            temp_RSHIFT_instruction = RSHIFT_instruction(temp_split[0], temp_split[2], temp_split[4])
            instructions.append(temp_RSHIFT_instruction)
        elif "LSHIFT" in line:
            temp_split = line.strip().split()
            temp_LSHIFT_instruction = LSHIFT_instruction(temp_split[0], temp_split[2], temp_split[4])
            instructions.append(temp_LSHIFT_instruction)
        elif "NOT" in line:
            temp_split = line.strip().split()
            temp_NOT_instruction = NOT_instruction(temp_split[1], temp_split[3])
            instructions.append(temp_NOT_instruction)
        else:
            temp_split = line.strip().split()
            temp_INIT_instruction = INIT_instruction(temp_split[0], temp_split[2])
            instructions.append(temp_INIT_instruction)
    return instructions

def main():
    instructions = get_instructions()
    new_value = part1(instructions)
    instructions = get_instructions()
    part2(instructions, new_value)
    return 0

def part1(instructions):
    variable_status = {}
    while True:
        for elem in instructions:
            elem.execute_instruction(variable_status)
        if all_instructions_executed(instructions) == True:
            break
    a_value = variable_status["a"]
    print(a_value)
    return a_value

def part2(instructions, new_value):
    variable_status = {}
    while True:
        for elem in instructions:
            elem.execute_instruction(variable_status)
        if all_instructions_executed(instructions) == True:
            break
        variable_status["b"] = new_value
    a_value = variable_status["a"]
    print(a_value)
    return 0

def all_instructions_executed(instructions):
    for elem in instructions:
        if elem.get_execution_status() == False:
            return False
    return True

class instruction_template():
    def get_execution_status(self):
        return self.executed

class shift_class(instruction_template):
    def __init__ (self, input, shift, output):
        self.input = input
        self.shift = int(shift)
        self.output = output
        self.executed = False
    
    def get_variable_values(self, variable_status):
        if self.input in variable_status:
            temp_A = variable_status[self.input]
        elif self.input.isnumeric():
            temp_A = int(self.input)
        else:
            temp_A = None
        return temp_A

class combination_class(instruction_template):
    def __init__ (self, input1, input2, output):
        self.input1 = input1
        self.input2 = input2
        self.output = output
        self.executed = False

    def get_variable_values(self, variable_status):
        if self.input1 in variable_status:
            temp_A = variable_status[self.input1]
        elif self.input1.isnumeric():
            temp_A = int(self.input1)
        else:
            temp_A = None

        if self.input2 in variable_status:
            temp_B = variable_status[self.input2]
        elif self.input2.isnumeric():
            temp_B = int(self.input2)
        else:
            temp_B = None
        
        return temp_A, temp_B

class AND_instruction(combination_class):
    def execute_instruction(self, variable_status):
        if self.executed == True:
            pass
        A, B = self.get_variable_values(variable_status)
        if A == None or B == None:
            return
        else:
            variable_status[self.output] = (A & B) % 65536
            self.executed = True

class OR_instruction(combination_class):
    def execute_instruction(self, variable_status):
        if self.executed == True:
            pass
        A, B = self.get_variable_values(variable_status)
        if A == None or B == None:
            return
        else:
            variable_status[self.output] = (A | B) % 65536
            self.executed = True

class RSHIFT_instruction(shift_class):
    def execute_instruction(self, variable_status):
        if self.executed == True:
            pass
        A = self.get_variable_values(variable_status)
        if A == None:
            return
        else:
            variable_status[self.output] = (A >> self.shift) % 65536
            self.executed = True

class LSHIFT_instruction(shift_class):
    def execute_instruction(self, variable_status):
        if self.executed == True:
            pass
        A = self.get_variable_values(variable_status)
        if A == None:
            return
        else:
            variable_status[self.output] = (A << self.shift) % 65536
            self.executed = True

class NOT_instruction(instruction_template):
    def __init__ (self, input, output):
        self.input = input
        self.output = output
        self.executed = False
    
    def get_variable_values(self, variable_status):
        if self.input in variable_status:
            temp_A = variable_status[self.input]
        elif self.input.isnumeric():
            temp_A = int(self.input)
        else:
            temp_A = None
        return temp_A

    def execute_instruction(self, variable_status):
        if self.executed == True:
            pass
        A = self.get_variable_values(variable_status)
        if A == None:
            return
        else:
            variable_status[self.output] = ~A % 65536
            self.executed = True

class INIT_instruction(instruction_template):
    def __init__ (self, input, output):
        self.input = input
        self.output = output
        self.executed = False

    def execute_instruction(self, variable_status):
        if self.executed == True:
            pass
        if self.input.isnumeric():
            variable_status[self.output] = int(self.input)
            self.executed = True
        else:
            if self.input in variable_status:
                variable_status[self.output] = variable_status[self.input]
                self.executed = True
            else:
                pass

main()