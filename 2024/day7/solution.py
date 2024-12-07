from itertools import combinations_with_replacement, permutations
from concurrent.futures import ThreadPoolExecutor
from typing import List
import time

start_time = time.time()


def read_file(file):
    with open(file, "r") as f:
        file = f.readlines()
    return file


inp = read_file("input.txt")
# inp = read_file("sample.txt")
mapping = {}
for i in inp:
    s = i.replace("\n", "").split(": ")
    ints = s[-1].split(" ")
    final_result = s[0]
    mapping[int(final_result)] = [int(x) for x in ints]

len_mapping = len(mapping)
print(f"Num of totals to  be processed: {len(mapping)}")


def generate_possible_combinations(num_of_elements: int) -> List:
    if num_of_elements == 2:
        return [["*"], ["+"]]
    stuff = ["*", "+"]
    cache = []
    for subset in combinations_with_replacement(stuff, num_of_elements - 1):
        for x in permutations(subset, num_of_elements - 1):
            if x not in cache:
                cache.append(x)
    return cache


def evaluate_expression(operator, value, total) -> bool:
    i = 0
    temp_total = 0
    if len(value) == 1:
        return value[0] == total
    if len(value) == 2:
        return value[i] * value[i + 1] == total
    if operator[0] == "*":
        temp_total = value[i] * value[i + 1]
        i += 2
    if operator[0] == "+":
        temp_total = value[i] + value[i + 1]
    i = 2
    while True:
        if i == len(value):
            break
        if operator[i - 1] == "*":
            temp_total *= value[i]
        if operator[i - 1] == "+":
            temp_total += value[i]
        i += 1
    return temp_total == total


def there_is_a_possible_combination(
    total: int, value: List, poss_combinations: List
) -> bool:
    print(total, value, len(value))
    for operator in poss_combinations:
        futures = []
        with ThreadPoolExecutor(4) as executor:
            futures.append(
                executor.submit(
                    evaluate_expression, operator=operator, value=value, total=total
                )
            )

        for a in futures:
            if a.result():
                return True

    return False


def part_1():
    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = []
        for total, value in mapping.items():
            poss_combinations = generate_possible_combinations(len(value))
            futures.append(
                [
                    total,
                    executor.submit(
                        there_is_a_possible_combination,
                        total=total,
                        value=value,
                        poss_combinations=poss_combinations,
                    ),
                ]
            )

    total = 0
    for a in futures:
        if a[1].result():
            total += a[0]

    print(total)


print(time.time() - start_time)
