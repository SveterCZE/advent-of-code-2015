def main():
    instructions = get_input()
    part1(instructions)
    part2(instructions)
    return 0

def get_input():
    f = open("input.txt", "r")
    instructions = []
    for line in f:
        instructions.append(line.strip())
    return instructions

def part1(instructions):
    nice_word_count = 0
    for word in instructions:
        if is_nice_word_part1(word):
            nice_word_count +=1
    print (nice_word_count)
    return 0

def is_nice_word_part1(word):
    if no_forbidden_word(word) and three_vowels(word) and double_letter(word):
        return True
    else: 
        return False

def no_forbidden_word(word):
    if "ab" in word or "cd" in word or "pq" in word or "xy" in word:
        return False
    else:
        return True

def three_vowels(word):
    wovels = "aeiou"
    wovel_count = 0
    for letter in word:
        if letter in wovels:
            wovel_count +=1
    if wovel_count >= 3:
        return True
    else:
        return False

def double_letter(word):
    previous_letter = None
    for i in range(len(word)):
        if word[i] == previous_letter:
            return True
        else:
            previous_letter = word[i]
    return False

def part2(instructions):
    nice_word_count = 0
    for word in instructions:
        if is_nice_word_part2(word):
            nice_word_count +=1
    print (nice_word_count)
    return 0

def is_nice_word_part2(word):
    if one_letter_in_between(word) and two_unique_pair(word):
        return True
    else: 
        return False

def two_unique_pair(word):
    unique_pairs = generate_unique_pairs(word)
    for key, value in unique_pairs.items():
        if len(value) >= 2 and gap_between_repetitions(value):
            return True
    return False

def gap_between_repetitions(value):
    for i in range(len(value)):
        for j in range(len(value)):
            if i != j:
                if abs(value[i] - value[j]) > 1:
                    return True
    return False


def generate_unique_pairs(word):
    pairs_db = {}
    for i in range(len(word) - 1):
        pair = word[i] + word[i + 1]
        if pair not in pairs_db:
            pairs_db[pair] = [i]
        else:
            pairs_db[pair].append(i)
    return pairs_db

def one_letter_in_between(word):
    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            return True
    return False

main()