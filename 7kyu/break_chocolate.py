# how many splits
# input always a positive integer

def break_chocolate(n, m):
	# if n<1 or m<1:
	# 	return 0
	# return (n*m)-1 /big-o 102ms

	# return n*m-1 if n>=1 or m>=1 else 0
	return max(n*m-1, 0)
break_chocolate(10000, 23432)