#aoc day 9

with open('example.txt', 'r') as file:

    

    top = []
    lows = []
    lines = file.readlines()
    
    for line in lines:
        line = line.strip()
        temp = []
        for c in line:
            temp.append(int(c))
        top.append(temp)

    #print (top)

    cols = len(top)
    rows = len(top[0])
    size = cols * rows
    #print (size)


    
    

    for i in range(cols):
        
        for j in range(rows):
            cur = top[i][j]

            if i == cols-1:
                down = 9
            else:
                down = top[i+1][j]

            if i == 0:
                up = 9
            else:
                up = top[i-1][j]
                
            if j == 0:
                left = 9
            else:
                left = top[i][j-1]
                
            if j == rows-1:
                right = 9                
            else:
                right = top[i][j+1]


            if (cur < left and cur < right and cur < up and cur < down):
                #print ("add" + str(cur))
                lows.append(cur+1)
            
            #print (f"{cur=}")
            #print (f"{up=}")
            #print (f"{down=}")
            #print (f"{left=}")
            #print (f"{right=}")
            #print ()
    #print (lows)
    result = sum(lows)
    print (f"Part 1:\n{result}")    
            
        
        
        




    
 

    
