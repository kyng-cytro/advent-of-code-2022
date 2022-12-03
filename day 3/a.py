count = 0

priorities = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def get_priority_number(letter):
    return priorities.index(letter) + 1


with open('./input.txt', 'r') as input:
    for line in input:
        n = len(line)

        comp1 = line[slice(0, n//2)]

        comp2 = line[slice(n//2, n)]

        for x in comp1:
            if x in comp2:
                count = count + get_priority_number(x)
                break

print(count)
