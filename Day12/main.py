def parse_paths(lines):
    return [tuple(line.split("-")) for line in lines]


def is_small(cave: str):
    return cave == cave.lower()


def get_directions(paths, all_caves):
    directions = {cave: [] for cave in all_caves}
    for a, b in paths:
        directions[a].append(b)
        directions[b].append(a)

    return directions

def get_paths(path: list, small_caves_visits: list):
    paths = []
    current_cave = path[-1]
    current_directions = directions[current_cave]

    new_unused_small_caves_visits = small_caves_visits[:]
    if is_small(current_cave) and current_cave != START:
        new_unused_small_caves_visits.pop(new_unused_small_caves_visits.index(current_cave))

    for d in current_directions:
        if d == START:
            continue
        elif d == END:
            paths.append(path + [END])
        elif not is_small(d) or d in small_caves_visits:
            new_paths = get_paths(path + [d], new_unused_small_caves_visits)
            paths.extend(new_paths)

    return paths

lines = open("Day12/input.txt").read().split('\n')
START, END = "start", "end"
paths = parse_paths(lines)
all_caves = set([c for p in paths for c in p])
directions = get_directions(paths, all_caves)
small_caves = [c for c in all_caves if c not in [START, END] and is_small(c)]

# Part 1
paths = get_paths([START], small_caves)
distinct_paths = set([tuple(p) for p in paths])
print(len(distinct_paths))

# part 2
paths = []
for sc in small_caves:
    paths.extend(get_paths([START], small_caves + [sc]))

distinct_paths = set([tuple(p) for p in paths])
print(len(distinct_paths))