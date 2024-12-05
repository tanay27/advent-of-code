with open("input.txt", "r") as f:
    input_txt = f.readlines()


list_1, list_2 = [], []

for x in input_txt:
    ints = x.replace("\n", "").split(" ")
    # print(ints)
    list_1.append(int(ints[0]))
    list_2.append(int(ints[-1]))


list_1.sort()
list_2.sort()

distance = 0
for x, y in zip(list_1, list_2):
    distance += abs(x - y)

print("---------------------")
print(f"Distance: {distance}")
print("---------------------")
print("similarity score:")


counter = {}

for num in list_2:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

similarity_score = 0

for num in list_1:
    similarity_score += num * counter.get(num, 0)

print(similarity_score)
print("---------------------")
