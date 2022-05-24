"""
Given a set of numbers, return the additive inverse of each.
Each positive becomes negatives, and the negatives become positives.
"""
def invert(lst):
    new_lst = []
    for i in lst:
        new_lst.append(-i)
    return new_lst