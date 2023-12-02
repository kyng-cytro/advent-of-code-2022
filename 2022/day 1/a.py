elves = []

count = 0
elf = 1
with open('./input.txt', 'r') as input:
    line_list = input.readlines()

    for line in line_list:
        if line == '\n':
            elves.append(count)
            count = 0
            continue

        count = count + int(line)


print(elves.index(max(elves)), max(elves))
