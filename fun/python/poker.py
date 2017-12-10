# class poker:
#
#     def __init__(self):
#
#     def
#
# def main():
#
# main()
fom random import *

def AI(x,y):
    # compare own card
    if x[0][0] == x[1][0] and x[0][0] >= y[1][0] and len(y) == 3:
        if random() < 0.85:
            return True
    #compare total value
    if x[0][0] + x[1][0] >= y[1][0] + y[randint(0,len(y)-1)][0]:
        if random() < 0.6:
            return True
    # compare color
    colourList = [x[0][1], x[1][1]]
    for i in range(len(y)):
        colourList += [y[i][1]]
    colourList.sort()
    for i in range(len(colourList)):
        if colourList[i] == colourList[i+1] == colourList[i+2] and i+2 <= len(colourList)-1:
            if random() < 0.55:
                return True
        if colourList[i] == colourList[i+1] == colourList[i+2] == colourList[i+3] and i+3 <= len(colourList)-1:
            if random() < 0.67:
                return True
        if colourList[i] == colourList[i+1] == colourList[i+2] == colourList[i+3] == colourList[i+4] and i+4 <= len(colourList)-1:
            return True
    # compare bot and table
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i][0] == y[j][0] and x[i][0] >= y[randint(0,len(y)-1)][0]:
                if random() < 0.85:
                    return True
