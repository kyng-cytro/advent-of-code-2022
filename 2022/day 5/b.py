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

firsts = []

with open('./input.txt', 'r') as input:
    for line in input:

        procedure = line.strip()

        creates_to_move = int(procedure.split(' ')[1])
        from_stack = int(procedure.split(' ')[3]) - 1
        to_stack = int(procedure.split(' ')[-1]) - 1

        new_stack = stacks

        # do this if only moving one create
        if creates_to_move == 1:
            for i in range(creates_to_move):
                new_stack[to_stack].insert(0, (new_stack[from_stack][0]))
                new_stack[from_stack].pop(0)

        # when moving more than one create we want to make sure it lands in the same order
        else:
            # looping from 1 to creates_to_move + 1 because i need to use i
            for i in range(1, creates_to_move + 1):
                # adding the create at the bottom of the ones we have to move first using i
                new_stack[to_stack].insert(
                    0, new_stack[from_stack][creates_to_move - i])
                # removing the create we just moved
                new_stack[from_stack].pop(creates_to_move - i)

        # setting stacks and moving on
        stacks = new_stack

# getting the first of each stack
for stack in stacks:
    firsts.append(stack[0])

# output
print(''.join(firsts))
