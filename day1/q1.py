with open('data.txt', 'r') as data_file:
    mylist = list(map(int, data_file.readlines()))
    increase = 0
    for i in range(1,len(mylist)):
        if (mylist[i-1] < mylist[i]):
            increase += 1
    
    print (f"{increase=}")

