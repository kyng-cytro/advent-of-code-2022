def main():
    with open('./input.txt', 'r') as reader:
        total = 0
        for game in reader.readlines():
            points = 0
            winning_numbers = set(game.strip().split(
                ": ")[1].split(" | ")[0].split(" "))
            player_numbers = set(game.strip().split(
                ": ")[1].split(" | ")[1].split(" "))

            if '' in winning_numbers:
                winning_numbers.remove('')

            if '' in player_numbers:
                player_numbers.remove('')

            for number in player_numbers:
                if number in winning_numbers:
                    if points == 0:
                        points = 1
                        continue
                    points += points
            total += points
        print(total)


if __name__ == "__main__":
    main()
