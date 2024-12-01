import threading
from multiprocessing.pool import ThreadPool as Pool

SEEDS = []

threads = []

MAPS = {
    "seed-to-soil": [],
    "soil-to-fertilizer": [],
    "fertilizer-to-water": [],
    "water-to-light": [],
    "light-to-temperature": [],
    "temperature-to-humidity": [],
    "humidity-to-location": []
}

PLOT = {
    "seed-to-soil": {},
    "soil-to-fertilizer": {},
    "fertilizer-to-water": {},
    "water-to-light": {},
    "light-to-temperature": {},
    "temperature-to-humidity": {},
    "humidity-to-location": {}
}


def find_point(map, point):
    try:
        return PLOT[map][point]
    except KeyError:
        return point


def setup():
    global SEEDS
    global MAPS
    with open("./input.txt", 'r') as reader:
        gear = None
        for index, line in enumerate(reader.readlines()):
            if index == 0:
                SEEDS = line.split(": ")[1].strip().split(" ")
            if "map:" in line:
                gear = line.split(" map:")[0].strip()
                continue

            if line != "\n" and gear:
                MAPS[gear].append(line.strip())


def run_range(map, dest, source, path):
    for i in range(path):  # this part where we loop to path. path can be a very large number
        PLOT[map][source + i] = dest + i


def plot(map):
    for points in MAPS[map]:
        dest = int(points.split(" ")[0])
        source = int(points.split(" ")[1])
        path = int(points.split(" ")[2])
        threads.append(
            threading.Thread(target=run_range, args=(map, dest, source, path)))
        threads[-1].start()

    for t in threads:
        t.join()


def main():
    locations = []
    setup()
    pool = Pool(7)
    for map in MAPS:
        pool.apply(plot, (map,))

    pool.close()
    pool.join()

    for seed in SEEDS:
        location = seed
        for path in MAPS:
            location = find_point(path, int(location))
        locations.append(location)

    print(min(locations))


if __name__ == "__main__":
    main()
