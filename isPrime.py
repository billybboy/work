"""
A function that takes an integer as input,
and returns a boolean value that indicates if the input number is prime.
"""

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(isPrime(1)) # returns false
print(isPrime(5)) # returns true
print(isPrime(91)) # returns false
print(isPrime(1000000)) # returns false