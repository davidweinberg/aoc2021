with open('data.txt', 'r') as data_file:
    x = 0
    y = 0 #depth
    
    for index, line in enumerate(data_file):
        (direction, value) = line.split()
        value = int(value)
        
        if direction == 'forward':
            x += value
        elif direction == 'down':
            y += value
        elif direction == 'up':
            y -= value

    print (x * y)
        

