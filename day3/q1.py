# 2021 adventofcode
# day 3, part 1
with open('data.txt', 'r') as data_file:
    matrix = list(map(list, map(str.strip, [c for c in data_file])))
    matrix_trans = [*zip(*matrix)]
    #[print(*line) for line in matrix_trans]
       
    mode_fn = lambda a: max(set(a), key = a.count)    
    flipchar_fn = lambda c: 1 if (c == '0') else 0
    listtostring_fn = lambda s: ''.join([str(elem) for elem in s])
    flipstring_fn  = lambda s: listtostring_fn(list(map(flipchar_fn, s)))
    
    gamma = ''.join(map(mode_fn, matrix_trans))    
    epsilon = flipstring_fn(gamma)
    result = int(gamma,2) * int(epsilon,2)
    
    print (f"{result=}")
