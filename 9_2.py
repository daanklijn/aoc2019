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








