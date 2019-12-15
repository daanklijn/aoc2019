from aocd.models import Puzzle
import numpy as np
import math

def get_value(mode,position,code,relative_base):
    if(mode==0):
        return code[code[position]]
    elif(mode==1):
        return code[position]
    elif(mode==2):
        return code[relative_base+code[position]]
    else:
        print("WRONG MODE")

def get_location(mode,position,code,relative_base):
    if(mode==0):
        return code[position]
    if(mode==2):
        return code[position]+relative_base
    else:
        print("Cannot get location for other mode")

def run_intcode(code,input_vars,position=0,relative_base=0):
    var_count=0
    prints=0

    while(True):
        value = code[position]
        instruction = str(value).zfill(5)
        opcode = int(instruction[3:5])
        mode1 = int(instruction[2])
        mode2 = int(instruction[1])
        mode3 = int(instruction[0])

        if(opcode == 99):
            raise Exception()
            
            break
        elif(opcode == 1):
            a = get_value(mode1,position+1,code,relative_base)
            b = get_value(mode2,position+2,code,relative_base)
            c = get_location(mode3,position+3,code,relative_base)
            code[c]=a+b
            position+=4
        elif(opcode == 2):
            a = get_value(mode1,position+1,code,relative_base)
            b = get_value(mode2,position+2,code,relative_base)
            c = get_location(mode3,position+3,code,relative_base)
            code[c]=a*b
            position+=4
        elif(opcode == 3):
            a = get_location(mode1,position+1,code,relative_base)
            code[a] = input_vars[var_count]

            var_count+=1
            position+=2
        elif(opcode == 4):
            a = get_value(mode1,position+1,code,relative_base)
            position+=2
            # print("RETURN:" + str(a))
            return(a,code,position,relative_base)
        elif(opcode == 5):
            a = get_value(mode1,position+1,code,relative_base)
            b = get_value(mode2,position+2,code,relative_base)
            if(a != 0):
                position=b
            else:
                position+=3
        elif(opcode == 6):
            a = get_value(mode1,position+1,code,relative_base)
            b = get_value(mode2,position+2,code,relative_base)
            if(a == 0):
                position=b
            else:
                position+=3
        elif(opcode == 7):
            a = get_value(mode1,position+1,code,relative_base)
            b = get_value(mode2,position+2,code,relative_base)
            c = get_location(mode3,position+3,code,relative_base)
            if(a < b):
                code[c]=1
            else:
                code[c]=0
            position+=4
        elif(opcode == 8):
            a = get_value(mode1,position+1,code,relative_base)
            b = get_value(mode2,position+2,code,relative_base)
            c = get_location(mode3,position+3,code,relative_base)
            if(a == b):
                code[c]=1
            else:
                code[c]=0
            position+=4
        elif(opcode == 8):
            a = get_value(mode1,position+1,code,relative_base)
            b = get_value(mode2,position+2,code,relative_base)
            c = get_location(mode3,position+3,code,relative_base)
            if(a == b):
                code[c]=1
            else:
                code[c]=0
            position+=4
        elif(opcode == 9):
            a = get_value(mode1,position+1,code,relative_base)
            relative_base+=a
            position+=2
        else:
            print("wrong op" + str(instruction))

def try_path(path,direction,visited,x,y,code,position,base):
    path = path.copy()
    visited = visited.copy()
    code = code.copy()
    if(direction==1):
        y+=1
    elif(direction==2):
        y-=1
    elif(direction==3):
        x+=1
    else:
        x-=1
    
    if([x,y] in visited):
        return

    visited.append([x,y])

    path.append(direction)
    result, code, position, base = run_intcode(code,[direction],position,base)
    if(result==1):
        for i in range(1,5):
            try_path(path,i,visited,x,y,code,position,base)
    elif(result==0):
        return
    elif(result==2):
        print("found path to oxygen system: "+ str(len(path)))
        for i in range(1,5):
            fill_with_oxy(i,[[x,y]],x,y,0,code,position,base)

def fill_with_oxy(direction,oxygen,x,y,time,code,position,base):
    if(direction==1):
        y+=1
    elif(direction==2):
        y-=1
    elif(direction==3):
        x+=1
    else:
        x-=1

    if([x,y] in oxygen):
        return

    code = code.copy()

    result, code, position, base = run_intcode(code,[direction],position,base)
    if(result!=1):
        return

    oxygen.append([x,y])
    print('filled oxygen at '+str(time)+'min')
    time+=1

    for i in range(1,5):
        fill_with_oxy(i,oxygen,x,y,time,code,position,base)


data = Puzzle(year=2019, day=15).input_data.split(',')
code = list(map(lambda x : int(x),data))+list(np.zeros(1000))
position = 0
base = 0
x = 0
y = 0
path = []
visited=[]

for i in range(1,5):
    try_path([],i,visited,x,y,code,position,base)
