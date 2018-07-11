from decimal import Decimal
from decimal import getcontext
def piToNth(num): #Bailey–Borwein–Plouffe-algorithm
    pi = Decimal(0)
    k = 0
    while k < num:
        pi += ((Decimal(4/(8*k + 1))-Decimal(2/(8*k + 4))-Decimal(1/(8*k + 5))-Decimal(1/(8*k + 6))))* Decimal(16 **(-k))
        k += 1
    return pi 
num = Decimal(input("Give the position till which you want the Pi to be tracked: "))
getcontext().prec = int(num)
print(piToNth(num))