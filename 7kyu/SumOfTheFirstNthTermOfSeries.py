"""Your task is to write a function which returns the sum of following series upto nth term(parameter)."""

"""Rules:
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return 0.00

You will only be given Natural Numbers as arguments."""


def series_sum(n):
    sum = 0
    for i in range(0,n):
        # first loop add 1 to sum.
        # second loop adds 1/4 to 1, which equals 1.25.
        sum += 1/(1+3 * i)
        # each additional loop adds an updated fraction to previous sum.
    print("%.2f" % sum)






series_sum(6)