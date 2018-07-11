from decimal import Decimal
from decimal import getcontext
def piToNth(num): #Bailey–Borwein–Plouffe-algorithm
    pi = Decimal(0)
    k = 0
    while k < num:
        pi += (((4/(8*k + 1))-(2/(8*k + 4))-(1/(8*k + 5))-(1/(8*k + 6))))*16 **(-k)
        k += 1
    return pi 
num = Decimal(input("Give the position till which you want the Pi to be tracked: "))
getcontext().prec = int(num)
print(piToNth(num))