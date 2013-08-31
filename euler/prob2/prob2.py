fb1 = 1
fb2 = 2
fibEvenSum= 0

def fibSumEven(fb1, fb2):
    global fibEvenSum
    
    if fb2 <= 4000000:
        if fb2%2 == 0:
            fibEvenSum += fb2
    else:
        return fibEvenSum
    temp = fb1+fb2
    fb1 = fb2
    fb2 = temp
    fibSumEven(fb1, fb2)

fibSumEven(fb1, fb2)

print(fibEvenSum)
    
