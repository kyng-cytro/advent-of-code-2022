count = 0

priorities = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def get_priority_number(letter):
    return priorities.index(letter) + 1


with open('./input.txt', 'r') as input:
    l = input.readlines()

    # TODO review this line
    groups = [l[x:x+3] for x in range(0, len(l), 3)]

    # FIXME try to avoid multiple for loops here
    for group in groups:
        for x in group[0]:
            if x in group[1] and x in group[2]:
                count = count + get_priority_number(x)
                break


print(count)
