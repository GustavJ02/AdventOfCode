#with open("mini-input.txt", "r") as file:
with open("input.txt", "r") as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = list(lines[i])

beam_indexes = []
for i in range(len(lines[0])):
    if lines[0][i] == 'S':
        beam_indexes.append(i)
        break

count_split = 0

for i in range(1, len(lines)):
    for j in [x for x in beam_indexes]:
        if lines[i][j] == '.':
            lines[i][j] = '|'
        elif lines[i][j] == '^':
            count_split += 1
            lines[i][j-1] = '|'
            lines[i][j+1] = '|'
            beam_indexes.remove(j)
            beam_indexes.append(j-1)
            beam_indexes.append(j+1)
    beam_indexes = list(set(beam_indexes))

print(f"Nr of splits: {count_split}")

class Point:
    def __init__(self, char):
        self.char = char
        if char == '|':
            self.paths_here = 1
        else:
            self.paths_here = 0

    def __str__(self):
        if self.char == '|':
            return " " + str(self.paths_here) + " "
        return self.char

for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j] = Point(lines[i][j])

nr_of_paths = 1
for i in range(2, len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j].char == '|':
            ways_to_get_here = 0
            if j > 0 and lines[i][j-1].char == '^':
                ways_to_get_here += lines[i-1][j-1].paths_here
            if j < len(lines[i-1]) - 1 and lines[i][j+1].char == '^':
                ways_to_get_here += lines[i-1][j+1].paths_here
            ways_to_get_here += lines[i-1][j].paths_here
            lines[i][j].paths_here = ways_to_get_here

print(f"Nr of paths: {sum([point.paths_here for point in lines[-1] if point.char == '|'])}")