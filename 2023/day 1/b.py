import re

# List of string representations for numbers
string_nums = ["one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine"]


def find_all_indexes(line: str, search: str):
    """Find all start indices of a substring in a line."""
    return [index.start() for index in re.finditer(pattern=search, string=line)]


def convert_to_numbers(line: str) -> dict:
    """
    Convert string representation of numbers to a dictionary of indices.
    Each index is associated with the corresponding numeric value.
    """
    # Use dictionary comprehension to map indices to numeric values
    # Enumerate with start=1 to match the numeric values in string_nums
    numeric_indices = {i: index for index, num in enumerate(
        string_nums, start=1) for i in find_all_indexes(line, num)}
    # Map digit indices to their numeric values
    numeric_indices |= {t: int(i) for t, i in enumerate(line) if i.isdigit()}
    return numeric_indices


def reconstruct(items: dict) -> str:
    """Reconstruct a string based on a dictionary of indices."""
    # Join the values corresponding to sorted keys
    return ''.join(str(items[key]) for key in sorted(items.keys()))


def find_calibration_value(line: str) -> int:
    """Find the calibration value in a given line."""
    # Find the first number forward
    forward_number = next(i for i in line if i.isdigit())

    # Find the first number backward
    backward_number = next(i for i in reversed(line) if i.isdigit())

    # Combine and return the concatenation of forward and backward numbers
    return int(forward_number + backward_number)


def main():
    # Accumulate the total calibration values from the input file
    with open("./input.txt", "r") as reader:
        # Use sum with a generator expression for concise accumulation
        total = sum(find_calibration_value(reconstruct(
            convert_to_numbers(line.strip()))) for line in reader)

    # Print the total calibration value
    print(total)


if __name__ == "__main__":
    main()
