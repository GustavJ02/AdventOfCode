#with open("mini-input.txt", "r") as file:
with open("input.txt", "r") as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()
