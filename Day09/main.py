import math
import numpy as np

lines = open("Day09/input.txt").read().split('\n')
map = [[int(x) for x in line] for line in lines]


def add_border(map, border_value):
    x_size = len(map[0])
    map = np.array(map)
    row = np.array([border_value] * x_size)
    map = np.append(map, [row], 0)
    map = np.insert(map, 0, [row], 0)
    map = map.tolist()
    for i, row in enumerate(map):
        map[i] = row + [border_value]
        map[i].insert(0, border_value)
    return map


def get_map_point(map, point, delta):
    x, y = point
    dx, dy = delta if delta else (0, 0)
    return map[y + dy][x + dx]


def is_lowest(map, x, y):
    deltas = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    current_value = map[y][x]
    for dx, dy in deltas:
        if current_value >= map[y + dy][x + dx]:
            return False

    return True


def get_lowest_points(map):
    result = []

    x_size = len(map[0])
    y_size = len(map)
    for y in range(1, y_size - 1):
        for x in range(1, x_size - 1):
            if is_lowest(map, x, y):
                result.append((x, y))

    return result


bordered_map = add_border(map, 42)
lowest_points = get_lowest_points(bordered_map)

# part 1

risk_levels = [bordered_map[y][x] + 1 for x, y in lowest_points]
print(sum(risk_levels))

#part 2

pass
