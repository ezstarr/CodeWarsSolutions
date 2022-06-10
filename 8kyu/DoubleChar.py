"""
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
"""

def double_char(s):
    output = ""
    new_s = [(i+i) for i in ''.join(s)]
    for i in new_s:
        output += i
    return output


def double_char1(s):
    return ''.join(c*2 for c in s)


double_char1("String")