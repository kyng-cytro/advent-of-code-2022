def fully_contains(a, b):
    # TODO: study this line
    if (any(a[idx: idx + len(b)] == b
            for idx in range(len(a) - len(b) + 1))):
        return True
    return False


def format_range(line):
    p1 = line.replace('\n', '').split(',')[0]

    p2 = line.replace('\n', '').split(',')[1]

    range1 = range(int(p1.split('-')[0]), int(p1.split('-')[1]) + 1)

    range2 = range(int(p2.split('-')[0]), int(p2.split('-')[1]) + 1)

    return list(range1), list(range2)


count = 0

with open('input.txt', 'r') as input:
    for line in input:

        section1, section2 = format_range(line)

        if len(section1) == len(section2) or len(section1) > len(section2):
            if fully_contains(section1, section2):
                count = count + 1

        else:
            if fully_contains(section2, section1):
                count = count + 1

print(count)
