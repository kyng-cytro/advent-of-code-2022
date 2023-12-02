# defined stacks to make things easier
stacks = [
    ['B', 'V', 'W', 'T', 'Q', 'N', 'H', 'D'],
    ['B', 'W', 'D'],
    ['C', 'J', 'W', 'Q', 'S', 'T'],
    ['P', 'T', 'Z', 'N', 'R', 'J', 'F'],
    ['T', 'S', 'M', 'J', 'V', 'P', 'G'],
    ['N', 'T', 'F', 'W', 'B'],
    ['N', 'V', 'H', 'F', 'Q', 'D', 'L', 'B'],
    ['R', 'F', 'P', 'H'],
    ['H', 'P', 'N', 'L', 'B', 'M', 'S', 'Z']
]

# for later
firsts = []

with open('./input.txt', 'r') as input:
    for line in input:

        procedure = line.strip()

        creates_to_move = int(procedure.split(' ')[1])
        from_stack = int(procedure.split(' ')[3]) - 1
        to_stack = int(procedure.split(' ')[-1]) - 1

        new_stack = stacks

        # looping to the number of creates we need to move
        for i in range(creates_to_move):
            # moving the first create in the from_stack
            new_stack[to_stack].insert(0, (new_stack[from_stack][0]))

            # removing the create we just moved from the from_stack
            new_stack[from_stack].pop(0)

        # setting stacks and moving on
        stacks = new_stack

# getting the first of each stack
for stack in stacks:
    firsts.append(stack[0])

# output
print(''.join(firsts))
