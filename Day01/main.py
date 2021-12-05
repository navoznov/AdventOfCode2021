lines = open('Day01\input.txt').read().split('\n')
measurements = [int(l) for l in lines]

def get_icreased_count(measurements) :
    counter = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            counter += 1
    return counter

# part 1
print(get_icreased_count(measurements))

# part 2
new_measurements = []
for i in range(len(measurements)-2):
    new_measurements.append(sum(measurements[i:i+3]))

print(get_icreased_count(new_measurements))
