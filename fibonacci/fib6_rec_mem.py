"""Calculates the n element of the Fibonacci sequence.
The Fibonacci sequence:  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Where F(0) = 0, F(1) = 1 and F(n) = F(n - 1) + F(n - 2) for n > 1.
So, each term greater than 1 is generated by adding the previous two terms.
For example, the 6th element of the sequence is 8.
It uses a dynamic programming memoized solution for a recursive approach
using functools.lru_cache from the standard library.
Benchmarks function fib with the user created decorator time_it.
Applying functools.wraps to the wrapper closure returned by the decorator
carries over the docstring and other metadata of the input function.
"""
__author__ = 'Joan A. Pinol  (japinol)'

from functools import lru_cache

from fibonacci.time_it_dec import time_it


@lru_cache(maxsize=None)
def fib_n(n):
    if n < 2:
        return n
    return fib_n(n - 1) + fib_n(n - 2)


@time_it
def fib(n):
    if n < 0:
        return None
    return fib_n(n)


if __name__ == "__main__":
    n = 35
    res = fib(n)
    print(f'fib({n}): {res}')
