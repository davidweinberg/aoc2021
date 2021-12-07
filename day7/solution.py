from collections import defaultdict

#aoc day 7

with open('data.txt', 'r') as file:
    crabs = list(map(int, file.read().strip().split(",")))
    costs1 = defaultdict(int)
    costs2 = defaultdict(int)

    def calc_cost(distance):
        sum = 0
        for i in range(1,distance+1):
            sum += i
        return sum

    
    for i in range (max(crabs)+1):
        # cacluate cost to move all to position i
        for crab in crabs:
            costs1[i] += abs(crab - i)

    min_key = min(costs1, key = costs1.get)
    print (f"Part 1\nPosition: {min_key}, Value: {costs1[min_key]}")


    for i in range (max(crabs)+1):
        # cacluate cost to move all to position i
        for crab in crabs:
            costs2[i] += calc_cost(abs(crab - i))

    min_key = min(costs2, key = costs2.get)
    print (f"\nPart 2\nPosition: {min_key}, Value: {costs2[min_key]}")
