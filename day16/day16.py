def main():
    aunt_properties, all_aunts = get_input()
    part1(aunt_properties, all_aunts)
    part2(aunt_properties, all_aunts)
    return 0

def get_input():
    aunt_properties = get_aunt_properties()
    all_aunts = get_all_aunts()
    return aunt_properties, all_aunts

def get_aunt_properties():
    f = open("aunt-properties.txt", "r")
    aunt_properties = {}
    for line in f:
        split_line = line.strip().split()
        aunt_properties[split_line[0][:-1]] = int(split_line[1])
    return aunt_properties

def get_all_aunts():
    f = open("all-aunts.txt", "r")
    all_aunts = {}
    for line in f:
        split_line = line.strip().split()
        all_aunts[split_line[1][:-1]] = extract_aunt_data(split_line[2:])
    return all_aunts

def extract_aunt_data(aunt_data):
    aunt_properties = {}
    aunt_properties = extract_aunt_data_recursive(aunt_data, aunt_properties)
    return aunt_properties

def extract_aunt_data_recursive(aunt_data, aunt_properties):
    # BASE CASE - Len of aunt_data == 0
    if len(aunt_data) == 0:
        return aunt_properties
    # RECURSIVE CASE - data are to be processed
    else:
        aunt_properties[aunt_data[0][:-1]] = int(aunt_data[1].split(",")[0])
        return extract_aunt_data_recursive(aunt_data[2:], aunt_properties)

def part1(aunt_properties, all_aunts):
    for checked_aunt_no, checked_aunt_properties in all_aunts.items():
        if aunt_matches_description(aunt_properties, checked_aunt_properties):
            print(checked_aunt_no)

def aunt_matches_description(aunt_properties, checked_aunt):
    for key, value in aunt_properties.items():
        if key in checked_aunt:
            if value != checked_aunt[key]:
                return False
    return True

def part2(aunt_properties, all_aunts):
    for checked_aunt_no, checked_aunt_properties in all_aunts.items():
        if aunt_matches_description_new_rules(aunt_properties, checked_aunt_properties):
            print(checked_aunt_no)

def aunt_matches_description_new_rules(aunt_properties, checked_aunt):
    for key, value in aunt_properties.items():
        if key in checked_aunt:
            if "cats" in key or "trees" in key:
                if value >= checked_aunt[key]:
                    return False
            elif "pomeranians" in key or "goldfish" in key:
                if value <= checked_aunt[key]:
                    return False
            elif value != checked_aunt[key]:
                return False
    return True

main()