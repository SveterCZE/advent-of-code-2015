def main():
    instructions = get_input()
    new_password = part1(instructions)
    part1(iterate_password(new_password))
    return 0

def get_input():
    f = open("input.txt", "r")
    for line in f:
        return list(line.strip())

def part1(password):
    while True:
        if is_valid_password(password):
            break
        password = iterate_password(password)
    print("".join(password))
    return list(password)

def is_valid_password(password):
    if contains_illegal_chars(password):
        return False
    if contains_two_pair(password) == False:
        return False
    if contains_a_triplet(password) == False:
        return False
    return True

def contains_two_pair(password):
    pair_letters = set()
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            pair_letters.add(password[i])
    if len(pair_letters) > 1:
        return True
    else:
        return False

def contains_illegal_chars(password):
    if "i" in password or "o" in password or "l" in password:
        return True
    else:
        return False

def contains_a_triplet(password):
    for i in range(len(password) - 2):
        if ord(password[i]) - ord(password[i + 1]) == -1 and ord(password[i]) - ord(password[i + 2]) == -2:
            return True
    return False

def iterate_password(password):
    init_rider = len(password) - 1
    password = iterate_password_recursive_helper(password, init_rider)
    return password

def iterate_password_recursive_helper(password, init_rider):
    # BASE CASE - the letter we are chaning is not "z", so we change and return it
    if password[init_rider] != "z":
        password[init_rider] = chr(ord(password[init_rider]) + 1)
        return password
    else:
        password[init_rider] = "a"
        password = iterate_password_recursive_helper(password, init_rider - 1)
        return password

main()