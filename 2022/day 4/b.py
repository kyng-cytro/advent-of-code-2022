def format_range(line):
    p1 = line.replace('\n', '').split(',')[0]

    p2 = line.replace('\n', '').split(',')[1]

    range1 = range(int(p1.split('-')[0]), int(p1.split('-')[1]) + 1)

    range2 = range(int(p2.split('-')[0]), int(p2.split('-')[1]) + 1)

    return list(range1), list(range2)


def is_overlapping(section1, section2):
    if any(check in section1 for check in section2):
        return True
    return False


count = 0

with open('input.txt', 'r') as input:
    for line in input:

        section1, section2 = format_range(line)

        if is_overlapping(section1, section2):
            count = count + 1


print(count)
