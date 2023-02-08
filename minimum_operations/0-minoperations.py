#!/usr/bin/python3

def minOperations(n):
    """turn 0 if n is less than or equal to 0"""
    if n <= 0:
        return 0

    """Initialize a variable to store the number of operations"""
    operations = 0

    """Start with the smallest factor, 2"""
    i = 2

    """Keep dividing n by i until n is no longer divisible by i"""
    while i <= n:
        while n % i == 0:
            operations += i
            n = n / i
        i += 1

    """Add the remaining value of n to operations"""
    operations += n

    """Return operations as an integer"""
    return int(operations)
