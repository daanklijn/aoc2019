from aocd.models import Puzzle
import numpy as np


def get_pattern(row_number,length):
    result=[]
    result+=[0]*row_number
    result+=[1]*row_number
    result+=[0]*row_number
    result+=[-1]*row_number
    result = np.resize(result, length+1)
    result = np.delete(result,0)
    return result

def get_row(row_number,data):
    sum = 0
    pattern = get_pattern(row_number,len(data))
    for i in range(len(data)):
        sum+=int(data[i])*pattern[i]
    return str(sum)[-1]

def get_phase(data):
    result = ''
    for i in range(len(data)):
        result += get_row(i+1,data)
    return result

# data = '12345678'
# data = '80871224585914546619083218645595'
# data = '19617804207202209144916044189917'
# data = '69317163492948606335995924319873'
# data = '03036732577212944063491565474664'*10000
data = Puzzle(year=2019, day=16).input_data*10000
# first_seven = int(data[0:7])
# print(first_seven)

offset = 5974057
skip = 5500000

chars = list(data)
ints = list(map(lambda x: int(x),chars))
ints = ints[skip:]


for j in range(100):
    print(j)
    i = len(ints)-2
    while i>-1:
        ints[i]=abs(ints[i]+ints[i+1])%10
        i-=1

print(ints[offset-skip:offset-skip+10])

