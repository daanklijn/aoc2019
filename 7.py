from aocd.models import Puzzle
import numpy as np
import itertools



def get_value(mode,position,code):
    if(mode==0):
        return code[code[position]]
    elif(mode==1):
        return code[position]
    else:
        print("WRONG MODE")

def get_location(mode,position,code):
    if(mode==0):
        return code[position]
    else:
        print("Cannot get location for other mode")

def run_intcode(code,input_vars,position=0):
    # print(code)
    # print(position)
    # print(input_vars)
    var_count=0

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
            a = get_value(mode1,position+1,code)
            b = get_value(mode2,position+2,code)
            c = get_location(mode3,position+3,code)
            code[c]=a+b
            position+=4
        elif(opcode == 2):
            a = get_value(mode1,position+1,code)
            b = get_value(mode2,position+2,code)
            c = get_location(mode3,position+3,code)
            code[c]=a*b
            position+=4
        elif(opcode == 3):
            a = get_location(mode1,position+1,code)
            code[a] = input_vars[var_count]

            var_count+=1
            position+=2
        elif(opcode == 4):
            a = get_value(mode1,position+1,code)
            position+=2
            return(a,code,position)
        elif(opcode == 5):
            a = get_value(mode1,position+1,code)
            b = get_value(mode2,position+2,code)
            if(a != 0):
                position=b
            else:
                position+=3
        elif(opcode == 6):
            a = get_value(mode1,position+1,code)
            b = get_value(mode2,position+2,code)
            if(a == 0):
                position=b
            else:
                position+=3
        elif(opcode == 7):
            a = get_value(mode1,position+1,code)
            b = get_value(mode2,position+2,code)
            c = get_location(mode3,position+3,code)
            if(a < b):
                code[c]=1
            else:
                code[c]=0
            position+=4
        elif(opcode == 8):
            a = get_value(mode1,position+1,code)
            b = get_value(mode2,position+2,code)
            c = get_location(mode3,position+3,code)
            if(a == b):
                code[c]=1
            else:
                code[c]=0
            position+=4
                
            

        else:
            print("wrong op" + str(instruction))

def run_amp_program(values,setting):
    input = 0
    for i in setting:
        input=run_intcode(values,[i,input])
    return input

def run_feedback_amp_program(values,setting):
    output1, state1, position1 = run_intcode(values.copy(),[setting[0],0],position=0)
    output2, state2, position2 = run_intcode(values.copy(),[setting[1],output1],position=0)
    output3, state3, position3 = run_intcode(values.copy(),[setting[2],output2],position=0)
    output4, state4, position4 = run_intcode(values.copy(),[setting[3],output3],position=0)
    output5, state5, position5 = run_intcode(values.copy(),[setting[4],output4],position=0)

    while(True):
        try:
            output1, state1, position1 = run_intcode(state1,[output5],position=position1)
            output2, state2, position2 = run_intcode(state2,[output1],position=position2)
            output3, state3, position3 = run_intcode(state3,[output2],position=position3)
            output4, state4, position4 = run_intcode(state4,[output3],position=position4)
            output5, state5, position5 = run_intcode(state5,[output4],position=position5)
        except:
            break
    print(output5)
    return output5



data = Puzzle(year=2019, day=7).input_data.split(',')

values = list(map(lambda x : int(x),data))
# values = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# print(run_amp_program(values,[4,3,2,1,0]))
# values = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
# 101,5,23,23,1,24,23,23,4,23,99,0,0]
# print(run_amp_program(values,[0,1,2,3,4]))
# values = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
# 1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
# print(run_amp_program(values,[1,0,4,3,2]))
# values = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
# print(run_feedback_amp_program(values,[9,8,7,6,5]))
# values = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
# -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
# 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
# print(run_feedback_amp_program(values,[9,7,8,5,6]))


settings = list(itertools.permutations([5,6,7,8,9]))

max = 0
for setting in settings:
    output = run_feedback_amp_program(values,setting)
    if output>max:
        max = output

print(max)





