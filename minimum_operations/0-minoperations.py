#!/usr/bin/python3
"""
  In a text file, there is a single character H. Your text editor can execute only two operations in this file:
  Copy All and Paste. Given a number n,
  write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
  """


def minOperations(n):
    # If n is 1, 0 operations are needed.
    if n <= 1:
        return 0

    # Find smallest prime factors
    for i in range(2, int((n / 2) + 1)):
        if n % i == 0:
            return minOperations(int(n / i)) + i
    return n
