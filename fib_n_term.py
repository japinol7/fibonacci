"""Benchmarks some algorithms that calculate the n element of the Fibonacci sequence.
The Fibonacci sequence:  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Where F(0) = 0, F(1) = 1 and F(n) = F(n - 1) + F(n - 2) for n > 1.
So, each term greater than 1 is generated by adding the previous two terms.
For example, the 6th element of the sequence is 8.
Most algorithms contained here do not expect negative numbers;
so, if a negative number is supplied their behavior is undefined.
"""
__author__ = 'Joan A. Pinol  (japinol)'

import logging
import traceback

from fibonacci.fib1_rec import fib as fib1
from fibonacci.fib2_ite import fib as fib2
from fibonacci.fib3a_rec_mem_list import fib as fib3a
from fibonacci.fib3b_rec_mem_arr import fib as fib3b
from fibonacci.fib4_rec_mem_dic import fib as fib4
from fibonacci.fib5_rec_mem import fib as fib5
from fibonacci.fib6_rec_mem import fib as fib6
from fibonacci.time_it import time_it


logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def write_result(res, n):
    print(f"fib({n}): {res}\n{'-'*10}")


def main():
    n = 35  # Term to calculate

    print("> A recursive approach without optimizations:")
    if n < 36:
        res = time_it(fib1, n)
        write_result(res, n)
    else:
        print(f"fib({n}): Oops! It will take so much time, so I abort it. Sorry.\n{'-'*10}")

    print("> An iterative programming solution:")
    res = time_it(fib2, n)
    write_result(res, n)

    print("> A dynamic programming memoized solution\n"
          "for a recursive approach using a list:")
    res = time_it(fib3a, n)
    write_result(res, n)

    print("> A dynamic programming memoized solution for a recursive approach\n"
          "using an array of unsigned integers of 64 or 32 bits:")
    res = time_it(fib3b, n)
    write_result(res, n)

    print("> A dynamic programming memoized solution using a dictionary:")
    res = time_it(fib4, n)
    write_result(res, n)

    print("> A dynamic programming memoized solution for a recursive approach\n"
          "using functools.lru_cache from the standard library:")
    res = time_it(fib5, n)
    write_result(res, n)

    print("> A dynamic programming memoized solution for a recursive approach\n"
          "using functools.lru_cache from the standard library.\n"
          "Benchmarks function fib with the user created decorator time_it:")
    res = fib6(n)
    write_result(res, n)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        logger.critical(f'Error: {e}')
