"""Given an integer n and two other values,
 build an array of size n filled with these two values alternating.

Examples
5, true, false     -->  [true, false, true, false, true]
10, "blue", "red"  -->  ["blue", "red", "blue", "red", "blue", "red", "blue", "red", "blue", "red"]
0, "one", "two"    -->  []

"""

def alternate(n, first_value, second_value):
    output = []
    for index, i in enumerate(range(0, n)):
        if index % 2 == 0:
            i = first_value
        elif index % 2 == 1:
            i = second_value
        output.append(i)
    return output




def alternate1(n, first_value, second_value):
    output = []
    for i in range(n):
        if i % 2 == 0:
            output.append(first_value)
        else:
            output.append(second_value)


def alternate2(n, first_value, second_value):
    return [first_value if i % 2 == 0 else second_value for i in range(n)]


alternate(5, True, False)