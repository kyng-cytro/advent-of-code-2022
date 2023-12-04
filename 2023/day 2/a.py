config = {"red": 12, "green": 13, "blue": 14}


def main():
    total = 0
    with open("./input.txt", "r") as reader:
        for line in reader.readlines():
            line = line.replace("\n", "")

            game_no = int(line.split(" ")[1].replace(":", ''))

            game_set = line.split(": ")[1]

            level = game_set.split("; ")

            did_break = False

            for draw in level:
                games = draw.split(", ")
                for game in games:
                    [count, choice] = game.split(" ")
                    if int(count) > config[choice]:
                        did_break = True
                        break

            if not did_break:
                total += game_no

    print(total)


if __name__ == "__main__":
    main()
