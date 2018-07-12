from decimal import Decimal
from decimal import getcontext

def factorial(n):
    '''
    Factorial function to find the factorial of the functions
    https://en.wikipedia.org/wiki/Factorial
    
    '''
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

def piToNth(num):
    '''
     chudnovsky-algorithm to compute pi to 'num' digit
    https://en.wikipedia.org/wiki/Chudnovsky_algorithm

    '''
    pi = Decimal(0)
    k = 0
    while k < num:
        first = Decimal(-1)**(k)
        second = Decimal(factorial(6*k))
        third =  Decimal((545140134*k + 13591409))
        fourth = Decimal(factorial(3*k))
        fifth = Decimal((factorial(k)**3))
        sixth =  Decimal((640320)**((3*k+3)/2))
        pi += (first*second*third)/(fourth*fifth*sixth)
        k = k + 1 
    pi = (pi ** Decimal(-1)) / Decimal(12) 
    return pi 
num = Decimal(input("Give the position till which you want the Pi to be tracked: "))
getcontext().prec = int(num)
print(piToNth(num))


    