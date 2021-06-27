"""
This starter code is written by Pemi Nguyen. Permission is
hereby granted to students registered for University of Washington
CSE 312 (originally written for Fall 2020) for use solely for purposes of
the course.  No other use, copying, distribution, or modification
is permitted without prior written consent.
"""

from typing import List, Tuple

def make_lists(n:int) -> Tuple[List[int], List[int]]:
    """
    Generate a list l1 that has n elements which are multiples of 3: [0, 3, 6, ... ,3(n-1)]
    Notice that you can use list comprehension to shorten the initialization
    """
    # 
    l1 = []
    for i in range(0, n):
        l1.append(3 * i)
    """
    Add 30 to the end of l1.
    """
    # TODO
    l1.insert(len(l1), 30)
    """
    Add 0 as to the beginning of l1.
    """
    # TODO
    l1.insert(0, 0)

    """
    Create another list l2 with the same elements as l1 except for its last element
    Add 312 to the end of l2.
    """
    # TODO
    l2 = []
    for i in range(0, len(l1)):
        l2.append(l1[i])
    del l2[len(l2) - 1]  
    l2.append(312)

    """
    Remove the second-last element of l2.
    """
    # TODO
    del l2[len(l2) - 2]

    # Return two lists l1 and l2
    return l1, l2

if __name__ == "__main__":
    l1, l2 = make_lists(n=4)
    print("l1 = {}".format(l1))
    print("l2 = {}".format(l2))