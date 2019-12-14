from aocd.models import Puzzle
import numpy as np
import math

class Reaction:
    def __init__(self,string):
        split = string.split(' => ')
        self.inputs = split[0].split(', ')
        self.inputs = list(map(lambda x: x.split(' '), self.inputs))
        self.output = split[1].split(' ')
    
    def has_output(self,output_name):
        return self.output[1]==output_name

    def has_input(self,input_name):
        for input in self.inputs:
            if(input[1]==input_name):
                return True
        return False

    def __str__(self):
        return str(self.inputs) + '\n' + str(self.output)

def find_reaction_with_output(reactions,output_name):
    for reaction in reactions:
        if reaction.has_output(output_name):
            return reaction
    # print('cannot find '+str(output_name))
    return False

rest = {}

def get_number_of_ore_for(required_qty,element,reactions):
    reaction = find_reaction_with_output(data,element)
    output_qty = int(reaction.output[0])
    reaction_multiplier = math.ceil(int(required_qty) / output_qty)
    rest_output = reaction_multiplier * output_qty - int(required_qty)
    if element in rest:
        rest[element]+=rest_output
    else:
        rest[element]=rest_output

    if(reaction.inputs[0][1]=='ORE'):
        return reaction_multiplier * int(reaction.inputs[0][0])
    else:
        ores = 0
        for input in reaction.inputs:
            input_qty = int(input[0]) * reaction_multiplier
            input_element = input[1]
            ores+=get_number_of_ore_for(input_qty,input_element,data)
        return ores

def try_substite_in_rest(rest,data):
    substituted = False
    for element in rest:
        qty = rest[element]
        if qty > 0:
            reaction = find_reaction_with_output(data,element)
            if(not reaction):
                continue
            output_qty = int(reaction.output[0])
            if(output_qty<=qty):
                reaction_multiplier = math.floor(int(qty) / output_qty)
                rest[element]-=output_qty*reaction_multiplier
                for input in reaction.inputs:
                    input_element = input[1]
                    input_qty = int(input[0])*reaction_multiplier
                    rest[input_element]+=input_qty
                substituted = True
    return substituted




data = Puzzle(year=2019, day=14).input_data.split('\n')
# data = '10 ORE => 10 A\n1 ORE => 1 B\n7 A, 1 B => 1 C\n7 A, 1 C => 1 D\n7 A, 1 D => 1 E\n7 A, 1 E => 1 FUEL'.split('\n')
# data = [
#     '9 ORE => 2 A',
#     '8 ORE => 3 B',
#     '7 ORE => 5 C',
#     '3 A, 4 B => 1 AB',
#     '5 B, 7 C => 1 BC',
#     '4 C, 1 A => 1 CA',
#     '2 AB, 3 BC, 4 CA => 1 FUEL'
# ]
data = list(map(lambda x : Reaction(x),data))
for reaction in data:
    for input in reaction.inputs:
        rest[input[1]]=0


ores = get_number_of_ore_for(1,'FUEL',data)
while(try_substite_in_rest(rest,data)):
    abc = 1

ores_per_fuel = ores-rest['ORE']
rest['ORE']=0
orig_rest = rest.copy()
for element in rest:
    rest[element]= 0

print(ores_per_fuel)
fuel = 0
ores = 1000000000000

for i in range(40):
    new_fuel = math.floor(ores/ores_per_fuel)
    # print(new_fuel)
    fuel+=new_fuel
    print(fuel)
    rest_ores = ores - new_fuel*ores_per_fuel

    for element in rest:
        rest[element]=rest[element]+orig_rest[element]*new_fuel

    while(try_substite_in_rest(rest,data)):
        abc=0

    ores = rest_ores + rest['ORE']
    rest['ORE']=0

# print(get_number_of_ore_for(1,'FUEL',data,{}))

