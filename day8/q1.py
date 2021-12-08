from collections import defaultdict

#aoc day 8

with open('data.txt', 'r') as file:
       
    lines = file.readlines()
    result = 0
    
    for line in lines:
        line = line.strip()         
        before, after = line.split(" | ")
        after = after.split()
        before = before.split()

        by_len = defaultdict(list)
        for x in before:
            by_len[len(x)].append(x)    
            

        
        for x in after:
            if len(by_len[len(x)]) == 1:
                result += 1

    print (by_len)
    print (f"Part 1:\n{result=}")

    

    
