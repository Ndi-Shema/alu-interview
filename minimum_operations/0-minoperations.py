#!/usr/bin/python3

import math

def minOperations(n):
    '''
    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
    Example:

    n = 9

    H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

    Number of operations: 6
    :param n:
    :return:
    '''
    if n <= 0:
        return 0

    operations = 0
    i = 2
    while i <= n:
        while n % i == 0:
            operations += i
            n = n / i
        i += 1
    operations += n
    return operations
print(minOperations.__doc__)