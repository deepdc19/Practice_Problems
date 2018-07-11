from decimal import Decimal
from decimal import getcontext
def piToNth(num): 
    """
     Bailey–Borwein–Plouffe-algorithm to compute pi to `num` digit
    https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
    
    """
    pi = Decimal(0)
    k = 0
    while k < num:
        first =  Decimal(4/(8*k + 1))
        second = Decimal(2/(8*k + 4))
        third = Decimal(1/(8*k + 5))
        fourth = Decimal(1/(8*k + 6)) 
        fifth = Decimal(16 **(-k))
        pi += (first - second - third - fourth) * fifth 
        k += 1
    return pi 
num = Decimal(input("Give the position till which you want the Pi to be tracked: "))
getcontext().prec = int(num)
print(piToNth(num))