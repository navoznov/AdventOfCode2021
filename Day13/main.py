def parse(lines):
    dots = []
    for i, line in enumerate(lines):
        if len(line) == 0: break
        dots.append(tuple([int(x) for x in line.split(",")]))

    folding = []
    for line in lines[i + 1:]:
        direction, value = line.split(" ")[-1].split("=")
        folding.append((direction, int(value)))

    return dots, folding


def fold_1d(dot_coord, folding_line_coord):
    if dot_coord == folding_line_coord:
        return None
    elif dot_coord > folding_line_coord:
        return folding_line_coord - (dot_coord - folding_line_coord)
    else:
        return dot_coord


assert (fold_1d(7, 5) == 3)
assert (fold_1d(3, 5) == 3)


def fold_dot_along(dot, folding):
    folding_direction, folding_position = folding
    x, y = dot
    if folding_direction == "y":
        y = fold_1d(y, folding_position)
    else:
        x = fold_1d(x, folding_position)

    return None if x == None or y == None else (x, y)


assert (fold_dot_along((6, 0), ("x", 5)) == (4, 0))


def fold_all_dots_along(dots, folding):
    return set([fold_dot_along(d, folding) for d in dots]) - {None}


lines = open("Day13/input.txt").read().split('\n')
initial_dots, foldings = parse(lines)

# part 1
dots = set(initial_dots)
folding = foldings[0]
dots = fold_all_dots_along(dots, folding)
print(len(dots))

# part 2
dots = set(initial_dots)

for f in foldings:
    dots = fold_all_dots_along(dots, f)

max_x = max([x for x, _ in dots]) + 1
max_y = max([y for _, y in dots]) + 1

for i in range(max_y):
    xs = [x for x, y in dots if y == i]
    chars = ["."] * max_x
    for x in xs:
        chars[x] = "#"

    print("".join(chars))
