#with open("mini-input.txt", "r") as file:
with open("input.txt", "r") as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = int(lines[i].split(',')[0]), int(lines[i].split(',')[1])

largest_area = 0
for x1, y1 in lines:
    for x2, y2 in lines:
        dx = x2 - x1 + 1
        dy = y2 - y1 + 1
        area = dy * dx
        if area > largest_area:
            largest_area = area

print(largest_area)

def ok(x1, x2, y1, y2):
    minx = min(x1, x2)
    maxx = max(x1, x2)
    miny = min(y1, y2)
    maxy = max(y1, y2)

    for a, b in zip(lines, lines[1:] + [lines[0]]):
        left = a[0] <= minx and b[0] <= minx
        right = a[0] >= maxx and b[0] >= maxx
        above = a[1] >= maxy and b[1] >= maxy
        below = a[1] <= miny and b[1] <= miny

        if not any([left, right, above, below]):
            return False
    
    return True


largest_area = 0
for x1, y1 in lines:
    for x2, y2 in lines:
        dx = abs(x2 - x1) + 1
        dy = abs(y2 - y1) + 1
        area = dy * dx
        if area > largest_area and ok(x1, x2, y1, y2):
            largest_area = area

print(largest_area)
