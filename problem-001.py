"""
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples(x):
    """
    multiples of 3 and 5 below x
    """
    #number of  multiples of 3
    k3=(x-1)//3
    
    # number of multiples of 5
    k5=(x-1)//5
    
    # number of multiples of 15
    k15=(x-1)//15
    
    #sum of 3's multiples included 15's 
    a=3*k3*(k3+1)//2
    
    #sum of 5's multiples included 15's
    b=5*k5*(k5+1)//2
    
    #sum of 15's multiples
    c=15*k15*(k15+1)//2
    
    return a+b-c


print(multiples(1000))
