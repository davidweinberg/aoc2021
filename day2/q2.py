with open('data.txt', 'r') as data_file:
    x = 0
    y = 0 #depth
    aim = 0
    for index, line in enumerate(data_file):
        (direction, value) = line.split()
        value = int(value)
        
        if direction == 'forward':
            x += value
            y += aim * value
        elif direction == 'down':            
            aim += value
        elif direction == 'up':
            aim -= value

    print (x * y)
        

