from aocd.models import Puzzle
from math import atan
import numpy as np

def get_angle(x1, x2, y1, y2):
    if x1 == x2:
        angle = 90 if y2 > y1 else 270
    else:
        degrees = atan((y2-y1)/(x2-x1))*57.2957795
        if x2 >= x1 and y2 >= y1:
            angle = degrees
        elif x2 < x1 and y2 >= y1 or x2 < x1 and y2 < y1:
            angle = degrees + 180
        elif x2 >= x1 and y2 < y1:
            angle = degrees + 360
    return (angle-270)%360

def visible_astroid_angles(x,y,data):
    angles = set()
    astroids = []
    for y2 in range(len(data)):
        for x2 in range(len(data[y])):
            field = data[y2][x2]
            if(not (y2==y and x2==x) and field=='#'):
                angles.add(get_angle(x,x2,y,y2))
    return angles

def find_astroid_with_angle(x,y,data,angle):
    angles = set()
    astroids = []
    for y2 in range(len(data)):
        for x2 in range(len(data[y])):
            field = data[y2][x2]
            if(not (y2==y and x2==x) and field=='#'):
                angle2 = get_angle(x,x2,y,y2)
                if(angle2==angle):
                    print(x2, y2)
                

data = Puzzle(year=2019, day=10).input_data
# data = '#..\n.#.\n..#'
# data = '.#..#\n.....\n#####\n....#\n...##'
# data = '.#..#..###\n####.###.#\n....###.#.\n..###.##.#\n##.##.#.#.\n....###..#\n..#.#..#.#\n#..#.#.###\n.##...##.#\n.....#.#..'
# data = '.#..##.###...#######\n##.############..##.\n.#.######.########.#\n.###.#######.####.#.\n#####.##.#.##.###.##\n..#####..#.#########\n####################\n#.####....###.#.#.##\n##.#################\n#####.##.###..####..\n..######..##.#######\n####.##.####...##..#\n.#####..#.######.###\n##...#.##########...\n#.##########.#######\n.####.#.###.###.#.##\n....##.##.###..#####\n.#.#.###########.###\n#.#.#.#####.####.###\n###.##.####.##.#..##'
data = data.split('\n')

result = data.copy()
result = list(map(lambda x: list(x),result))

counts = []

for y in range(len(data)):
    for x in range(len(data[y])):
        # print("at "+str(x)+','+str(y))
        field = data[y][x]
        if(field=='#'):
            angles = visible_astroid_angles(x,y,data)
            count = len(angles)
            if(count == 276):
                print(x)
                print(y)
            counts.append(count)
            result[y][x] =str(count)
print(max(counts))

laser_x = 17
laser_y = 22
astroid_angles = visible_astroid_angles(laser_x,laser_y,data)
n200 = sorted(astroid_angles)[199]
find_astroid_with_angle(laser_x,laser_y,data,n200)


