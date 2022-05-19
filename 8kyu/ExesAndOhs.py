"""
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case in-sensitive.
The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""
def xo(s):
    exes = 0
    ohs = 0
    new_s = s.lower()
    for i in new_s:
        if i == "x":
            exes += 1
    for i in new_s:
        if i == "o":
            ohs += 1
    if exes == ohs:
        return True
    else:
        return False
