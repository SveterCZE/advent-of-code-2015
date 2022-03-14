import copy

def main():
    instructions = get_input()
    part1(instructions)
    part2(instructions)
    return 0

def get_input():
    f = open("input.txt", "r")
    flight_database = {}
    for line in f:
        split_line = line.split()
        dest1, dest2, distance = split_line[0], split_line[2], int(split_line[4])
        # Load first direction
        if dest1 not in flight_database:
            flight_database[dest1] = []
            flight_database[dest1].append((dest2, distance))
        else:
            flight_database[dest1].append((dest2, distance))
        # Load the other direction
        if dest2 not in flight_database:
            flight_database[dest2] = []
            flight_database[dest2].append((dest1, distance))
        else:
            flight_database[dest2].append((dest1, distance))
    return flight_database

def part1(instructions):
    dummy_journey = [None, 9999999]
    for elem in instructions:
        empty_journey = [[elem], 0]
        find_shortest_journey_recursive_helper(instructions, dummy_journey, empty_journey)
    print(dummy_journey[1])
    return 0 

def find_shortest_journey_recursive_helper(instructions, dummy_journey, journey):
    # BASE CASE --- Found a complete journey
    if len(journey[0]) == len(instructions):
        if journey[1] < dummy_journey[1]:
            dummy_journey[0] = journey[0]
            dummy_journey[1] = journey[1]
    # CASE 2 - The journey I found is already longer than the shortest I found - break
    if journey[1] > dummy_journey[1]:
        pass
    # CASE 3 - Add new journeys
    for elem in instructions[journey[0][-1]]:
        possible_dest = elem[0]
        distance = elem[1]
        if possible_dest not in journey[0]:
            new_journey = copy.deepcopy(journey)
            new_journey[0].append(possible_dest)
            new_journey[1] += distance
            find_shortest_journey_recursive_helper(instructions, dummy_journey, new_journey)

def part2(instructions):
    dummy_journey = [None, 0]
    for elem in instructions:
        empty_journey = [[elem], 0]
        find_longest_journey_recursive_helper(instructions, dummy_journey, empty_journey)
    print(dummy_journey[1])
    return 0

def find_longest_journey_recursive_helper(instructions, dummy_journey, journey):
    # BASE CASE --- Found a complete journey
    if len(journey[0]) == len(instructions):
        if journey[1] > dummy_journey[1]:
            dummy_journey[0] = journey[0]
            dummy_journey[1] = journey[1]
    # CASE 2 - Add new journeys
    for elem in instructions[journey[0][-1]]:
        possible_dest = elem[0]
        distance = elem[1]
        if possible_dest not in journey[0]:
            new_journey = copy.deepcopy(journey)
            new_journey[0].append(possible_dest)
            new_journey[1] += distance
            find_longest_journey_recursive_helper(instructions, dummy_journey, new_journey)

main()