def convert_to_grid(input):
    grid = []
    for line in input:
        grid.append([item for item in list(line.strip())])

    return grid


def get_up_score(grid, row_num, item_num):
    score = 0

    item = grid[row_num][item_num]

    x = row_num - 1

    while x >= 0:

        if item <= grid[x][item_num]:
            score += 1
            break

        score += 1

        x -= 1
    return score


def get_down_score(grid, row_num, item_num):
    score = 0

    item = grid[row_num][item_num]

    x = row_num + 1

    while x <= len(grid) - 1:

        if item <= grid[x][item_num]:
            score += 1
            break

        score += 1

        x += 1

    return score


def get_left_score(grid, row_num, item_num):
    score = 0

    item = grid[row_num][item_num]

    x = item_num - 1

    while x >= 0:

        if item <= grid[row_num][x]:
            score += 1
            break

        score += 1

        x -= 1

    return score


def get_right_score(grid, row_num, item_num):
    score = 0

    item = grid[row_num][item_num]

    x = item_num + 1

    while x <= len(grid) - 1:

        if item <= grid[row_num][x]:
            score += 1
            break

        score += 1

        x += 1

    return score


with open('./input.txt', 'r') as input:
    grid = convert_to_grid(input)
    scores = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            scores.append(get_left_score(grid, y, x) * get_right_score(
                grid, y, x) * get_up_score(grid, y, x) * get_down_score(grid, y, x))

    print(max(scores))
