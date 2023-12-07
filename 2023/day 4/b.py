def main():
    with open('./input.txt', 'r') as reader:
        cards = [1]*300
        count = 0
        for i, game in enumerate(reader.readlines()):
            points = 0
            winning_numbers = set(game.strip().split(
                ": ")[1].split(" | ")[0].split(" "))
            player_numbers = set(game.strip().split(
                ": ")[1].split(" | ")[1].split(" "))

            if '' in winning_numbers:
                winning_numbers.remove('')

            if '' in player_numbers:
                player_numbers.remove('')

            points = len(winning_numbers.intersection(player_numbers))
            for j in range(points):
                cards[j+i+1] = cards[j+i+1] + cards[i]

            count += 1
        print(sum(cards[:count]))


if __name__ == "__main__":
    main()
