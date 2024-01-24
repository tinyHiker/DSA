def sumDigits(n):
    assert n >= 0 and int(n) == n, "The number has to be a positive integer only!"
    if n == 0:
        return 0
    else:
        return int(n%10) + sumDigits(int(n/10))
    
    
def powerNum(x, n):
    if n==1:
        return x
    else:
        return x * powerNum(x, n-1)
    
number = powerNum(2, 3)
print(number)