import hashlib

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
    i = 0
    while True:
        test_input = instructions + str(i)
        hash = generate_hash(test_input)
        if is_valid_solution(hash) == True:
            print(i)
            return 0
        else:
            i+=1

def part2(instructions):
    i = 0
    while True:
        test_input = instructions + str(i)
        hash = generate_hash(test_input)
        if is_valid_solution_part2(hash) == True:
            print(i)
            return 0
        else:
            i+=1

def generate_hash(test_input):
    hash = hashlib.md5(test_input.encode()).hexdigest()
    return hash

def is_valid_solution(hash):
    if hash[0] == "0" and hash[1] == "0" and hash[2] == "0" and hash[3] == "0" and hash[4] == "0":
        return True
    else:
        return False

def is_valid_solution_part2(hash):
    if hash[0] == "0" and hash[1] == "0" and hash[2] == "0" and hash[3] == "0" and hash[4] == "0" and hash[5] == "0":
        return True
    else:
        return False

main()