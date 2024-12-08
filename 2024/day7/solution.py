from copy import deepcopy


def read_file(file):
    with open(file, "r") as f:
        file = f.readlines()
    return file


inp = read_file("input.txt")
# inp = read_file("sample.txt")
mapping = []
for i in inp:
    s = i.replace("\n", "").split(": ")
    ints = s[-1].split(" ")
    final_result = s[0]
    mapping.append((int(final_result), [int(x) for x in ints]))

cache = set()


def helper(data: list, solve_second_part: bool = False):
    data_copy = deepcopy(data)
    data_copy_2 = deepcopy(data)
    if len(data) == 1:
        cache.add(data[0])
        return
    if len(data) == 2:
        cache.add(data[0] * data[1])
        cache.add(data[0] + data[1])
        if solve_second_part:
            cache.add(int(f"{str(data[0])}{str(data[1])}"))
        return
    temp_plus = data[0] + data[1]
    data[0] = temp_plus
    del data[1]
    helper(data, solve_second_part)
    temp_mul = data_copy[0] * data_copy[1]
    data_copy[0] = temp_mul
    del data_copy[1]
    helper(data_copy, solve_second_part)
    if solve_second_part:
        temp_concat = int(f"{str(data_copy_2[0])}{str(data_copy_2[1])}")
        data_copy_2[0] = temp_concat
        del data_copy_2[1]
        helper(data_copy_2, solve_second_part)


sum = 0
for v in mapping:
    cache = set()
    helper(v[1], solve_second_part=True)
    if v[0] in cache:
        sum += v[0]

print(sum)
