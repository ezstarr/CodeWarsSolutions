"""
Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]
"""
def reverse_seq(n):
    n_array = []
    rev_n_array =[]
    for i in range(1,(n+1)):
        n_array.append(i)
    n_array.reverse()
    print(n_array)

num = 5

reverse_seq(num)

# Learned that .reverse() just reverses an array, but can't be printed

"""
Alternative Solution:
def reverse_seq(n):
    ranges = reversed([*range(1, n + 1)])
    return [*ranges]

print(reverse_seq(5))
"""