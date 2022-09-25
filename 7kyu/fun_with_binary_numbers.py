"""
list all numbers --> (2^n)-1
	- must contain 1 at the same places/bits as the 
	binary representation of b. 
	- b will be 1, 2, 4, 8, etc. 

	example:
	soln(4,2) 
		[2, 3, 6, 7, 10, 11, 14, 15]

	1st: 16-1 --> 5
"""
from math import log2

# def solution(n, b):
# 	output = []
# 	if b == 0:
# 		return output
# 	for num in range(b,(2**n)): # starts at num where 1 is in the b's place value 		
# 		digit_offset = round(log2(b))+1 # logs can have rounding errors (lookup:truncate))
# 		binary_num = bin(num) #'0b1000'
# 		if binary_num[-digit_offset] == "1":
# 			output.append(num)
		
# 	return output 


# Codewars: Fun With Binary Numbers



print(solution(6,8))

def solution(n,b):
    pos = len(bin(b)[2:])
    result = []
    if b == 0:
        return result
    for i in range(0, 2**n):
        if ((i >> (pos - 1)) & 1):
            result.append(i)
    return result