
DATA_MATRIX = []


def setup():
    """Read input file and populate the data matrix."""
    with open("./input.txt", "r") as reader:
        for line in reader.readlines():
            DATA_MATRIX.append(list(line.strip()))


def grab_full_number(cell, row):
    """Retrieve the full number starting from the specified position with given steps."""
    number = []

    i = cell

    # Check left side
    while i >= 0:
        if str(DATA_MATRIX[row][i]).isdigit():
            number.insert(0, DATA_MATRIX[row][i])
            i -= 1
            continue

        break

    z = cell + 1
    # Check right side
    while z < len(DATA_MATRIX[row]):
        if str(DATA_MATRIX[row][z]).isdigit():
            number.append(DATA_MATRIX[row][z])
            z += 1
            continue

        break

    return (int(''.join(number)))


def find_adjacents(cell, row):
    """Find adjacent numbers for the current position."""
    numbers = []

    left = DATA_MATRIX[row][cell-1] if cell != 0 else None

    if str(left).isdigit():
        numbers.append(grab_full_number(cell-1, row))

    right = DATA_MATRIX[row][cell +
                             1] if cell < (len(DATA_MATRIX[row]) - 1) else None

    if str(right).isdigit():
        numbers.append(grab_full_number(cell+1, row))

    top = DATA_MATRIX[row - 1][cell] if row != 0 else None

    if str(top).isdigit():
        numbers.append(grab_full_number(cell, row - 1))

    else:
        top_left = DATA_MATRIX[row - 1][cell -
                                        1] if row != 0 and cell != 0 else None

        if str(top_left).isdigit():
            numbers.append(grab_full_number(cell - 1, row - 1))

        top_right = DATA_MATRIX[row - 1][cell +
                                         1] if row != 0 and cell < (len(DATA_MATRIX[row]) - 1) else None

        if str(top_right).isdigit():
            numbers.append(grab_full_number(cell + 1, row - 1))

    bottom = DATA_MATRIX[row +
                         1][cell] if row < (len(DATA_MATRIX) - 1) else None

    if str(bottom).isdigit():
        numbers.append(grab_full_number(cell, row + 1))

    else:
        bottom_left = DATA_MATRIX[row + 1][cell -
                                           1] if cell != 0 and row < (len(DATA_MATRIX) - 1) else None

        if str(bottom_left).isdigit():
            numbers.append(grab_full_number(cell - 1, row + 1))

        bottom_right = DATA_MATRIX[row + 1][cell + 1] if row < (
            len(DATA_MATRIX) - 1) and cell < (len(DATA_MATRIX[row]) - 1) else None

        if str(bottom_right).isdigit():
            numbers.append(grab_full_number(cell + 1, row + 1))

    return numbers


def search_for_chars():
    """Search for  characters and calculate the sum of adjacent numbers."""
    total = 0
    for data_index, data in enumerate(DATA_MATRIX):
        for item_index, item in enumerate(data):
            if not item.isdigit() and item != '.':
                total += sum(find_adjacents(item_index, data_index))

    print(total)


def main():
    """Main entry point."""
    setup()
    search_for_chars()


if __name__ == "__main__":
    main()
