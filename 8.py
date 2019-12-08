from aocd.models import Puzzle
import numpy as np


data = Puzzle(year=2019, day=8).input_data
w = 25
h = 6
n = w*h
layers = [data[i:i+n] for i in range(0, len(data), n)]

#1
# min = 1000
# for layer in layers:
#     if(layer.count('0')<min):
#         min = layer.count('0')
#         print(layer.count('1')*layer.count('2'))

def row_to_image(row):
    result = ''
    for number in row:
        if(number==1):
            result+='#'
        else: 
            result+=' '
    return result


result = np.full(n,2)
for layer in layers:
    for i in range(n):
        if(result[i]<2):
            continue
        else:
            result[i]=layer[i]

rows = [result[i:i+w] for i in range(0, len(result), w)]
for row in rows:
    print(row_to_image(row))

