from typing import Tuple


def read_file(filename) -> list:
    with open(filename, "r") as f:
        file = f.readlines()
    return file


order = read_file("input_ordering.txt")
# order = read_file("sample_ordering.txt")
updated = read_file("input_page_update.txt")
# updated = read_file("sample_update.txt")

ordering = {}
for a in order:
    el = a.replace(" ", "").replace("\n", "").split("|")
    if el[0] in ordering:
        ordering[el[0]].append(el[1])
    else:
        ordering[el[0]] = [el[1]]

updates = []

for up in updated:
    el = up.replace(" ", "").replace("\n", "").split(",")
    updates.append(el)

num_reordered = 0


def ordering_respect(arr: list) -> bool:
    global num_reordered
    if len(arr) == 1:
        return True
    for i in range(len(arr)):
        if ordering.get(arr[i], ""):
            for num in ordering[arr[i]]:
                for j, _num in enumerate(arr[:i]):
                    if _num == num:
                        num_reordered += 1
                        return False
    return True


def middle_num(arr: list) -> int:
    if len(arr) == 1:
        return 0
    if len(arr) > 1 and len(arr) % 2 != 0:
        return int(arr[len(arr) // 2])
    else:
        print("even")
    return int("0")


def part1():
    total = 0
    for arr in updates:
        temp = ordering_respect(arr)
        if temp:
            middle_number = middle_num(arr)
            total += middle_number
    print(f"part1: {total}, num_reordered: {num_reordered}")


# part2

num_reordered_2 = 0


def ordering_respect_part2(arr: list) -> Tuple[list, bool]:
    global num_reordered_2
    if len(arr) == 1:
        return arr, False
    reordered = False
    len_arr = len(arr)
    while not ordering_respect(arr):
        for i in range(len_arr):
            if ordering.get(arr[i], ""):
                for num in ordering[arr[i]]:
                    for j, _num in enumerate(arr[:i]):
                        if _num == num:
                            num_reordered_2 += 1
                            arr[i], arr[j] = arr[j], arr[i]
                            reordered = True
    return arr, reordered


def part2():
    total_part2 = 0
    for arr in updates:
        temp_arr, temp = ordering_respect_part2(arr)
        if temp:
            middle_number = middle_num(temp_arr)
            total_part2 += middle_number
    print(f"part2: {total_part2}, num_reordered: {num_reordered_2}")


part2()
# part1()
