def emulate(fishes, days):
    fishes_dict = dict.fromkeys(range(-1, 9), 0)
    for i in fishes_dict.keys():
        fishes_dict[i] = len([1 for fish in fishes if fish == i])

    days_counter = 0
    while days_counter != days:
        for i in range(9):
            fishes_dict[i-1] = fishes_dict[i]

        fishes_dict[8] = fishes_dict[-1]
        fishes_dict[6] = fishes_dict[6] + fishes_dict[-1]
        fishes_dict[-1] = 0

        days_counter += 1

    return fishes_dict

fishes = [int(x) for x in open("Day06/input.txt").read().split(',')]

# part 1
fishes_dict = emulate(fishes, 80)
print(sum(fishes_dict.values()))

# part 2

fishes_dict = emulate(fishes, 256)
print(sum(fishes_dict.values()))