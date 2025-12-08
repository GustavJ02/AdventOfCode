import math

#with open("mini-input.txt", "r") as file:
with open("input.txt", "r") as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = int(lines[i].split(',')[0]), int(lines[i].split(',')[1]), int(lines[i].split(',')[2])
    #print(lines[i])

def distance(a, b):
    s = 0
    for i in range(len(a)):
        s += (a[i] - b[i])**2
    return math.sqrt(s)

distances = []

for i in range(len(lines)):
    for j in range(i, len(lines)):
        if i != j:
            distances.append(
                (
                    i,
                    j,
                    distance(lines[i], lines[j])
                )
            )

distances = sorted(distances, key=lambda x: x[2])

circuits = []

for i in range(1000):
    a, b, d = distances[i]
    circ_a = None
    circ_b = None
    for i in range(len(circuits)):
        if a in circuits[i]:
            circ_a = i
        if b in circuits[i]:
            circ_b = i
    if circ_a is None and circ_b is None:
        circuits.append(set([a, b]))
    elif circ_a is None:
        circuits[circ_b].add(a)
    elif circ_b is None:
        circuits[circ_a].add(b)
    elif circ_a != circ_b:
        circuits[circ_a].update(circuits[circ_b])
        circuits.pop(circ_b)
    
for i in range(len(circuits)):
    circuits[i] = len(circuits[i])

largest_circ = sorted(circuits, reverse=True)[:3]
print(f"Result: {math.prod(largest_circ)}")

circuits = []

last_added_xs = (None, None)

for a, b, d in distances:
    circ_a = None
    circ_b = None
    for i in range(len(circuits)):
        if a in circuits[i]:
            circ_a = i
        if b in circuits[i]:
            circ_b = i
    if circ_a is None and circ_b is None:
        last_added_xs = lines[a][0], lines[b][0]
        circuits.append(set([a, b]))
    elif circ_a is None:
        last_added_xs = lines[a][0], lines[b][0]
        circuits[circ_b].add(a)
    elif circ_b is None:
        last_added_xs = lines[a][0], lines[b][0]
        circuits[circ_a].add(b)
    elif circ_a != circ_b:
        last_added_xs = lines[a][0], lines[b][0]
        circuits[circ_a].update(circuits[circ_b])
        circuits.pop(circ_b)

    if len(circuits) == 1 and len(circuits[0]) == len(lines):
        break

print(f"Result: {last_added_xs[0] * last_added_xs[1]}")

