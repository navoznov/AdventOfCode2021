import math

input = [int(x) for x in open("Day07/input.txt").read().split(',')]


def get_fuel_count(input, use_simple_calc_rules):

    min_pos, max_pos = min(input), max(input)

    def calc_fuel(input, position, use_simple_calc_rules):
        def calc_fuel_simple(start, end):
            return math.fabs(start - end)

        def calc_fuel_complex(start, end):
            count = math.fabs(start-end)
            return count * (1 + count) / 2

        if use_simple_calc_rules:
            return sum([calc_fuel_simple(x, position) for x in input])
        else:
            return sum([calc_fuel_complex(position, x) for x in input])

    min_fuel = None
    for pos in range(min_pos, max_pos):
        fuel = calc_fuel(input, pos, use_simple_calc_rules)
        if  min_fuel == None or fuel < min_fuel:
            min_fuel = fuel

    return min_fuel

# part 1
print(int(get_fuel_count(input, use_simple_calc_rules=True)))

# part 2
print(int(get_fuel_count(input, use_simple_calc_rules=False)))