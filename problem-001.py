"""
Multiples of 3 and 5
Problem 1 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples(a, b, x):
    """
    multiples of a and b
    below x
    """
    sum = 0  # sum of multiples

    for i in range(1, x):
        # check i if multiple of a or b
        if i % a == 0 or i % b == 0:
            sum += i

    return sum


print(multiples(3, 5, 10))
