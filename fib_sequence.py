'''Calculates the first n elements of the Fibonacci sequence.
The Fibonacci sequence:  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Where F(0) = 0, F(1) = 1 and F(n) = F(n - 1) + F(n - 2) for n > 1.
So, each term greater than 1 is generated by adding the previous two terms.
For example, the 6th element of the sequence is 8.
It uses an iterative programming solution.
'''
__author__ = 'Joan A. Pinol  (japinol)'

import logging
import traceback


from fibonacci.fib_seq1_ite import fib as fib1
from fibonacci.fib_seq2_ite import fib as fib2
from fibonacci.fib_seq3_ite_gen import fib_list as fib3


logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def write_result(res, n):
    print(f"fib({n}): {res}\n{'-'*10}")


def main():
    n = 35  # Last term to calculate

    print("> It uses an iterative programming solution and returns the sequence as a list.")
    res = fib1(n)
    write_result(res, n)

    print("> An iterative programming solution using a list in the very algorithm.")
    res = fib2(n)
    write_result(res, n)

    print("> An iterative programming solution using a user generator.\n"
          "  It is later converted to a list to time it. But it should be used as a generator.")
    res = fib3(n)
    write_result(res, n)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        logger.critical(f'Error: {e}')