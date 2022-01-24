def main():
    instructions = get_input()
    part1(instructions)
    part2(instructions)
    return 0

def get_input():
    f = open("input.txt", "r")
    list_of_dimensions = []
    for line in f:
        list_of_dimensions.append(list(line.strip().split("x")))
    return list_of_dimensions

def part1(instructions):
    total_size = 0
    for elem in instructions:
        l = int(elem[0]) 
        w = int(elem[1])
        h = int(elem[2])
        total_size += (2*l*w + 2*w*h + 2*h*l)
        total_size += (min(l*w, w*h, h*l))
    print(total_size)
    return 0

def part2(instructions):
    total_length = 0
    for elem in instructions:
        l = int(elem[0]) 
        w = int(elem[1])
        h = int(elem[2])
        temp_sum = l+w+h
        temp_sum -= max(l, w, h)
        temp_sum *= 2
        total_length += temp_sum
        total_length += (l*w*h)
    print(total_length)
    return 0

main()
