#with open("mini-input.txt", "r") as file:
with open("input.txt", "r") as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

ranges = []
id = None
for i in range(len(lines)):
    if len(lines[i]) == 0:
        id = i + 1
        break
    low = int(lines[i].split('-')[0])
    high = int(lines[i].split('-')[1])
    ranges.append((low, high))


def is_fresh(id):
    for low, high in ranges:
        if low <= id <= high:
            return True
    
    return False

count = 0
for i in lines[id:]:
    if is_fresh(int(i)):
        count += 1

print(f"Nr of fresh: {count}")

fresh_ids = set()
ranges = sorted(ranges, key=lambda item: item[0])

current_min = ranges[0][0]
current_max = ranges[0][1]
total = 0

for low, high in ranges[1:]:
    if low >= current_max + 1: # Disjoint ranges
        total += current_max - current_min + 1
        current_min = low
        current_max = high
    else:
        current_max = max(current_max, high)

total += current_max - current_min + 1

print(f"Nr of fresh ids: {total}")