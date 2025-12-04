#with open("mini-input.txt", "r") as file:
with open("input.txt", "r") as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

diagram = [list(line) for line in lines]

def count_neighbours(diagram, x, y):
    count = 0
    for i in [x - 1, x, x + 1]:
        for j in [y - 1, y, y + 1]:
            if i == x and j == y:
                continue
            if i in range(len(diagram)):
                if j in range(len(diagram[i])):
                    if diagram[i][j] == '@':
                        count += 1
    
    return count

def find_accessable(diagram, removeable):
    accessable = 0
    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            if diagram[i][j] == '@':
                neighbours = count_neighbours(diagram, i, j)
                if neighbours < 4:
                    accessable += 1
                    removeable.append((i, j))
    
    return accessable

removeable = []
accessable = find_accessable(diagram, removeable)
print(f"Accessable: {accessable}")

def remove(diagram, removeable):
    count = 0
    for i, j in removeable:
        diagram[i][j] = '.'
        count += 1
    
    return count

total_removed = 0
while True:
    removeabl1e = []
    accessable = find_accessable(diagram, removeable)
    print(f"Can remove {accessable}")
    if accessable == 0:
        break

    remove(diagram, removeable)
    total_removed += accessable


print(f"Removeable: {total_removed}")
