"""Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]"""


def maps(a):
    doubled_a = []
    for i in a:
        doubled_a.append(i * 2)
    return doubled_a


# alternative solution


def maps2(a):
    return [i*2 for i in a]
