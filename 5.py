from aocd.models import Puzzle
import numpy as np
import time



data = Puzzle(year=2019, day=5).input_data.split(',')
values = list(map(lambda x : int(x),data))

# values= [1002,4,3,4,33]

# values = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
# values = [3,9,8,9,10,9,4,9,99,-1,8]
# values = [3,9,7,9,10,9,4,9,99,-1,8]
# values = [3,3,1108,-1,8,3,4,3,99]
# values = [3,3,1107,-1,8,3,4,3,99]
# values = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]

input_var = 5

def get_value(mode,position):
    if(mode==0):
        return values[values[position]]
    elif(mode==1):
        return values[position]
    else:
        print("WRONG MODE")

def get_location(mode,position):
    if(mode==0):
        return values[position]
    else:
        print("Cannot get location for other mode")



position = 0
while(True):

    value = values[position]
    instruction = str(value).zfill(5)
    opcode = int(instruction[3:5])
    mode1 = int(instruction[2])
    mode2 = int(instruction[1])
    mode3 = int(instruction[0])
    time.sleep(1)

    if(opcode == 99):
        print("DONE")
        break
    elif(opcode == 1):
        a = get_value(mode1,position+1)
        b = get_value(mode2,position+2)
        c = get_location(mode3,position+3)
        values[c]=a+b
        position+=4
    elif(opcode == 2):
        a = get_value(mode1,position+1)
        b = get_value(mode2,position+2)
        c = get_location(mode3,position+3)
        values[c]=a*b
        position+=4
    elif(opcode == 3):
        a = get_location(mode1,position+1)
        values[a] = input_var
        position+=2
    elif(opcode == 4):
        a = get_value(mode1,position+1)
        print(a)
        position+=2
    elif(opcode == 5):
        a = get_value(mode1,position+1)
        b = get_value(mode2,position+2)
        if(a != 0):
            position=b
        else:
            position+=3
    elif(opcode == 6):
        a = get_value(mode1,position+1)
        b = get_value(mode2,position+2)
        if(a == 0):
            position=b
        else:
            position+=3
    elif(opcode == 7):
        a = get_value(mode1,position+1)
        b = get_value(mode2,position+2)
        c = get_location(mode3,position+3)
        if(a < b):
            values[c]=1
        else:
            values[c]=0
        position+=4
    elif(opcode == 8):
        a = get_value(mode1,position+1)
        b = get_value(mode2,position+2)
        c = get_location(mode3,position+3)
        if(a == b):
            values[c]=1
        else:
            values[c]=0
        position+=4
            
        

    else:
        print("wrong op" + str(instruction))








