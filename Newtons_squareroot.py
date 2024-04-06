'''
Created on Apr 3, 2024

@author: Administrator
'''
def newtonSqrt(n, howmany):
    approx = 0.5 * n
    for i in range(howmany):
        betterapprox = 0.5 * (approx + n/approx)
        approx = betterapprox
    return betterapprox

print(newtonSqrt(100, 10))
print(newtonSqrt(4, 10))
print(newtonSqrt(1, 10))