import numpy as np


start = 123257
end = 647015

def count_chars(s):
  arr = np.fromstring(s, dtype=np.uint8)

  unique_chars, char_counts = np.unique(arr, return_counts=True)

  return max(char_counts)

passes = []

for i in range(start,end):
    number = str(i)
    length = len(number)-1
    doubles = False
    triples = False
    stop = False
    for i in range(length):
        if(number[i] > number[i+1]):
            stop = True
            break
        if(number[i] == number[i+1]):
            if(i >= length - 1):
                if(number[i] != number[i-1]):
                    doubles = True
            elif(not(number[i] == number[i+1] and number[i] == number[i+2])):
                if(number[i] != number[i-1]):
                    doubles = True
    if(not stop and doubles==True):
        print(number)
        passes.append(number)


print(len(passes))