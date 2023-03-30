"""
Write a function called "factorPrime" that takes an integer as input, and returns the prime factorization of the input.
"""

def factorPrime(n):
    f = 2
    if n == 1:
        print('1 x 1')
    if n == 0 or n < 0:
        print('invalid number')
    result = str(n) + ' = '
    while n > 1:
        if n % f == 0:
            n = int(n / f)
            result += str(f) + ' x '
        else:
            f += 1
    print(result[:len(result) - 3])

factorPrime(120)
factorPrime(1207)
factorPrime(964)