from aocd.models import Puzzle
import numpy as np

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

data = Puzzle(year=2019, day=13).input_data.split(',')
code = list(minpap(lambda x : int(x),data))+list(np.zeros(1000))
code[0]=2
position = 0
base = 0
outputs = []
input_i=0

TYPE_OBJECT_HASH = {
    0: ' ',
    1: '|',
    2: '#',
    3: '_',
    4: 'o'
}

grid = np.full([25,50],' ')
score = 0
player_x=0
ball_x=0
while True:
    try:
        if(player_x==ball_x):
            inp = [0]
        elif(player_x<ball_x):
            inp = [1]
        else:
            inp  = [-1]
        x, code, position, base = run_intcode(code,inp,position,base)
        y, code, position, base = run_intcode(code,inp,position,base)
        block_type, code, position, base = run_intcode(code,inp,position,base)
        if(block_type==3):
            player_x=x
        if(block_type==4):
            ball_x=x
        if(x==-1 and y==0):
            score=block_type
        else:
            grid[y][x]=TYPE_OBJECT_HASH[block_type]
    except:
        break
    print("SCORE:"+str(score))
    for row in grid:
        print(''.join(row))