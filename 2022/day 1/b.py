elves = []
count = 0
with open('./input.txt', 'r') as input:
    line_list = input.readlines()

    for line in line_list:
        if line == '\n':
            elves.append(count)
            count = 0
            continue

        count = count + int(line)


top = []

for _ in range(3):
    top.append(max(elves))
    elves.remove(max(elves))

print(sum(top))
