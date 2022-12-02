# Used dictionaries to handle possibilities
draw_sheet = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

win_sheet = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}

lose_sheet = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

# global score
score = 0


# uses dictionaries to determine "me" variable
def what_to_pick(opp, end_in):
    if end_in == "X":
        return lose_sheet[opp]

    if end_in == "Y":
        return draw_sheet[opp]

    if end_in == "Z":
        return win_sheet[opp]


# determine score to be added based on "me" variable
def choice_score(me):
    if me == "X":
        return 1

    if me == "Y":
        return 2

    if me == "Z":
        return 3

# determine score to be added based on if "me" won or lost


def end_score(end_in):
    if end_in == "X":
        return 0

    if end_in == "Y":
        return 3

    if end_in == "Z":
        return 6


with open('./input.txt', 'r') as input:
    for line in input:
        opponent = line.split()[0]
        end_in = line.split()[1]
        me = what_to_pick(opponent, end_in)

        score = score + choice_score(me)

        score = score + end_score(end_in)

print(score)
