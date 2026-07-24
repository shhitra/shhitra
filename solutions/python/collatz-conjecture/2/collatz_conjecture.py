"""
This is a funtion used to determine the number of steps itterated to reach to the number one using Collatz Conjecture
"""

def steps(number):
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