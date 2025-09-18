#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Parameters:
        n (int): The number to calculate the factorial of. 
                 Must be a non-negative integer.

    Returns:
        int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
