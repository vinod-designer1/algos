import math

k = 20
N = 1
i = 0
a = {}
check = True
limit = math.sqrt(k)

p = [2,3,5,7,11,13,17,19,23]

while p[i] <= k:
    a[i] = 1
    if check:
        if p[i] <= limit:
            a[i] = math.floor(math.log(k,p[i]))
        else:
            check = False
    N *= (p[i]**a[i])
    i += 1

print(N)
        

