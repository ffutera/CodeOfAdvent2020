import string
import math

f = open("day5.txt", "r")
data = f.read().split("\n")
taken = []
available = []

for seat in data:
    rowd  =  list(seat[0:7])
    cold = list(seat[7:10])
    
    rowrange =  [0,127]
    for r in rowd:
        if r == 'B':
            rowrange[0] = math.ceil((rowrange[1] - rowrange[0])/2 + rowrange[0])
        else:
            rowrange[1] = math.floor((rowrange[1]-rowrange[0])/2 + rowrange[0])

    colrange = [0,7]
    for c in cold:
        if c == 'R':
            colrange[0] = math.ceil((colrange[1] - colrange[0])/2 + colrange[0])
        else:
            colrange[1] = math.floor((colrange[1]-colrange[0])/2 + colrange[0])
    row = rowrange[0]
    col = colrange[0]
    seatid = row*8+col
    taken.append(seatid)

for i in range(127*8+7):
    if not i in taken and i+1 in taken and i-1 in taken:
        available.append(i)

print(available)
