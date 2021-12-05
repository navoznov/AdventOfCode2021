lines = open('Day02\input.txt').read().split('\n')

def parse_line(line):
    parts = line.split(" ")
    return (parts[0], int(parts[1]))

commands = [parse_line(line) for line in lines]
axises = { "forward": "x", "down": "z", "up": "z" }

# part 1
position_koefs = { "forward": 1, "down": 1, "up": -1 }
current_position = { "x": 0, "y": 0, "z": 0 }
for direction, delta in commands:
    axis = axises[direction]
    current_position[axis] += position_koefs[direction] * delta

print(current_position["x"] * current_position["z"])

# part 2
aim = 0
x=0
z=0
for direction, delta in commands:
    if direction == "forward":
        x += delta
        z += aim * delta
    elif direction == "up":
        aim -= delta
    elif direction == "down":
        aim += delta

print(x*z)