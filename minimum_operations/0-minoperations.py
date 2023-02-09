#!/usr/bin/python3
"""
  Arguments :
  :param n:
  :return:
  """
def minOperations(n):
    """
    Arguments :
    :param n:
    :return:
    """
    # If n is 1, 0 operations are needed.
    if n <= 1:
        return 0

    # Find smallest prime factors
    for i in range(2, int((n / 2) + 1)):
        if n % i == 0:
            return minOperations(int(n / i)) + i
    return n

