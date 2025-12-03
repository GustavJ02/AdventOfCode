
with open("input.txt", "r") as file:
    lines = file.readline()

ranges = lines.split(",")

range_tpls = []

for r in ranges:
    low, high = r.split("-")
    range_tpls.append((int(low), int(high)))

s = 0
for low, high in range_tpls:
    for i in range(low, high + 1):
        candidate = str(i)
        length = len(candidate)
        if length % 2 != 0:
            continue
        mid = length // 2
        if candidate[0:mid] == candidate[mid:]:
            s += i

print(f"Sum of invalid ids: {s}")

def is_invalid(id):
    for i in range(1, len(id) // 2 + 1):
        nr_of_reps = len(id) // i
        ptrn_rep_str = id[0:i] * nr_of_reps

        if ptrn_rep_str == id:
            return True
    return False

s = 0
for low, high in range_tpls:
    for i in range(low, high + 1):
        candidate = str(i)
        if is_invalid(candidate):
            s += i

print(f"Sum of invalid ids: {s}")
