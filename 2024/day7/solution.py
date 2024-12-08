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


def fork_data(temp, data):
    s = [temp]
    for a in data:
        s.append(a)
    return s


def helper(data: list, solve_second_part: bool = False):
    if len(data) == 1:
        cache.add(data[0])
        return
    if len(data) == 2:
        cache.add(data[0] * data[1])
        cache.add(data[0] + data[1])
        if solve_second_part:
            cache.add(int(f"{str(data[0])}{str(data[1])}"))
        return
    helper(fork_data(data[0] + data[1], data[2:]), solve_second_part)
    helper(fork_data(data[0] * data[1], data[2:]), solve_second_part)
    if solve_second_part:
        helper(
            fork_data(int(f"{str(data[0])}{str(data[1])}"), data[2:]), solve_second_part
        )


sum = 0
for v in mapping:
    cache = set()
    helper(v[1], solve_second_part=False)
    if v[0] in cache:
        sum += v[0]

print(sum)
