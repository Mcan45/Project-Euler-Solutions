"""
    Largest prime factor
    Problem 3
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
"""


if __name__ == "__main__":

    number = 600851475143  # the given number

    n = 2  # number to divide
    while number > n:
        # if number is not prime divide number to n as a factor of number
        if number % n == 0:
            # new number maybe the largest prime
            number //= n
        else:
            # look for new prime
            n += 1
    # number is prime result is number

    print("result:", number)
