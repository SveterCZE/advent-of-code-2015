from queue import PriorityQueue
import copy

def main():
    instructions = get_instructions()
    part1(instructions)
    part2(instructions)

def get_instructions():
    f = open("input.txt", "r")
    boss_stats = []
    for line in f:
        boss_stats.append(int(line.strip().split()[-1]))
    boss = {}
    boss["HP"] = boss_stats[0]
    boss["Damage"] = boss_stats[1]
    return boss

def part1(boss_stats):
    print(initialize_game(boss_stats, 1))
    return 0

def part2(boss_stats):
    print(initialize_game(boss_stats, 2))
    return 0

def initialize_game(boss_stats, level):
    game_state = generate_init_game_state(boss_stats)
    game_states_list = PriorityQueue()
    counter = {}
    counter["value"] = 0
    game_states_list.put((game_state["Mana_Spent"], counter["value"], game_state))
    counter["value"] += 1
    final_mana_spent = run_game_simulation(game_states_list, counter, level)
    return final_mana_spent

def run_game_simulation(game_states_list, counter, game_part):
    while True:
        # Remove the item with the lowest mana spent
        game_played = game_states_list.get()[2]
        # Apply all potential actions
        victory, mana_spent = apply_all_scenarios(game_played, game_states_list, counter, game_part)
        if victory == True:
            return mana_spent
        if game_states_list.qsize() == 0:
            return None

def apply_all_scenarios(game_played, game_states_list, counter, game_part):
    # Hard mode --- If playing the game_part2, decrease the player's health by 1
    if game_part == 2:
        game_played["Player_HP"] -= 1
        if player_alive(game_played) == False:
            return False, None
    
    # Apply the effects
    game_played = apply_effects(game_played)
    if is_victorious(game_played):
        return True, game_played["Mana_Spent"]

    # Check if at least missile can be cast
    if game_played["Player_Mana"] < 53:
        return False, None
    
    # Missile
    missile_outcome = apply_missile(copy.deepcopy(game_played))
    if is_victorious(missile_outcome):
        return True, missile_outcome["Mana_Spent"]
    missile_outcome = apply_boss_attack(missile_outcome)
    if is_victorious(missile_outcome):
        return True, missile_outcome["Mana_Spent"]
    if player_alive(missile_outcome) == True:
        game_states_list.put((missile_outcome["Mana_Spent"], counter["value"], missile_outcome))
        counter["value"] += 1
    
    # Drain
    if game_played["Player_Mana"] >= 73:
        drain_outcome = apply_drain(copy.deepcopy(game_played))
        if is_victorious(drain_outcome):
            return True, drain_outcome["Mana_Spent"]
        drain_outcome = apply_boss_attack(drain_outcome)
        if is_victorious(drain_outcome):
            return True, drain_outcome["Mana_Spent"]
        if player_alive(drain_outcome) == True: 
            game_states_list.put((drain_outcome["Mana_Spent"], counter["value"], drain_outcome))
            counter["value"] += 1

    # Shield
    if game_played["Player_Mana"] >= 113 and game_played["Shield_Duration"] <= 0:
        shield_outcome = apply_shield(copy.deepcopy(game_played))
        if is_victorious(shield_outcome):
            return True, shield_outcome["Mana_Spent"]
        shield_outcome = apply_boss_attack(shield_outcome)
        if is_victorious(shield_outcome):
            return True, shield_outcome["Mana_Spent"]
        if player_alive(shield_outcome) == True: 
            game_states_list.put((shield_outcome["Mana_Spent"], counter["value"], shield_outcome))
            counter["value"] += 1

    # Poison
    if game_played["Player_Mana"] >= 173 and game_played["Poison_Duration"] <= 0:
        poison_outcome = apply_poison(copy.deepcopy(game_played))
        if is_victorious(poison_outcome):
            return True, poison_outcome["Mana_Spent"]
        poison_outcome = apply_boss_attack(poison_outcome)
        if is_victorious(poison_outcome):
            return True, poison_outcome["Mana_Spent"]
        if player_alive(poison_outcome) == True:
            game_states_list.put((poison_outcome["Mana_Spent"], counter["value"], poison_outcome))
            counter["value"] += 1

    # Recharge
    if game_played["Player_Mana"] >= 229 and game_played["Recharge_Duration"] <= 0:
        recharge_outcome = apply_recharge(copy.deepcopy(game_played))
        if is_victorious(recharge_outcome):
            return True, recharge_outcome["Mana_Spent"]
        recharge_outcome = apply_boss_attack(recharge_outcome)
        if is_victorious(recharge_outcome):
            return True, recharge_outcome["Mana_Spent"]
        if player_alive(recharge_outcome) == True: 
            game_states_list.put((recharge_outcome["Mana_Spent"], counter["value"], recharge_outcome))
            counter["value"] += 1
    return False, None

def apply_boss_attack(checked_game_state):
    apply_effects(checked_game_state)
    boss_attack_strength = checked_game_state["Boss_Damage"] - checked_game_state["Player_Armor"]
    if boss_attack_strength < 1:
        boss_attack_strength == 1
    checked_game_state["Player_HP"] -= boss_attack_strength
    return checked_game_state


def is_victorious(checked_game_state):
    if checked_game_state["Boss_HP"] <= 0:
        return True
    else:
        return False

def apply_effects(checked_game_state):
    if checked_game_state["Shield_Duration"] >= 1:
        checked_game_state["Shield_Duration"] -= 1
        if checked_game_state["Shield_Duration"] == 0:
            checked_game_state["Player_Armor"] = 0

    if checked_game_state["Poison_Duration"] >= 1:
        checked_game_state["Boss_HP"] -= 3
        checked_game_state["Poison_Duration"] -= 1

    if checked_game_state["Recharge_Duration"] >= 1:
        checked_game_state["Player_Mana"] += 101
        checked_game_state["Recharge_Duration"] -= 1
    return checked_game_state

def apply_missile(checked_game_state):
    checked_game_state["Mana_Spent"] += 53
    checked_game_state["Player_Mana"] -= 53
    checked_game_state["Boss_HP"] -= 4
    return checked_game_state

def apply_drain(checked_game_state):
    checked_game_state["Mana_Spent"] += 73
    checked_game_state["Player_Mana"] -= 73
    checked_game_state["Player_HP"] += 2
    checked_game_state["Boss_HP"] -= 2
    return checked_game_state

def apply_shield(checked_game_state):
    checked_game_state["Mana_Spent"] += 113
    checked_game_state["Player_Mana"] -= 113
    checked_game_state["Shield_Duration"] = 6
    checked_game_state["Player_Armor"] = 7
    return checked_game_state

def apply_poison(checked_game_state):
    checked_game_state["Mana_Spent"] += 173
    checked_game_state["Player_Mana"] -= 173
    checked_game_state["Poison_Duration"] = 6
    return checked_game_state

def apply_recharge(checked_game_state):
    checked_game_state["Mana_Spent"] += 229
    checked_game_state["Player_Mana"] -= 229
    checked_game_state["Recharge_Duration"] = 5
    return checked_game_state

def player_alive(checked_game_state):
    if checked_game_state["Player_HP"] > 0:
        return True
    else:
        return False

def generate_init_game_state(boss_stats):
    game_state = {}
    game_state["Player_HP"] = 50
    game_state["Player_Mana"] = 500
    game_state["Player_Armor"] = 0
    game_state["Mana_Spent"] = 0
    game_state["Shield_Duration"] = 0
    game_state["Poison_Duration"] = 0
    game_state["Recharge_Duration"] = 0
    game_state["Boss_HP"] = boss_stats["HP"]
    game_state["Boss_Damage"] = boss_stats["Damage"]
    return(game_state)

main()