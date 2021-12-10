import math

lines = open("Day08/input.txt").read().split('\n')


def parse(line):
    signals_str, output_str = line.split(" | ")
    return signals_str.split(" "), output_str.split(" ")


entries = [parse(line) for line in lines]
alphabet = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
}

# part 1
output_values = [ov for _, ov in entries]
counter1478 = 0

lens1478 = set([len(alphabet[digit]) for digit in [1, 4, 7, 8]])
for ov_list in output_values:
    counter1478 += len([1 for ov in ov_list if len(ov) in lens1478])

print(counter1478)

# part 2


def order_signal(signal):
    return "".join(sorted(signal))


assert (order_signal("bca") == "abc")


def order_signals(signals):
    return [order_signal(s) for s in signals]


def filter_by_length(signals, length):
    return [s for s in signals if len(s) == length]


def convert_digits_to_decimal_number(digits):
    digits = reversed(digits)
    return sum([d * 10**i for i, d in enumerate(digits)])


assert (convert_digits_to_decimal_number([1, 2, 3, 4]) == 1234)


def try_decode_outputs(outputs, map):
    map = {v: k for k, v in map.items()}
    decoded = [map.get(signal, None) for signal in outputs]
    return len([1 for x in decoded if x == None]) == 0, decoded


def decoded_signal_to_int(signal):
    digits = reversed(signal)
    return sum([d * (10**i) for i, d in enumerate(digits)])


assert (decoded_signal_to_int([1, 2, 3]) == 123)


def decode_signal(signals, outputs):
    lens1478 = {len(alphabet[digit]): digit for digit in [1, 4, 7, 8]}
    simple_map = dict()
    all_signals = list(set([order_signal(s) for s in signals + outputs]))
    pass
    for signal in all_signals:
        digit = lens1478.get(len(signal), None)
        if digit and not simple_map.get(digit, None):
            simple_map[digit] = signal
            is_decoded, decoded_signal = try_decode_outputs(
                outputs, simple_map)
            if is_decoded:
                return decoded_signal_to_int(decoded_signal)

    signal1 = set(simple_map[1])

    signal4 = set(simple_map.get(4, None))
    if not signal4:
        print("No 4")

    signal7 = set(simple_map.get(7, None))
    if not signal7:
        print("No 7")

    sixes = filter_by_length(signals + outputs, 6)
    for six in sixes:
        if 6 in simple_map and 9 in simple_map and 0 in simple_map:
            break

        if len(signal1 - set(six)) != 0:
            digit = 6
        elif len(signal4 - set(six)) != 0:
            digit = 0
        else:
            digit = 9

        simple_map[digit] = order_signal(six)

    is_decoded, decoded_signal = try_decode_outputs(outputs, simple_map)
    if is_decoded:
        return decoded_signal_to_int(decoded_signal)

    signal9 = set(simple_map.get(9, None))
    if not signal9:
        print("No 9")

    fives = filter_by_length(signals + outputs, 5)
    for five in fives:
        if 2 in simple_map and 3 in simple_map and 5 in simple_map:
            break

        digit = None
        if len(signal1 - set(five)) == 0:
            digit = 3
        elif len(set(five) - signal9) == 0:
            digit = 5
        else:
            digit = 2

        simple_map[digit] = order_signal(five)

    is_decoded, decoded_signal = try_decode_outputs(outputs, simple_map)
    return decoded_signal_to_int(decoded_signal) if is_decoded else None


decoded_signals = []
for signals, outputs in entries:
    signals, outputs = order_signals(signals), order_signals(outputs)
    decoded_signal = decode_signal(signals, outputs)
    decoded_signals.append(decoded_signal)

print(sum(decoded_signals))