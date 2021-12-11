def init_state(lines):
    return [[int(x) for x in line] for line in lines]


def get_deltas(map, x, y):
    x_size = len(map[0])
    xs = [0]
    if x > 0: xs.append(-1)
    if x < x_size - 1: xs.append(1)

    ys = [0]
    if y > 0: ys.append(-1)
    y_size = len(map)
    if y < y_size - 1: ys.append(1)

    deltas = [(x, y) for x in xs for y in ys]
    deltas = [d for d in deltas if d != (0, 0)]
    return deltas


def flash(state, x, y):
    state[y][x] = 0
    deltas = get_deltas(state, x, y)
    for dx, dy in deltas:
        nx, ny = x + dx, y + dy
        if state[ny][nx] > 0:
            state[ny][nx] += 1

    return state


def process_point(state, x, y):
    if state[y][x] > 9:
        is_flash = True
        state = flash(state, x, y)
    else:
        is_flash = False

    return state, is_flash


def make_step(state):
    for y in range(len(state)):
        for x in range(len(state[y])):
            state[y][x] += 1

    flash_count = 0
    while True:
        current_flash_count = flash_count
        for y in range(len(state)):
            for x in range(len(state[y])):
                state, is_flash = process_point(state, x, y)
                if is_flash:
                    flash_count += 1

        if current_flash_count == flash_count:
            break

    return state, flash_count


lines = open("Day11/input.txt").read().split('\n')

# part 1
state = init_state(lines)
flash_count = 0
steps_count = 100
for si in range(steps_count):
    state, fc = make_step(state)
    flash_count += fc

print(flash_count)

# part 2
state = init_state(lines)
octopus_count = len(state) * len(state[0])
step_counter = 0
while True:
    step_counter += 1
    state, flash_count = make_step(state)

    if flash_count == octopus_count:
        break

print(step_counter)