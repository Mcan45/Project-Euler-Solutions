"""
    Largest prime factor
    Problem 3
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
"""
#!/bin/python3

import sys

def isPrime(x):
    """
        checks if x is prime
        !sieve of erostatenes!
    """

    ################## helper function ######################
    def isPrime_helper(n, p_list):
        """
            check prime numbers lower than sqrt(x), if any of these is not a factor of x than; x is prime
        """
        sqrt = n ** 0.5

        for i in p_list:
            if i <= sqrt and n % i == 0:
                return False
            elif i > sqrt:
                break
        return True
    ##########################################################

    prime_list = [2, 3]  # beginning of prime list
    # we will update prime list up to sqrt of x

    # if x is lower than 2
    if x <= 1:
        return False

    # if x is 2 0r 3
    elif x in prime_list:
        return True

    else:
        # square root of x
        sqrt = int(x**0.5)

        # extend prime_list up to sqrt of x
        for i in range(4, sqrt+1):
            if isPrime_helper(i, prime_list):
                prime_list.append(i)
        # now prime list is ok!

        # check is x is prime
        return isPrime_helper(x, prime_list)


def largest_prime_factor(number):
    #divide to 2**n
    while number % 2 == 0:
        # new number maybe the largest prime
        number //= 2
    
    if isPrime(number):
        return number
    

    #check only odd numbers grater than 2      
    n = 3  # number to divide
    while number > n:
        # if number is not prime divide number to n as a factor of number
        if number % n == 0:
            # new number maybe the largest prime
            number //= n
        else:
            # look for new prime
            # odd numbers increasing by 2
            n += 2
    # number is prime result is number
    return number



if __name__ == "__main__":

    print(largest_prime_factor(600851475143))
