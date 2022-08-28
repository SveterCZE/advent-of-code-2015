import math

def main():
    min_present_number = 33100000
    part1(min_present_number)
    part2(min_present_number)

def part1(min_present_number):
    house_number = 1
    while True:
        if count_gifts(house_number) >= min_present_number:
            print(house_number)
            break
        house_number +=1

def count_gifts(house_number):
    visiting_elfs = divisors(house_number)
    gift_count = int(sum(visiting_elfs) * 10)
    return gift_count

def divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    divs.extend([n])
    return list(set(divs))


def part2(min_present_number):
    house_number = 1
    while True:
        if count_gifts_part2(house_number) >= min_present_number:
            print(house_number)
            break
        house_number +=1

def count_gifts_part2(house_number):
    visiting_elfs = remove_over_50_visits(divisors(house_number), house_number)
    gift_count = int(sum(visiting_elfs) * 11)
    return gift_count

def remove_over_50_visits(list_of_elf_numbers, house_number):
    active_elves = []
    for elf in list_of_elf_numbers:
        if (house_number / elf) <= 50:
            active_elves.append(elf)
    return active_elves

main()