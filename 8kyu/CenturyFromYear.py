"""Introduction
The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Task
Given a year, return the century it is in.

Examples
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20"""


def century(year):
    print((year//100)+(year % 100 > 0))


#======= Loosely Typed: data can change data types.

# TIL that this will print "2"
print(1 + True)

# This prints "1"
print(True+0)

# This prints "2"
print(True+True)

# This prints 4
print(True+True+True + 1)
