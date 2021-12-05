def parse(lines):
    def parse_coord(coord):
        return tuple([int(x) for x in coord.split(",")])

    result = []
    for line in lines:
        start, end = [parse_coord(coord) for coord in line.split(" -> ")]
        result.append((start, end))
    return result


def get_vent_delta(vent):
    def get_delta(c1, c2):
        if c1 == c2: return 0
        return 1 if c2 > c1 else -1

    (x1, y1), (x2, y2) = vent
    dx = get_delta(x1, x2)
    dy = get_delta(y1, y2)
    return (dx, dy)


def get_vent_points(vent):
    dx, dy = get_vent_delta(vent)
    (x, y), (x2, y2) = vent
    result = [(x, y)]
    while (x, y) != (x2, y2):
        x += dx
        y += dy
        result.append((x, y))
    return result


def is_diagonal_vent(vent):
    return len([1 for d in get_vent_delta(vent) if d != 0]) == 2


def mark_point(map, point):
    map[point] = map.get(point, 0) + 1


def mark_vents(map, use_diagonal):
    for vent in vents:
        if not use_diagonal and is_diagonal_vent(vent):
            continue

        points = get_vent_points(vent)
        for point in points:
            mark_point(map, point)
    return map

lines = open("Day05/input.txt").read().split('\n')
vents = parse(lines)

# part 1
map = dict()
mark_vents(map, use_diagonal=False)
print(len([1 for v in map.values() if v > 1]))

# part 2
map = dict()
mark_vents(map, use_diagonal=True)
print(len([1 for v in map.values() if v > 1]))