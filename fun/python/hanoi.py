# Hanoi
# Created by MyKoh
# 2018-02-06

# There are 3 Hanoi Towers and the plates are in the middle. We need to shift the plates to the left accordingly
# I am going to solve it using recursion

def main():
    numberOfPlates = input("Please insert number of plates you wish to have:")
    hanoi(numberOfPlates, 2, 1, 3)

def printResult(fr, to):
    print "move plate from " + str(fr) + " to " + str(to)

def hanoi(n, fr, to, spare):
    if n == 1:
        printResult(fr, to)
    else:
        hanoi(n-1, fr, spare, to)
        hanoi(1, fr, to, spare)
        hanoi(n-1, spare, to, fr)

main()
