DATA_MATRIX = []


def setup():
    """Read input file and populate the data matrix."""
    with open("./input.txt", "r") as reader:
        for line in reader.readlines():
            DATA_MATRIX.append(list(line.strip()))


def grab_full_number(item_index, data_index):
    """Retrieve the full number starting from the specified position with given steps."""
    number = []

    i = item_index

    while i >= 0:
        if str(DATA_MATRIX[data_index][i]).isdigit():
            number.insert(0, DATA_MATRIX[data_index][i])
            i -= 1
            continue

        break

    z = item_index + 1

    while z < len(DATA_MATRIX[data_index]):
        if str(DATA_MATRIX[data_index][z]).isdigit():
            number.append(DATA_MATRIX[data_index][z])
            z += 1
            continue

        break

    return (int(''.join(number)))


def find_adjacents(item_index, data_index):
    """Find adjacent numbers for the current position."""
    numbers = []

    left = DATA_MATRIX[data_index][item_index-1] if item_index != 0 else None

    if str(left).isdigit():
        numbers.append(grab_full_number(item_index-1, data_index))

    right = DATA_MATRIX[data_index][item_index +
                                    1] if item_index < (len(DATA_MATRIX[data_index]) - 1) else None

    if str(right).isdigit():
        numbers.append(grab_full_number(item_index+1, data_index))

    top = DATA_MATRIX[data_index - 1][item_index] if data_index != 0 else None

    if str(top).isdigit():
        numbers.append(grab_full_number(item_index, data_index - 1))

    else:
        top_left = DATA_MATRIX[data_index - 1][item_index -
                                               1] if data_index != 0 and item_index != 0 else None

        if str(top_left).isdigit():
            numbers.append(grab_full_number(item_index - 1, data_index - 1))

        top_right = DATA_MATRIX[data_index - 1][item_index +
                                                1] if data_index != 0 and item_index < (len(DATA_MATRIX[data_index]) - 1) else None

        if str(top_right).isdigit():
            numbers.append(grab_full_number(item_index + 1, data_index - 1))

    bottom = DATA_MATRIX[data_index +
                         1][item_index] if data_index < (len(DATA_MATRIX) - 1) else None

    if str(bottom).isdigit():
        numbers.append(grab_full_number(item_index, data_index + 1))

    else:
        bottom_left = DATA_MATRIX[data_index + 1][item_index -
                                                  1] if item_index != 0 and data_index < (len(DATA_MATRIX) - 1) else None

        if str(bottom_left).isdigit():
            numbers.append(grab_full_number(item_index - 1, data_index + 1))

        bottom_right = DATA_MATRIX[data_index + 1][item_index + 1] if data_index < (
            len(DATA_MATRIX) - 1) and item_index < (len(DATA_MATRIX[data_index]) - 1) else None

        if str(bottom_right).isdigit():
            numbers.append(grab_full_number(item_index + 1, data_index + 1))

    if len(numbers) != 2:
        return 0

    return numbers[0] * numbers[1]


def search_for_chars():
    """Search for '*' characters and calculate the product of adjacent numbers."""
    total = 0
    for data_index, data in enumerate(DATA_MATRIX):
        for item_index, item in enumerate(data):
            if item == '*':
                total += find_adjacents(item_index, data_index)

    print(total)


def main():
    """Main entry point."""
    setup()
    search_for_chars()


if __name__ == "__main__":
    main()
