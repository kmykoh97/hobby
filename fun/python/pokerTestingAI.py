from random import *
# return cards values and shape in understandable numbers format
def numberized(tableCard, aiCard):
        number = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        shape = ['S','H','C','D']
        tCard =[]
        aCard = []
        tCard = progress(tableCard, number, shape)
        aCard = progress(aiCard, number, shape)
        return tCard, aCard

# 2 functions to determine whether to follow
def evaluator1(x):
    if x[0][0] == x[1][0]: return True
    elif x[randint(0,1)][0] > 10:
        if random() < 0.9: return True
    elif x[0][0] + x[1][0] >= 15:
        if randint(0,1) == 0: return False
    elif x[0][1] == x[1][1]:
        if random() < 0.8: return True
    elif randint(1,3) == 2: return True

def evaluator2(x, y, numberList, shapeList, numberCount, shapeCount):
    # consider value of cards:
    if y[0][0] >= x[randint(0,len(x)-1)][0]:
        if random() > 0.25: return evaluator1(x)
    # consider total value of cards:
    if y[0][0] + y[1][0] >= x[1][0] + x[randint(0,len(x)-1)][0]:
        if random() < 0.7: return evaluator1(x)
    # consider duplicated shape of cards:
    if shapeCount == 3:
        if random() < 0.65: return True
    elif shapeCount > 3: return True
    # consider duplicated or progression number of cards:
    if numberCount >= 3: return True
    for i in range(len(numberList)):
        if i+3 < len(numberList) and numberList[i]+1 == numberList[i+1] and numberList[i+1]+1 == numberList[i+2] and numberList[i+2]+1 == numberList[i+3]:
            if random() < 0.65: return True
        elif i+4 < len(numberList) and numberList[i]+1 == numberList[i+1] and numberList[i+1]+1 == numberList[i+2] and numberList[i+2]+1 == numberList[i+3] and numberList[i+3]+1 == numberList[i+4]: return True

def progress(card, number, shape):
    Card = []
    for a in range(len(card)) :
        for b in range(len(card[a])):
            if b==0:
                x = number.index(card[a][b])
            elif b==1:
                y = shape.index(card[a][b])
        Card.append([x,y])
    return Card

# return a list of numbers and shapes combined
def groupNS(tCard,aCard):
    number, shape = [], []
    for a in range(len(tCard)):
        number.append(tCard[a][0])
        shape.append(tCard[a][1])
    for a in range(len(aCard)):
        number.append(aCard[a][0])
        shape.append(aCard[a][1])
    return number, shape

# return the highest count of same shape and number in both decks
def similarCount(number, shape):
    numcount, shapecount = 0, 0
    for a in range(13):
        temp = number.count(a)
        if temp > numcount:
            numcount = temp
    for a in range(4):
        temp = shape.count(a)
        if temp > shapecount:
            shapecount = temp
    return numcount, shapecount

def AI(x, y):
    # x is ai card, y is table card
    y, x = numberized(y, x)
    numberList, shapeList = groupNS(y, x)
    numberCount, shapeCount = similarCount(numberList, shapeList)
    # condition when no cards on table yet
    if len(y) == 0:
        if evaluator1(x): return True
        elif random() < 0.65: return True
        return False
    # condition when cards on table not yet completed
    elif len(y) == 3 or len(y) == 4:
        if evaluator2(x, y, numberList, shapeList, numberCount, shapeCount):
            return True
        # consider when no above condition satisfied:
        if randint(0, 2) == 0: return evaluator1(x)
        return False
    # condition when cards are fully displayed on table
    elif len(y) == 5:
        return True

def main():
    if AI([['A','H'],['7','H']], [['J','D'],['4','D'],['2','S'],['8','H'],['9','D']]):
        print 'a'
    else: print "b"

main()
