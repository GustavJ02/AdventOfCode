
with open("input.txt", "r") as file:
    lines = file.readlines()

actions = []

for line in lines:
    input = line.strip()
    if input[0] == "L":
        action = -int(input[1:])
    elif input[0] == "R":
        action = int(input[1:])
    else:
        exit("Invalid input")
    actions.append(action)

dial = 50
count = 0

for action in actions:
    dial += action
    dial %= 100
    if dial == 0:
        count += 1

print("Password:", count)

dial = 50
count = 0

for action in actions:
    if action > 0:
        for _ in range(action):
            dial += 1
            dial %= 100
            if dial == 0:
                count += 1
    else:
        for _ in range(-action):
            dial -= 1
            dial %= 100
            if dial == 0:
                count += 1

print("Password 2:", count)