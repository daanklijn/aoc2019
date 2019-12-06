from aocd.models import Puzzle
import numpy as np


data = Puzzle(year=2019, day=2).input_data.split(',')
# data = '1,1,1,4,99,5,6,0,99'.split(',')
# data = '1,0,0,0,99'.split(',')

for i in range(0,99):
    for j in range(0,99):
        values = []
        for dat in data:
            values.append(int(dat))
        values[1]=i
        values[2]=j
        position = 0
        while(True):
            value = values[position]
            if(value == 99):
                if(values[0]==19690720):
                    print("HIIIIIII" + str(i) + ' ' + str(j))
                break
            elif(value == 1):
                a = values[values[position+1]]
                b = values[values[position+2]]
                c = values[position+3]
                values[c]=a+b
            elif(value == 2):
                a = values[values[position+1]]
                b = values[values[position+2]]
                c = values[position+3]
                values[c]=a*b
            else:
                print("wrong op")
            position += 4






