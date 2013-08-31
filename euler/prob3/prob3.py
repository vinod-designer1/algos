import math

def findLargePrimeFactor(s):
    lastFactor = 0
    if s%2 == 0:
        s = s/2
        lastFactor = 2
        while s%2 == 0:
            s = s/2
    else:
        lastFactor = 1
        
    p = math.sqrt(s)
    factor = 3
    while s > 1 and factor <= p:
        if s%factor == 0:
            s = s/factor
            lastFactor = factor
            while s%factor == 0:
                s = s/factor
            p = math.sqrt(s)
        factor += 2
    if s == 1:
        print(lastFactor)
    else:
        print(s)

findLargePrimeFactor(600851475143)
        
