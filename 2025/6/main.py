import math

#with open("mini-input.txt", "r") as file:
with open("input.txt", "r") as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

    lines[i] = [e for e in lines[i].split(' ') if e]

summ = 0

for j in range(len(lines[0])):
    elems = []
    for i in range(len(lines)):
        elems.append(int(lines[i][j]) if lines[i][j].isdigit() else lines[i][j])
    
    if elems[-1] == '*':
        summ += math.prod(elems[:-1])
    elif elems[-1] == '+':
        summ += sum(elems[:-1])


print(f"Sum is: {summ}")

#with open("mini-input.txt", "r") as file:
with open("input.txt", "r") as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

operations = [e for e in lines[-1].split(' ') if e]

operands = [[]]
x = 0
tmp_nr = ''
for j in range(len(lines[0])):
    for i in range(len(lines) - 1):
        tmp_nr += lines[i][j]
    if tmp_nr.strip():
        operands[x].append(int(tmp_nr))
    else:
        operands.append([])
        x += 1
    tmp_nr = ''

summ = 0
x = 0
for i in range(len(operations)):
    if operations[i] == '*':
        print(operands[x], end=" (*) : ")
        summ += math.prod(operands[x])
        print(math.prod(operands[x]))
    elif operations[i] == '+':
        print(operands[x], end=" (+) : ")
        summ += sum(operands[x])
        print(sum(operands[x]))
    x += 1

print(f"Sum is: {summ}")