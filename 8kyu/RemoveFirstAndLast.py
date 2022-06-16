"""It's pretty straightforward.
Your goal is to create a function that removes the
first and last characters of a string.
You're given one parameter, the original string. Y
ou don't have to worry with strings with less than two characters."""

def remove_char(s):
    return s[1:-1]


def remove_char1(s):
    print(s[1:len(s)-1])



remove_char1("one two three four five")

