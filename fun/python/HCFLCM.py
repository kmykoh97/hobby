#A program to find LCM, HCF
#Created by MyKoh
#2017-10-20

#Input: Integer a, b, c
#Output: HCF, LCM of a, b, c

# linear way
def LCM(a,b,c):
    #a, b, c = input('Please insert 3 numbers saparated by ,:')
    truthValue = True
    multipleA, multipleB, multipleC = 1, 1, 1
    newA, newB, newC = a, b, c
    while truthValue:
        newA = a * multipleA
        multipleA += 1
        while newB < newA:
            newB = b * multipleB
            multipleB += 1
        while newC < newA:
            newC= c * multipleC
            multipleC += 1

        if newA - newB == 0 and newA - newC == 0:
            truthValue = False

    print 'LCM is', str(newA)

   #alternative LCM: use lower number in that 3 and add 1 by 1 and if x % y== 0, lcm
   #alternative: 3x for loops

#LCM()

def HCF(a,b,c):
    #a, b, c = input('Please insert 3 numbers saparated by ,:')
    listA = []
    listB = []
    listC = []
    resultList = []
    for i in range(1, a+1):
        for j in range(i, a+1):
            if i * j == a:
                listA.append(i)
                listA.append(j)

    for i in range(1, b+1):
        for j in range(i, b+1):
            if i * j == b:
                listB.append(i)
                listB.append(j)

    for i in range(1, c+1):
        for j in range(i, c+1):
            if i * j == c:
                listC.append(i)
                listC.append(j)

    for i in listA:
        for j in listB:
            for k in listC:
                if i == j == k:
                    resultList.append(i)

    print 'HCF is', str(max(resultList))

#HCF()

#control function
def main1():
    a, b, c = input('Please insert 3 numbers saparated by ,:')
    LCM(a,b,c)
    HCF(a,b,c)
    print 'This code is very complicated. Have fun studying XD'

# main1()

# recursive way
def main():
    a, b = input("Please insert 2 numbers for hcf: ")
    global hcf
    hcf = hcf(a,b) # for better efficiency
    print "LCM is:", lcm(a, b)
    print "HCF is:", hcf

def lcm(a, b):
    return a * b / hcf

"""
# second recursive way of finding LCM:
# this code is very inefficient althought it is recursive. It is even more inefficient than linear
def lcmForceRecursive(x, y, counter=1):
    if (counter%x == 0 and counter%y == 0):
        return counter
    return lcm(x, y, counter+1)

print lcmForceRecursive(2, 4)
"""

def hcf(a, b):
    if b == 0: return a
    else:
        return hcf(b, a%b)

main()
