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
    print(minOperations.__doc__)
    if type(n) is not int or n <= 0:
        return 0
    operations = 0
    H = 1
    copy_all = 0
    paste = 0
    H_copied = 0
    while H < n:
        if n % H == 0:
            copy_all += 1
            H_copied = H
        paste += 1
        operations = copy_all + paste
        H += H_copied
    return operations

