from itertools import combinations

#with open("mini-input.txt", "r") as file:
with open("input.txt", "r") as file:
    machines = file.readlines()

def parse_btn(btn):
    btn = btn.strip('()')
    btn = tuple([int(el) for el in btn.split(',')])
    return btn

for i in range(len(machines)):
    machines[i] = machines[i].strip()
    spl = machines[i].split(' ')
    lights = list(spl[0].strip('[]'))
    btns = [parse_btn(btn) for btn in spl[1:-1]]
    joltage = [int(el) for el in spl[-1].strip('{}').split(',')]

    machines[i] = {
        "lights" : lights,
        "btns" : btns,
        "joltage" : joltage
    }
    print(machines[i])


def ok(pressed, lights):
    initial = list("." * len(lights))
    for btn in pressed:
        for i in btn:
            initial[i] = '.' if initial[i] == '#' else '#'
    
    for i in range(len(initial)):
        if initial[i] != lights[i]:
            return False
    return True


def check_machine(machine):
    for k in range(len(machine['btns'])):
        for comb in list(combinations(machine['btns'], k)):
            if ok(comb, machine['lights']):
                return k    


total = 0

for machine in machines:
    total += check_machine(machine)

print(f"Total: {total}")

import pulp
import numpy as np

def check_machine2(machine):
    l = len(machine['joltage'])
    x = []
    for btn in machine['btns']:
        btn_arr = [0] * l
        for i in btn:
            btn_arr[i] = 1
        x.append(btn_arr)

    x = np.array(x).T
    y = np.array(machine['joltage'])
    print(x)
    print(y)
    prob = pulp.LpProblem("IntegerLinearSystem", pulp.LpMinimize)

    s = [pulp.LpVariable(f"s_{i}", lowBound=0, upBound=None, cat="Integer")
         for i in range(x.shape[1])]
    
    prob += pulp.lpSum(s)

    for row in range(x.shape[0]):
        prob += pulp.lpSum(x[row, col] * s[col] for col in range(x.shape[1])) == y[row]

    prob.solve()

    return sum([v.value() for v in s])


total = 0

for machine in machines:
    total += check_machine2(machine)

print(f"Total: {total}")