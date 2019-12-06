from aocd.models import Puzzle
import numpy as np

data = Puzzle(year=2019, day=6).input_data.split('\n')
print(data)
    
# data='COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L'.split(',')
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

tree = ['COM',[]]
place_in_tree(tree)
print(count_orbits(tree,0))
