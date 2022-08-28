from itertools import permutations, product, combinations

def main():
    equipment_stats = load_equipment_stats()
    boss_stats = load_boss_stats()
    part1(equipment_stats, boss_stats)
    part2(equipment_stats, boss_stats)
    return 0

def load_equipment_stats():
    equipment_stats = {}
    equipment_stats["weapons"] = generate_list_of_weapons()
    equipment_stats["armor"] =  generate_list_of_armor()
    equipment_stats["rings"] = generate_list_of_rings()
    return equipment_stats

def generate_list_of_weapons():
    f = open("weapons.txt", "r")
    weapons_list = []
    for line in f:
        weapons_list.append(line.split())
    return weapons_list

def generate_list_of_armor():
    f = open("armor.txt", "r")
    armor_list = []
    for line in f:
        armor_list.append(line.split())
    armor_list.append(["None", 0, 0, 0])
    return armor_list

def generate_list_of_rings():
    f = open("rings.txt", "r")
    rings_list = []
    for line in f:
        rings_list.append([line.split()[0]] + line.split()[2:])
    rings_list.append(["None", 0, 0, 0, 0])
    rings_list.append(["None", 0, 0, 0, 0])
    return rings_list

def load_boss_stats():
    f = open("input.txt", "r")
    boss_properties = []
    for line in f:
        boss_properties.append(int(line.split()[-1]))
    return boss_properties

def part1(equipment_stats, boss_stats):
    possible_equipment = generate_equipment_combinations(equipment_stats)
    for player_equipment in possible_equipment:
        if run_fight(player_equipment, boss_stats, boss_stats[0]) == True:
            print(player_equipment[0])
            break
    return 0

def part2(equipment_stats, boss_stats):
    possible_equipment = generate_equipment_combinations(equipment_stats)
    possible_equipment.sort(reverse=True)
    for player_equipment in possible_equipment:
        if run_fight(player_equipment, boss_stats, boss_stats[0]) == False:
            print(player_equipment[0])
            break
    return 0

def run_fight(selected_equipment, boss_stats, boss_HP):
    boss_attack = boss_stats[1]
    boss_defence = boss_stats[2]
    player_HP = 100
    player_attack = selected_equipment[1]
    player_defence = selected_equipment[2]

    player_impact = player_attack - boss_defence
    if player_impact < 1:
        player_impact = 1

    boss_impact = boss_attack - player_defence
    if boss_impact < 1:
        boss_impact = 1

    while True:
        # Player attacks
        boss_HP = boss_HP - player_impact
        if boss_HP <= 0:
            return True
        # Boss attacks
        player_HP = player_HP - boss_impact
        if player_HP <= 0:
            return False

def generate_equipment_combinations(equipment_stats):
    unsorted_equipment_combinations = []
    weapon_armor_combinations = product(equipment_stats["weapons"], equipment_stats["armor"])
    weapon_armor_combinations_list = []
    for elem in weapon_armor_combinations:
        weapon_armor_combinations_list.append(elem)

    rings_combinations = combinations(equipment_stats["rings"], 2)
    ring_combinations_list = []
    for elem in rings_combinations:
        ring_combinations_list.append(elem)

    for weapons_armor_combination in weapon_armor_combinations_list:
        for ring_combination in ring_combinations_list:
            combination_price = 0
            combination_damage = 0
            combination_armor = 0
            for elem in weapons_armor_combination:
                combination_price += int(elem[1])
                combination_damage += int(elem[2])
                combination_armor += int(elem[3])
            for elem in ring_combination:
                combination_price += int(elem[1])
                combination_damage += int(elem[2])
                combination_armor += int(elem[3])
            equipment_performance = (combination_price, combination_damage, combination_armor)
            unsorted_equipment_combinations.append(equipment_performance)
    unsorted_equipment_combinations.sort()
    return unsorted_equipment_combinations

main()