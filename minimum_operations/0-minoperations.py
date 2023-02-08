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
    if n <= 1:
        return 0
    number = 1
    copy = number
    operations = 0
    while number < n:
        if n % number == 0:
            copy = number
            number = 2 * copy
            operations += 2
        else:
            number += copy
            operations += 1
    return operations


print(minOperations.__doc__)
