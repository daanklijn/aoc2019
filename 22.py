from aocd.models import Puzzle
import numpy as np
import math

def handle_move(move,cards):
    if(move[0]=='n'):
        cards.reverse()
        return cards
    elif(move[0]=='c'):
        n = int(move[1])
        return cards[n:] + cards[0:n]
    elif(move[0]=='i'):
        n = int(move[1])
        result = [-1] * len(cards)
        index = 0
        for card in cards:
            result[index]=card
            index+=n
            if(index>=len(cards)):
                index = index%len(cards)
        return result
    else:
        print("Invalid move")

        


data = Puzzle(year=2019, day=22).input_data
# data = """deal into new stack
# cut -2
# deal with increment 7
# cut 8
# cut -4
# deal with increment 7
# cut 3
# deal with increment 9
# deal with increment 3
# cut -1"""
data = data.replace('deal into new stack','n')
data = data.replace('deal with increment','i')
data = data.replace('cut','c')
data = data.split('\n')
data = list(map(lambda x: x.split(' '),data))

cards = list(range(10007))
for i in range(1000):
    for move in data:
        cards = handle_move(move,cards)
    print(cards[0])
