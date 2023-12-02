
"""
    Turns out file names can reused so this is not a valid
    solution for now.

    Half solution at best i guess
    
"""
total = 0
cwd = ""
directory_history = []
directories = {}


def is_file(line):
    if line.startswith('$') or line.startswith('dir'):
        return False
    return True


with open('input.txt', 'r') as input:
    for line in input:
        output = line.strip()

        if output.startswith('dir'):
            try:
                directories[cwd]['subs'].append(output.split(' ')[1])
                continue

            except KeyError:
                directories[cwd] = {'files': [], 'subs': []}
                directories[cwd]['subs'] = [output.split(' ')[1]]
                continue

        if output == '$ cd /':
            cwd = 'root'
            directory_history.append(cwd)
            continue

        if output == "$ cd ..":
            cwd = directory_history[-2]
            directory_history.append(cwd)
            continue

        if output.startswith('$ cd'):
            cwd = output.split(' ')[2]
            directory_history.append(cwd)
            continue

        if is_file(output):
            try:
                directories[cwd]['files'].append(int(output.split(' ')[0]))
                continue

            except KeyError:
                directories[cwd] = {'files': [], 'subs': []}
                directories[cwd]['files'] = [int(output.split(' ')[0])]


directories['root']['subs'] = [dir for dir in directories.keys()][1:]

print(directories)

for dir in directories.keys():

    dir_sum = sum(directories[dir]['files'])

    for sub in directories[dir]['subs']:
        dir_sum += sum(directories[sub]['files'])

    if dir_sum > 100000:
        continue

    total = total + dir_sum

print(total)
