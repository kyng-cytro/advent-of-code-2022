not_visible = 0


def convert_to_grid(input):
    grid = []
    for line in input:
        grid.append([item for item in list(line.strip())])

    return grid


def remove_edge(grid):
    count = 0

    count += len(grid[0]) + len(grid[-1])

    grid = grid[1:-1]

    for index in range(len(grid)):
        grid[index] = grid[index][1:-1]
        count += 2

    return grid, count


def is_visible_left(grid, row_num, item_num):
    item = grid[row_num][item_num]

    for x in range(0, item_num):
        if grid[row_num][x] >= item:
            return False

    return True


def is_visible_right(grid, row_num, item_num):

    item = grid[row_num][item_num]

    for x in range(item_num + 1, len(grid)):
        if grid[row_num][x] >= item:
            return False

    return True


def is_visible_top(grid, row_num, item_num):
    item = grid[row_num][item_num]

    for x in range(0, row_num):
        if grid[x][item_num] >= item:
            return False

    return True


def is_visible_bottom(grid, row_num, item_num):

    item = grid[row_num][item_num]

    for x in range(row_num + 1, len(grid)):
        if grid[x][item_num] >= item:
            return False

    return True


with open('./input.txt', 'r') as input:
    grid = convert_to_grid(input)

    filtered, count = remove_edge(grid)

    not_visible = count

    for y, row in enumerate(filtered):
        for x, tree in enumerate(row):
            if is_visible_top(grid, y+1, x+1) or is_visible_bottom(grid, y+1, x+1) or is_visible_left(grid, y+1, x+1) or is_visible_right(grid, y+1, x+1):
                not_visible += 1


print(not_visible)
