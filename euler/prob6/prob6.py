def squareOfSum(n):
    return ((n*(n+1))/2)**2

def sumOfSqr(n):
    return (n*(n+1)*(2*n+1))/6

print(squareOfSum(100)-sumOfSqr(100))
