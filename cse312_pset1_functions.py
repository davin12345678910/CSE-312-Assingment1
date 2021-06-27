"""
This starter code is written by Pemi Nguyen. Permission is
hereby granted to students registered for University of Washington
CSE 312 (originally written for Fall 2020) for use solely for purposes of
the course.  No other use, copying, distribution, or modification
is permitted without prior written consent.
"""

"""
Task 1:
Write the method find_max, which takes two integer parameters and returns the larger one.
If they are equal, return which ever.
"""

from typing import List, Tuple
import math
# TODO

def find_max(x: int, y: int) -> int:
    if x > y: 
        return x
    elif x < y:
        return y
    else:
        return x        
"""
Task 2:
One of the differences between Python and other programming languages is that it can return
multiple values in a function (even with different types).
In this task, you will write a function called sum_and_prod(), which takes two integer parameters
and return the sum and product of the two.
(Remember, the return values are ordered, so you need to return the sum first and the product second).
"""
# TODO
def sum_and_prod(x: int, y: int) -> Tuple[int, int]:
    sum = x + y
    product = x * y
    return sum, product

    
if __name__ == "__main__":
    print("Task 1:")
    print(find_max(3, 6))

    print("Task 2:")
    s, p = sum_and_prod(4, 7)
    print("Sum = {}".format(s))
    print("Product = {}".format(p))