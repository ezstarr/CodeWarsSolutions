"""
Take 2 strings s1 and s2 including only letters from ato z.
Return a new sorted string, the longest possible,
containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
    """
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"


def longest(a1, a2):
    if len(set_a1) > len(set_a2):
        print(len(set_a1))
        for i in set_a1:
            new_a1 += i
    else:
        for l in set_a2:
            new_a2 += l



longest(a,b)