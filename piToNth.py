from decimal import *
getcontext().prec = 25
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

def piToNth(num):
    pi = Decimal(0)
    k = 0
    while k < num:
        pi += (Decimal(-1)**(k) * Decimal(factorial(6*k)) * Decimal((545140134*k + 13591409))) / (Decimal(factorial(3*k)) * Decimal((factorial(k)**3)) * Decimal((640320)**((3*k+3)/2)))
        k = k + 1 
    pi = (pi ** Decimal(-1)) / Decimal(12) 
    return pi 



    