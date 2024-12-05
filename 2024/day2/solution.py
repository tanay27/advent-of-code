from copy import deepcopy

with open("input.txt", "r") as f:
    input_txt = f.readlines()


levels = []
for x in input_txt:
    ints = x.replace("\n", "").split(" ")
    level = [int(i) for i in ints]
    levels.append(level)


def calculate_diff(level: list) -> list:
    i, j = 0, 1
    diffs = []
    while j < len(level):
        diff = level[j] - level[i]
        diffs.append(diff)
        i += 1
        j += 1
    return diffs


def is_level_safe(diffs: list) -> bool:
    if diffs[0] == 0:
        return False
    elif diffs[0] < 0:
        for diff in diffs:
            if diff > 3 or diff < -3:
                return False
            if diff >= 0:
                return False
    elif diffs[0] > 0:
        for diff in diffs:
            if diff > 3 or diff < -3:
                return False
            if diff <= 0:
                return False
    return True


# part 1 evaluation
safe = 0
for level in levels:
    diffs = calculate_diff(level)
    if is_level_safe(diffs):
        safe += 1

print(safe)


# part 2 evaluation
safe_2 = 0
for level in levels:
    diffs = calculate_diff(level)
    if is_level_safe(diffs):
        safe_2 += 1
    else:
        for i in range(len(level)):
            level_copy = deepcopy(level)
            del level_copy[i]
            diff_level = calculate_diff(level_copy)
            if is_level_safe(diff_level):
                safe_2 += 1
                break

print("safe2:", safe_2)
