from aocd.models import Puzzle
import numpy as np

def get_coordinates(path):
    coordinates = []
    x = 0
    y = 0
    coordinates.append(str(x)+','+str(y))
    for step in path:
        direction = step[0]
        steps = int(step[1:])
        if direction == 'L':
            for i in range(0,steps):
                x=x-1
                coordinates.append(str(x)+','+str(y))
        elif direction == 'R':
            for i in range(0,steps):
                x=x+1
                coordinates.append(str(x)+','+str(y))
        elif direction == 'U':
            for i in range(0,steps):
                y=y+1
                coordinates.append(str(x)+','+str(y))
        elif direction == 'D':
            for i in range(0,steps):
                y=y-1
                coordinates.append(str(x)+','+str(y))
        else:
            print("WRONG DIRECTION")
    return coordinates
        

data = Puzzle(year=2019, day=3).input_data.split('\n')

path1=data[0].split(',')
path2=data[1].split(',')

coordinates1=np.asarray(get_coordinates(path1))
coordinates2=np.asarray(get_coordinates(path2))
sect = np.intersect1d(coordinates1,coordinates2)
indexes = []
for i in sect[1:]:
    index1  = np.where(coordinates1 == i)[0][0]
    index2  = np.where(coordinates2 == i)[0][0]
    indexes.append(index1+index2)

print(min(indexes))
# i = 0
# for coor1 in coordinates1:
#     i+=1
#     print(i)
#     for coor2 in coordinates2:
#         if coor1 == coor2:
#             print(coor1)
