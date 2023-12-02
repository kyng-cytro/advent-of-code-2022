score = 0

# add score if game ended as win


def did_i_win(me, opp):
    if me == "X" and opp == "C":
        return True

    if me == "Y" and opp == "A":
        return True

    if me == "Z" and opp == "B":
        return True


# add score if game ended as draw
def did_we_draw(me, opp):
    if me == "X" and opp == "A":
        return True

    if me == "Y" and opp == "B":
        return True

    if me == "Z" and opp == "C":
        return True


# determine score to be added based on "me" variable
def choice_score(me):
    if me == "X":
        return 1

    if me == "Y":
        return 2

    if me == "Z":
        return 3


with open('./input.txt', 'r') as input:
    for line in input:
        opponent = line.split()[0]
        me = line.split()[1]

        score = score + choice_score(me)

        if did_i_win(me, opponent):
            score = score + 6

        if did_we_draw(me, opponent):
            score = score + 3

print("Score:", score)
