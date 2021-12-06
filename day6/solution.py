#aoc day 6
from collections import defaultdict

with open('data.txt', 'r') as file:
    data = file.read().strip().split(",")
    fishes = defaultdict(int)

    for i in data:
        fishes[int(i)] += 1


    def calc_growth(fishes, days):

        for i in range(days):
            new_fishes = defaultdict(int)

            for fish in fishes:
                if fish == 0:
                    new_fishes[6] += fishes[fish]
                    new_fishes[8] = fishes[fish]
                else:
                    new_fishes[fish - 1] += fishes[fish]

            fishes = new_fishes

        result = 0
        for fish in fishes:
            result += fishes[fish]
        return result

    print ("Part 1")
    result = calc_growth(fishes, 80)
    print (f"{result=}")

    print ("Part 2");
    result = calc_growth(fishes, 256)
    print (f"{result=}")

