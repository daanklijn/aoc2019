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

def run_intcode(code,input_vars,position=0,relative_base=0,var_count=0):
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
            return(a,code,position,relative_base,var_count)
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

class Computer:
    def __init__(self,code,input_vars):
        self.code = code
        self.inputs = input_vars
        self.position = 0
        self.base = 0
        self.var_count = 0
    
    def run(self):
        output, self.code, self.position, self.base, self.var_count = run_intcode(self.code,self.inputs,self.position, self.base, self.var_count)
        return output


    
        
        
data = Puzzle(year=2019, day=23).input_data.split(',')
code = list(map(lambda x : int(x),data))+list(np.zeros(10000))
computers = []
queues = []
for i in range(50):
    computers.append(Computer(code.copy(),[i]))
    queues.append([])

nat_x=None
nat_y=None
prev_y=None

current = 0
loop_total = 0

while(True):
    if(current==50):
        if(loop_total==0):
            queues[0].append(nat_x)
            queues[0].append(nat_y)
            if(nat_y==prev_y):
                print(nat_y)
            prev_y = nat_y

        loop_total = 0
        current = 0
            
    comp = computers[current]
    if(len(queues[current])<1):
        comp.inputs.append(-1)
    else:
        comp.inputs += queues[current]
        queues[current] = []

    try:
        addr = computers[current].run()
        x = computers[current].run()
        y = computers[current].run()
        if(addr == 255):
            nat_x = x
            nat_y = y
        # print(addr,x,y)
        queues[addr].append(x)
        queues[addr].append(y)
        loop_total+=1
    except:
        current+=1

# for computer in computers:
#     addr = computer.run()
#     x = computer.run()
#     y = computer.run()
#     computers[addr].inputs.append(x)
#     computers[addr].inputs.append(y)
#     print(addr,x,y)





