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


def get_paths(path: list, unused_small_caves: set):
    paths = []
    current_cave = path[-1]
    current_directions = directions[current_cave]
    new_unused_small_caves = unused_small_caves - {current_cave}
    for d in current_directions:
        if d == START:
            continue
        elif d == END:
            paths.append(path + [END])
        elif not is_small(d) or d in unused_small_caves:
            new_paths = get_paths(path + [d], new_unused_small_caves)
            paths.extend(new_paths)

    return paths


lines = open("Day12/input.txt").read().split('\n')
START, END = "start", "end"
paths = parse_paths(lines)
all_caves = set([c for p in paths for c in p])
directions = get_directions(paths, all_caves)
all_small_caves = {c for c in all_caves if c not in [START, END] and is_small(c)}

# Part 1
paths = get_paths([START], all_small_caves)
real_paths = set([tuple(p) for p in paths if p[0] == START and p[-1] == END])
print(len(real_paths))
pass