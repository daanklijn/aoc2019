from aocd.models import Puzzle
import numpy as np


data = Puzzle(year=2019, day=1).input_data.split('\n')

def get_fuel(weight):
    fuel = int(int(weight) / 3) - 2
    if fuel <=0: 
        return 0
    else:
        return fuel


total = 0
for value in data:
    fuel = get_fuel(value)
    total+=fuel
    fuels_fuel= get_fuel(fuel)
    while fuels_fuel > 0:
        total+=fuels_fuel
        fuels_fuel = get_fuel(fuels_fuel)

print(total)

