

def main():
    total = 0
    with open("./input.txt", "r") as reader:
        for line in reader.readlines():

            config = {"red": 0, "green": 0, "blue": 0}

            line = line.replace("\n", "")

            game_set = line.split(": ")[1]

            level = game_set.split("; ")

            for draw in level:
                games = draw.split(", ")
                for game in games:
                    [count, choice] = game.split(" ")

                    if int(count) > config[choice]:
                        config[choice] = int(count)

            i = 1

            for b in config.values():
                i *= b

            total += i

    print(total)


if __name__ == "__main__":
    main()
