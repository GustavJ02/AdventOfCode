with open("input.txt", "r") as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

def find_max_joltage(bank):
    found_max = 0
    for i in range(len(bank)):
        for ii in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[ii])
            if joltage > found_max:
                found_max = joltage
    
    return found_max

total_joltage = 0

for line in lines:
    total_joltage += find_max_joltage(line)

print(f"Max output: {total_joltage}")

def find_max_unsafe_joltage(bank):
    remove = len(bank) - 12
    stack = []

    for ch in bank:
        while remove > 0 and stack and stack[-1] < ch:
            stack.pop()
            remove -= 1
        stack.append(ch)

    result_str = ''.join(stack[:12])
    return int(result_str)

total_joltage = 0

for line in lines:
    total_joltage += find_max_unsafe_joltage(line)


print(f"Max unsafe output: {total_joltage}")