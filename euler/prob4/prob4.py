def reverse(n):
    reversed = 0
    while n > 0:
        reversed = 10*reversed + n%10
        n = n/10
    return reversed

def isPalindrome(n):
    return n == reverse(n)

largestPalindrome = 0
a = 999
while a>= 100:
    if a%11 == 0:
        b = 999
        db = 1
    else:
        b = 990
        db = 11
    while b >= a:
        if a*b <= largestPalindrome:
            break

        if isPalindrome(a*b):
            largestPalindrome = a*b

        b -= db
    a -= 1

print(largestPalindrome)
