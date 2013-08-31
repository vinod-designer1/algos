sumMultiples = 0

for i in range(3,1000):
    if i%15 == 0:
        sumMultiples += i
    elif i%5 == 0:
        sumMultiples += i
    elif i%3 == 0:
        sumMultiples += i

print(sumMultiples)
