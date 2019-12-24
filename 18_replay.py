from aocd.models import Puzzle
import numpy as np
import random


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

def shortest_path(x,y,maze,visited,steps,target):
    item = maze[x][y]
    if(item=='#'):
        return [9999]

    if(item.isupper()):
        return [9999]

    visited = visited.copy()
    if([x,y] in visited):
        return [9999]
    visited.append([x,y])
    if(item == target):
        return [steps, item, x, y]
    
    results = []
    results.append(shortest_path(x+1,y,maze,visited,steps+1,target))
    results.append(shortest_path(x-1,y,maze,visited,steps+1,target))
    results.append(shortest_path(x,y+1,maze,visited,steps+1,target))
    results.append(shortest_path(x,y-1,maze,visited,steps+1,target))

    min = 9999
    best = [9999]
    for result in results:
        if(result[0]<min):
            min = result[0]
            best = result
    return best
maze = Puzzle(year=2019, day=18).input_data.split('\n')

order = ['o', 'a', 'm', 'y', 'x', 'q', 'k', 'c', 'z', 'e', 't', 'h', 'l', 'g', 'i', 'u', 'j', 'd', 'w', 'r', 'f', 'v', 'p', 'n', 'b', 's']
#7538
order = ['o', 'm', 'a', 'y', 'x', 'q', 'k', 'c', 'z', 'e', 't', 'h', 'l', 'g', 'i', 'u', 'j', 'd', 'w', 'r', 'f', 'v', 'p', 'n', 'b', 's']
#7518
order = ['o', 'm', 'a', 'y', 'x', 'q', 'e', 'c', 'z', 'k', 't', 'h', 'l', 'g', 'i', 'u', 'j', 'd', 'w', 'r', 'f', 'v', 'p', 'n', 'b', 's']
#7514

orig_maze = Puzzle(year=2019, day=18).input_data.split('\n')
start_x,start_y=find_object('@',orig_maze)
offset = 1
while(True):
    broke =False
    index1 = random.randrange(0,len(order)-1,1)
    index2 = random.randrange(0,len(order)-1,1)
    if(index1-index2<2):
        continue
    maze = orig_maze.copy()
    x = start_x
    y = start_y
    steps = 0
    new_order = order.copy()
    new_order[index1]=order[index2]
    new_order[index1+1]=order[index2+1]
    new_order[index2]=order[index1]
    new_order[index2+1]=order[index1+1]
    for item in new_order:
        result = shortest_path(x,y,maze,[],0,item)
        maze = remove_key(item,maze)
        if(result[0]==9999):
            broke=True
            break
        steps+= result[0]
        x = result[2]
        y = result[3]
    if(not broke):
        with open('results.txt','a+') as my_file:
            my_file.write(str(new_order)+'\n')
            my_file.write(str(steps)+'\n')