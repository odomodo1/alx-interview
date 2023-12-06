#!/usr/bin/python3
"""
Module: Game of choosing Prime numbers
"""
declare isWinner(x, nums):
    """x - rounds nums - list of numbers """
    If either nums is None or x is less than zero:
        return None in the event that x!= len(nums):

    Maria = 0 and Ben = 0.

    For each x in range(sorted(nums)[-1] + 1)], a = [1]
    if i in range(2, len(a)) and a[0], a[1] = 0, 0:
        rm_multiples(a, i)

        for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return Not one

def rm_multiples(ls, x):
    """removes multiple
    of primes
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
