def parse_line(line):
    parts = line.split(" ")
    return (parts[0], int(parts[1]))

def get_nth_bit(number, n):
    return number >> n & 1

lines = open('Day03\input.txt').read().split('\n')
numbers = [int(l, 2) for l in lines]
max_level = len(lines[0])

# part 1
def get_rate_bits(numbers, level):
    zeros_count = len([n for n in numbers if get_nth_bit(n, level) == 0])
    ones_count = len(numbers) - zeros_count
    return (1 if ones_count >zeros_count else 0, 1 if ones_count <= zeros_count else 0)

gamma_rate = 0
epsilon_rate = 0
for level in range(max_level):
    gamma_rate_bit, epsilon_rate_bit = get_rate_bits(numbers, level)
    gamma_rate += gamma_rate_bit * (2 ** level)
    epsilon_rate += epsilon_rate_bit * (2 ** level)

print(gamma_rate*epsilon_rate)

# part 2

def get_last_bits(numbers, level):
    number = numbers[0]
    end = ""
    return "".join([str(get_nth_bit(number, x)) for x in range(level+1)])[::-1]

def get_o2(numbers, max_level):
    o2 = ""
    for level in range(max_level-1, -1, -1):
        if len(numbers) == 1:
            o2 += get_last_bits(numbers, level)
            break
        zeros_count = len([n for n in numbers if get_nth_bit(n, level) == 0])
        ones_count = len(numbers) - zeros_count
        bit = 0 if zeros_count > ones_count else 1
        o2 += str(bit)
        numbers = [number for number in numbers if get_nth_bit(number, level) == bit]
    return int(o2, 2)

def get_co2(numbers, max_level):
    co2 = ""
    for level in range(max_level-1, -1, -1):
        if len(numbers) == 1:
            a = get_last_bits(numbers, level)
            co2 += str(a)
            break

        zeros_count = len([n for n in numbers if get_nth_bit(n, level) == 0])
        ones_count = len(numbers) - zeros_count

        bit = 0 if zeros_count <= ones_count else 1
        co2 += str(bit)
        new = [n for n in numbers if get_nth_bit(n, level) == bit]
        numbers = new
    return int(co2, 2)

o2 = get_o2(numbers[:], max_level)
co2 = get_co2(numbers[:], max_level)
print(o2*co2)
