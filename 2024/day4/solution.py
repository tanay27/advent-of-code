with open("input.txt", "r") as f:
    input_txt = f.readlines()


total_columns = len(input_txt[0])
total_rows = len(input_txt)
print(f"total_columns: {total_columns}, total_rows: {total_rows}")


def num_of_xmas_in_neighborhood(row, col) -> int:
    total = 0
    for direction in [
        "north",
        "south",
        "east",
        "west",
        "southeast",
        "northeast",
        "northwest",
        "southwest",
    ]:
        if is_xmas(direction, row, col):
            total += 1
    return total


def num_of_x_mas_in_neighborhood(row, col) -> int:
    total = 0
    if is_mas("left_right", row, col) and is_mas("right_left", row, col):
        total += 1
    return total


def is_mas(direction, row, col) -> bool:
    try:
        if (
            row - 1 >= 0
            and row + 1 < total_rows
            and col - 1 >= 0
            and col + 1 < total_columns
        ):
            if direction == "left_right" and (
                (
                    input_txt[row - 1][col - 1] == "M"
                    and input_txt[row + 1][col + 1] == "S"
                )
                or (
                    input_txt[row - 1][col - 1] == "S"
                    and input_txt[row + 1][col + 1] == "M"
                )
            ):
                return True
            if direction == "right_left" and (
                (
                    input_txt[row - 1][col + 1] == "M"
                    and input_txt[row + 1][col - 1] == "S"
                )
                or (
                    input_txt[row - 1][col + 1] == "S"
                    and input_txt[row + 1][col - 1] == "M"
                )
            ):
                return True
    except Exception as e:
        print(e, row, col)

    return False


def is_xmas(direction, row, col) -> bool:
    try:
        if (
            direction == "north"
            and row - 3 >= 0
            and input_txt[row - 1][col] == "M"
            and input_txt[row - 2][col] == "A"
            and input_txt[row - 3][col] == "S"
        ):
            return True
        if (
            direction == "south"
            and row + 3 < total_rows
            and input_txt[row + 1][col] == "M"
            and input_txt[row + 2][col] == "A"
            and input_txt[row + 3][col] == "S"
        ):
            return True
        if (
            direction == "east"
            and col + 3 < total_columns
            and input_txt[row][col + 1] == "M"
            and input_txt[row][col + 2] == "A"
            and input_txt[row][col + 3] == "S"
        ):
            return True
        if (
            direction == "west"
            and col - 3 >= 0
            and input_txt[row][col - 1] == "M"
            and input_txt[row][col - 2] == "A"
            and input_txt[row][col - 3] == "S"
        ):
            return True
        if (
            direction == "northeast"
            and row - 3 >= 0
            and col + 3 < total_columns
            and input_txt[row - 1][col + 1] == "M"
            and input_txt[row - 2][col + 2] == "A"
            and input_txt[row - 3][col + 3] == "S"
        ):
            return True
        if (
            direction == "northwest"
            and row - 3 >= 0
            and col - 3 >= 0
            and input_txt[row - 1][col - 1] == "M"
            and input_txt[row - 2][col - 2] == "A"
            and input_txt[row - 3][col - 3] == "S"
        ):
            return True
        if (
            direction == "southeast"
            and row + 3 < total_rows
            and col + 3 < total_columns
            and input_txt[row + 1][col + 1] == "M"
            and input_txt[row + 2][col + 2] == "A"
            and input_txt[row + 3][col + 3] == "S"
        ):
            return True
        if (
            direction == "southwest"
            and row + 3 < total_rows
            and col - 3 >= 0
            and input_txt[row + 1][col - 1] == "M"
            and input_txt[row + 2][col - 2] == "A"
            and input_txt[row + 3][col - 3] == "S"
        ):
            return True
    except Exception as e:
        print(e)
    return False


# part 1
def part1():
    total = 0
    for row in range(len(input_txt)):
        for col in range(len(input_txt[row])):
            if input_txt[row][col] == "X":
                # travel around +3 and check XMAS
                total += num_of_xmas_in_neighborhood(row, col)
    return total


# part 2
def part2():
    total = 0
    for row in range(len(input_txt)):
        for col in range(len(input_txt[row])):
            if input_txt[row][col] == "A":
                # travel around +3 and check XMAS
                total_temp = num_of_x_mas_in_neighborhood(row, col)
                total += total_temp
    return total


part1()
part2()
