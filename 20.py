from aocd.models import Puzzle
import numpy as np
import sys
sys.setrecursionlimit(10000)

def print_maze(maze):
    for row in maze:
        print(row)

def portal_dict(maze):
    portals = {}
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if(x+1<len(maze) and maze[x][y].isupper() and maze[x+1][y].isupper()):
                name = maze[x][y]+maze[x+1][y]
                if(x+2<len(maze) and maze[x+2][y]=='.'):
                    if(name in portals):
                        portals[name].append([x+2,y])
                    else:
                        portals[name]=[[x+2,y]]
                elif(maze[x-1][y]=='.'):
                    if(name in portals):
                        portals[name].append([x-1,y])
                    else:
                        portals[name]=[[x-1,y]]

            elif(y+1<len(maze[x]) and maze[x][y].isupper() and maze[x][y+1].isupper()):
                name = maze[x][y]+maze[x][y+1]
                if(y+2<len(maze[x]) and maze[x][y+2]=='.'):
                    if(name in portals):
                        portals[name].append([x,y+2])
                    else:
                        portals[name]=[[x,y+2]]
                elif(maze[x][y-1]=='.'):
                    if(name in portals):
                        portals[name].append([x,y-1])
                    else:
                        portals[name]=[[x,y-1]]
    return portals


def find_end(x,y,end_x,end_y,maze,visited,steps,portals,portals_taken):
    if(maze[x][y]=='.'):
        steps+=1
        if([x,y] in visited):
            return
        visited = visited.copy()
        visited.append([x,y])
        find_end(x+1,y,end_x,end_y,maze,visited,steps,portals,portals_taken)
        find_end(x-1,y,end_x,end_y,maze,visited,steps,portals,portals_taken)
        find_end(x,y+1,end_x,end_y,maze,visited,steps,portals,portals_taken)
        find_end(x,y-1,end_x,end_y,maze,visited,steps,portals,portals_taken)
    elif(maze[x][y].isupper()):
        visited = visited.copy()
        visited.append([x,y])
        if(maze[x+1][y].isupper()):
            portal = maze[x][y] + maze[x+1][y]
        elif(maze[x-1][y].isupper()):
            portal = maze[x-1][y] + maze[x][y]
        elif(maze[x][y+1].isupper()):
            portal = maze[x][y] + maze[x][y+1]
        elif(maze[x][y-1].isupper()):
            portal = maze[x][y-1] + maze[x][y]
        else:
            print('could not find other')
            return
        if(portal == 'ZZ'):
            print("FOUND IN "+str(steps))
            return
        if(portal == 'AA'):
            return

        if(portal in portals_taken):
            return
        portals_taken = portals_taken.copy()
        portals_taken.append(portal)
        gates = portals[portal]
        dist1 = abs(gates[0][0]-x) + abs(gates[0][1]-y)
        dist2 = abs(gates[1][0]-x) + abs(gates[1][1]-y)
        if(dist1>dist2):
            find_end(gates[0][0],gates[0][1],end_x,end_y,maze,visited,steps,portals,portals_taken)
        else:
            find_end(gates[1][0],gates[1][1],end_x,end_y,maze,visited,steps,portals,portals_taken)
    else:
        return


                

maze = Puzzle(year=2019, day=20).input_data.split('\n')
# with open('20_input1.txt','r') as input_file:
#     maze = input_file.read().split('\n')
portals = portal_dict(maze)
start_x, start_y = portals['AA'][0]
end_x, end_y = portals['ZZ'][0]

find_end(start_x,start_y,end_x,end_y,maze,[],0,portals,[])

#690 too high
#750 too high
