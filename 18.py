from aocd.models import Puzzle
import numpy as np

def find_object(object_char,maze):
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if(maze[x][y]=='@'):
                return x,y
            
def remove_key(key,maze):
    for x in range(len(maze)):
        maze[x]=maze[x].replace(key,'.')
        maze[x]=maze[x].replace(key.upper(),'.')
    return maze

def print_maze(maze):
    for row in maze:
        print(row)


def find_closest_key(x,y,maze,visited,steps):
    item = maze[x][y]
    if(item=='#'):
        return [9999]

    if(item.isupper()):
        return [9999]

    visited = visited.copy()
    if([x,y] in visited):
        return [9999]
    visited.append([x,y])
    if(item.islower()):
        # print("FOUND "+maze[x][y]+' in '+str(steps))
        return [steps, item, x, y]
    
    results = []
    results.append(find_closest_key(x+1,y,maze,visited,steps+1))
    results.append(find_closest_key(x-1,y,maze,visited,steps+1))
    results.append(find_closest_key(x,y+1,maze,visited,steps+1))
    results.append(find_closest_key(x,y-1,maze,visited,steps+1))

    min = 9999
    best = [9999]
    for result in results:
        if(result[0]<min):
            min = result[0]
            best = result
    return best


maze = Puzzle(year=2019, day=18).input_data.split('\n')
x,y=find_object('@',maze)
steps = 0
found_keys = []

for i in range(26):
    closest = find_closest_key(x,y,maze,[],0)
    steps+=closest[0]
    print(steps)
    key=closest[1]
    found_keys.append(key)
    x=closest[2]
    y=closest[3]
    maze = remove_key(key,maze)

print_maze(maze)
print(found_keys)

#1804 too low
#6628 too low
#7538 too high