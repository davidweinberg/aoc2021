# aoc, day5
from dataclasses import dataclass

max_x = 1000
max_y = 1000

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Line:
    start: Point
    end: Point
    slope: int
    slope_inf: bool

def draw_graph(graph):
    for j in range(max_y):
        for i in range(max_x):
            print (graph[(i,j)], end=' ')
        print()
 
def draw_straight_line(graph, line):
    if line.slope == 0 and not line.slope_inf:
        # draw horizonal line
        if line.start.x < line.end.x:
            for i in range((line.end.x+1)-line.start.x):
                graph[((line.start.x+i),line.start.y)] += 1
        else:
            for i in range(line.start.x+1-line.end.x):
                graph[((line.start.x-i),line.start.y)] += 1
    elif line.slope == 0 and line.slope_inf:
        if line.start.y < line.end.y:
            for i in range((line.end.y+1)-line.start.y):                
                graph[((line.start.x),line.start.y+i)] += 1
        else:
            for i in range(line.start.y+1-line.end.y):
                graph[((line.start.x),line.start.y-i)] += 1

def draw_diagonal_line(graph, line):
    if (line.slope == 1 or line.slope == -1):
        m = line.slope
        b = int(line.start.y - (line.start.x * m))
                            
        if (line.start.x < line.end.x):
            startx = line.start.x
            endx = line.end.x            
        else:
            startx = line.end.x
            endx = line.start.x

        for x in range (startx, endx + 1):                
            y = m * x + b
            graph[(x, y)] += 1
            

def calc_num_intersect(graph):

    result = 0
    for j in range(max_y):
        for i in range(max_x):
            val = graph[(i,j)]
            if val > 1:
                result += 1

    return result

    

with open('data.txt', 'r') as data_file:
    data_lines = data_file.readlines()

    line_set = []
    graph = {}

    for data_line in data_lines:
        data_line = data_line.strip()
        points = data_line.split(' -> ')

        start = list(map(int,points[0].split(',')))
        startp = Point(start[0], start[1])
        end = list(map(int,points[1].split(',')))
        endp = Point(end[0], end[1])        


        if (endp.x - startp.x) == 0:
            slope = 0
            slope_inf = True
        else:
            slope = int((endp.y - startp.y) / (endp.x - startp.x))
            slope_inf = False
            
        
        myline = Line(startp, endp, slope, slope_inf)
        line_set.append(myline)
    # end load data for loop        
    

    # create graph
    for j in range(max_y):
        for i in range(max_x):
            graph[(i,j)] = 0



    print ("Part 1")    
    # draw all the straight lines
    for line in line_set:
        draw_straight_line(graph, line)
    
    #draw_graph(graph)
    print ("result="+str(calc_num_intersect(graph)))

    print ()
    print ("Part 2")
    for line in line_set:
        draw_diagonal_line(graph, line)
        
    #draw_graph(graph)
    print ("result="+str(calc_num_intersect(graph)))
