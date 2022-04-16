def main():
    instructions = get_input()
    part1(instructions)
    part2(instructions)
    return 0

def get_input():
    f = open("input.txt", "r")
    racers_properties = {}
    for line in f:
        split_line = line.strip().split()
        racers_properties[split_line[0]] = (int(split_line[3]), int(split_line[6]), int(split_line[-2]))
    return racers_properties

def part1(instructions):
    race_status = init_race_status(instructions)
    race_status = run_race(race_status, 2503, instructions)
    print(calculate_best_score(race_status))
    return 0


def part2(instructions):
    race_status = init_race_status(instructions)
    race_status = run_race_new_rules(race_status, 2503, instructions)
    print(calculate_best_score_new_rules(race_status))
    return 0

def init_race_status(instructions):
    race_status = {}
    for key, value in instructions.items():
        race_status[key] = [0, True, value[1], 0]
    return race_status

def run_race(race_status, race_len, racers_properties):
    for seconds_elapsed in range(race_len):
        for reindeer in race_status.keys():
            # Check if the reindeer moves
            if race_status[reindeer][1] == True:
                race_status[reindeer][0] += racers_properties[reindeer][0]
                race_status[reindeer][2] -= 1
                # If the reindeer ran out of steps - set it to resting mode
                if race_status[reindeer][2] == 0:
                    race_status[reindeer][1] = False
                    race_status[reindeer][2] = racers_properties[reindeer][2]
            else:
                race_status[reindeer][2] -= 1
                # If the reindeer rested - set it to racing mode
                if race_status[reindeer][2] == 0:
                    race_status[reindeer][1] = True
                    race_status[reindeer][2] = racers_properties[reindeer][1]
    return race_status

def run_race_new_rules(race_status, race_len, racers_properties):
    for seconds_elapsed in range(race_len):
        for reindeer in race_status.keys():
            # Check if the reindeer moves
            if race_status[reindeer][1] == True:
                race_status[reindeer][0] += racers_properties[reindeer][0]
                race_status[reindeer][2] -= 1
                # If the reindeer ran out of steps - set it to resting mode
                if race_status[reindeer][2] == 0:
                    race_status[reindeer][1] = False
                    race_status[reindeer][2] = racers_properties[reindeer][2]
            else:
                race_status[reindeer][2] -= 1
                # If the reindeer rested - set it to racing mode
                if race_status[reindeer][2] == 0:
                    race_status[reindeer][1] = True
                    race_status[reindeer][2] = racers_properties[reindeer][1]
        # Determine the leading reindeer
        best_current_distance = 0
        for reindeer, performance in race_status.items():
            if performance[0] > best_current_distance:
                best_current_distance = performance[0]
        for reindeer, performance in race_status.items():
            if race_status[reindeer][0] == best_current_distance:
                race_status[reindeer][3] += 1
    return race_status


def calculate_best_score(race_status):
    best_score = 0
    for reindeer in race_status.values():
        if reindeer[0] > best_score:
            best_score = reindeer[0]
    return(best_score)

def calculate_best_score_new_rules(race_status):
    best_score = 0
    for reindeer in race_status.values():
        if reindeer[3] > best_score:
            best_score = reindeer[3]
    return(best_score)

main()