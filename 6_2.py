from aocd.models import Puzzle
import numpy as np

data = Puzzle(year=2019, day=6).input_data.split('\n')
    
# data='COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L,K)YOU,I)SAN'.split(',')
data = list(map(lambda x: x.split(')'),data))

def place_in_tree(tree):
    to_find = tree[0]
    to_remove = []
    for item in data:
        if(item[0]==to_find):
            tree[1].append([item[1],[]])
            to_remove.append(item)
    for item in to_remove:
        data.remove(item)
    for link in tree[1]:
        place_in_tree(link)

def count_orbits(tree,depth):
    sum = 0
    for i in tree[1]:
        sum+=depth+1
        sum+=count_orbits(i,depth+1)
    return sum

def path_for(tree,location):
    path = []
    if(tree[0]==location):
        return [location]
    for i in tree[1]:
        sub_path = path_for(i,location)
        if(len(sub_path)>0):
            path = [tree[0]]
            path+=sub_path
    return path


tree = ['COM',[]]
place_in_tree(tree)
# print(count_orbits(tree,0))
path_san = path_for(tree,'SAN')
path_you = path_for(tree,'YOU')

for i in range(len(path_san)):
    if(path_san[i]!=path_you[i]):
        print(len(path_you)+len(path_san)-2*i-2)
        break

