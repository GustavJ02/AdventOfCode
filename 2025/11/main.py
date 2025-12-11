#with open("mini-input.txt", "r") as file:
with open("input.txt", "r") as file:
    lines = file.readlines()

points = {}

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    key = lines[i].split(':')[0]
    values = lines[i].split(':')[1].split()
    points[key] = values

def find_out(point):
    if point == 'out':
        return 1
    if points[point]:
        return sum([find_out(p) for p in points[point]])
    else:
        return 0
    
print(f"Sum: {find_out('you')}")

from functools import lru_cache

@lru_cache(maxsize=None)
def find_out_2(point, fft, dac):
    if point == 'out':
        return 1 if (fft and dac) else 0

    if point == 'fft':
        fft = True
    if point == 'dac':
        dac = True

    if points.get(point):
        return sum(find_out_2(p, fft, dac) for p in points[point])
    else:
        return 0

print(f"Sum: {find_out_2('svr', False, False)}")