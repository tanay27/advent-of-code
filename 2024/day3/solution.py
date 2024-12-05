import re

with open("input.txt", "r") as f:
    input_string = f.read()


def mul(input_string: str):
    pattern = r"mul\(([1-9]\d{0,2}),([1-9]\d{0,2})\)"

    matches = re.findall(pattern, input_string)

    total = 0
    for match in matches:
        num1, num2 = map(int, match)
        product = num1 * num2
        total += product
    return total


# part 1
print(mul(input_string))

# part 2
# split string by dont, all the strings some part is definitely to be ignored
dont = "don't()"
do = "do()"
input_split_dont = input_string.split(dont)
final_list = [input_split_dont[0]]
del input_split_dont[0]

for sentence in input_split_dont:
    sentence_split_do = sentence.split(do)
    del sentence_split_do[0]
    final_list.extend(sentence_split_do)
total = 0
for sentence in final_list:
    total += mul(sentence)

print(total)
