"""Your task is to make a function that can take any non-negative
integer as an argument and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321"""

# Three versions:


def descending_order(num):
    str_num = str(num)             # 42145
    sorted_num = sorted(str_num)   # ['1', '2', '4', '4', '5']
    str_num = ''.join(sorted_num)  # 12445
    rev = int(str_num[::-1])       # 54421
    return rev


def descending_order1(num):
    return int("".join(sorted(str(num), reverse=True)))


def descending_order2(num):
    s = str(num)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    print(int(s))


descending_order2(42145)