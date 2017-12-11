from random import *

def AI(a,b):
    # x is table, y is hand
    # print a,b
    x,y = numberized(b,a)
    if len(x) == 0:
        if y[0][0] == y[1][0]:
            if random() < 0.85:
                return True
            else: return False
        elif random() < 0.72:
            return True
        return False
    if y[0][0] == y[1][0] and y[0][0] >= x[randint(0,len(x)-1)][0]:
        if random() < 0.77:
            return True
    # compare total value
    if y[0][0] + y[1][0] >= x[1][0] + x[randint(0,len(x)-1)][0]:
        if random() < 0.7:
            return True
    # compare color
    colourList = [y[0][1], y[1][1]]
    for i in range(len(x)):
        colourList += [x[i][1]]
    colourList.sort()
    for i in range(len(colourList)):
        if i+2 < len(colourList) and colourList[i] == colourList[i+1] == colourList[i+2]:
            if random() < 0.65:
                return True
        if i+3 < len(colourList) and colourList[i] == colourList[i+1] == colourList[i+2] == colourList[i+3]:
            if random() < 0.80:
                return True
        if i+4 < len(colourList) and colourList[i] == colourList[i+1] == colourList[i+2] == colourList[i+3] == colourList[i+4]:
            return True
    # compare bot and table
    for i in range(len(y)):
        for j in range(len(x)):
            if y[i][0] >= x[j][0] and y[i][0] >= x[randint(0,len(x)-1)][0]:
                if random() < 0.79:
                    return True
    # make sure ai will not fold card during last few rounds
    if len(x) == 4:
        if random() < 0.9:
            return True
    elif len(x) == 5: return True
    return False


def numberized(tableCard, aiCard):
        number = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        shape = ['S','H','C','D']
        tCard =[]
        aCard = []
        tCard = progress(tableCard,number,shape)
        aCard = progress(aiCard,number,shape)
        return tCard,aCard

def progress(card,number,shape):
        Card = []
        for a in range(len(card)) :
                for b in range(len(card[a])):
                        if b==0:
                                x = number.index(card[a][b])
                        elif b==1:
                                y = shape.index(card[a][b])
                Card.append([x,y])
        return Card

def main():
        if AI([['J','S'],['K','D']], [['3','C'],['A','H'],['6','D']]):
            print 'a'
        else:
            print "b"


main()
