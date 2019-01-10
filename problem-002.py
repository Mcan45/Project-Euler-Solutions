"""
Even Fibonacci numbers
------------------------------------------ 
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def sum_of_even_fibo(n):
    """
    contains the fibonacci squence in a list
    and returns sum of even terms up to last term < value(n)
    """

    fibo_list = [1, 2]  # contains the fibonacci numbers
    sum_even = 2  # begin of sum
    if n <= 2:
        return 2
    else:
        while True:
            fibo_list.append(fibo_list[-1]+fibo_list[-2])
            k = fibo_list[-1]
            if k >= n:
                break
            if k % 2 == 0:
                sum_even += k
    return sum_even


print(sum_of_even_fibo(4*10**6))
