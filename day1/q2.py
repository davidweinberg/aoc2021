with open('data.txt', 'r') as data_file:
    mylist = list(map(int, data_file.readlines()))
     
    increase = 0
    window1 = 0
    window2 = 0

    for i in range(len(mylist)-3):    
        window1 = mylist[i] + mylist[i+1] + mylist[i+2]
        window2 = mylist[i+1] + mylist[i+2] + mylist[i+3]

        if (window2 > window1):
            increase += 1
    
    print (f"{increase=}")

