
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
        total = sum(find_calibration_value(line.strip()) for line in reader)

    # Print the total calibration value
    print(total)


if __name__ == "__main__":
    main()
