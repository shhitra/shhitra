"""
This python file is used for Collatz Conjecture
"""

def steps(number):
    """
    This funtion is used to find out the number of itterations it took for a user given number to     reach the value 1
    """
    if number<1:
        raise ValueError("Only positive integers are allowed")
    count=0
    while number != 1:
        if number%2==0:
            number= number//2
        else:
            number= 3 *number +1
        count+=1
    return count