# 2021 adventofcode
# day 3, part 2
from collections import Counter

def sub_matrix(key, pos, matrix):
    new_matrix = []
    for i in range(len(matrix)):
        if matrix[i][pos] == key:
            new_matrix.append(matrix[i])
    return (new_matrix)



def get_gas(matrix, flip=0):
    found = 0
    pos = 0
    while not found:
        matrix_trans = [*zip(*matrix)]      
        data = Counter(matrix_trans[pos])
        data_mode = data.most_common(1)
        data_occure = data.most_common()
        mode = data_mode[0][0]

        # if they are equal, default to 1
        if data_occure[0][1] == data_occure[1][1]:
            mode = '1'

        # for co2
        if (flip and mode == '1'):
            mode = '0'
        elif (flip and mode == '0'):
            mode = '1'
            
        sub = sub_matrix(mode, pos, matrix)
        matrix = sub
        
        if len(matrix) == 1:
            found = True

        pos += 1;

    return (sub)


def get_o2(matrix):
    return (get_gas(matrix)[0])

def get_co2(matrix):
    return (get_gas(matrix, True)[0])

    

with open('data.txt', 'r') as data_file:
    matrix = list(map(list, map(str.strip, [c for c in data_file])))
    listtostring_fn = lambda s: ''.join([str(elem) for elem in s])


    o2 = get_o2(matrix)
    o2_str = listtostring_fn(o2)
    o2_num = int(o2_str, 2)
    print (f"{o2_num=}")

    co2 = get_co2(matrix)
    co2_str = listtostring_fn(co2)
    co2_num = int(co2_str, 2)
    print (f"{co2_num=}")
    
    result = co2_num* o2_num
    print (f"{result=}")

    
