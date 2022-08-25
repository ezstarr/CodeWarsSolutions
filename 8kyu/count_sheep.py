def count_sheep(n):
	output = ""
	for i in range(1,n+1):
		output += f"{i} sheep..."
	return output


def count_sheep1(n):
	return ''.join([f"{i} sheep..." for i in range(1, n+1)])

num = 3

print(count_sheep1(num))