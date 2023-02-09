#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return 0

    i = 2
    while i <= n // 2:
        if n % i == 0:
            return minOperations(n // i) + i
        i += 1
    return n