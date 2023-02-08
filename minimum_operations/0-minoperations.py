#!/usr/bin/python3

import math


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0

    i = 1
    copy = i
    while i < n:
        if n % i == 0:
            copy = i
            i = 2 * copy
            operations += 2
        else:
            i += copy
            operations += 1
    return operations
