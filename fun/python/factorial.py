#Factorial Project
#Created by MyKoh
#2017-09-20

# linear way of doing factorial
print 'This a a program to find factorial'
def factorial():
    n = input('Please insert a whole number:')
    x = 1L #Use a long integer here
    for i in range(2, n+1):
        x *= i
    print 'Factorial of', n, 'is', x

# factorial()


# recursive way of doing factorial
def fac(n):
    if n == 1:
        return 1
    else: return n * fac(n-1)

def main():
    n = input('Please insert a whole number: ')
    print fac(n)

main()
