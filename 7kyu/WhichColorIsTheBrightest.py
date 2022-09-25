from typing import List

"""
Given a list of hexidecimal colors,
return the brightest color
V = max(r,g,b)
"""
def brightest_commented(color):
	highest_value = ''
	highest_color = ''
	for i, c in enumerate(color): 
		r, g, b = c[1:3], c[3:5], c[5:7]
		color_value = max(r, g, b)
		if color_value > highest_value:
			highest_value = color_value
			highest_color = c
	print(highest_color)


	#print(highest_value)

	# print(f"{i}, {(c, color_value)}")

		
		#dict_c[c] = color_value # dictionary created in order list was given.
	
	
	#print(f"sorted dict: {sorted(dict_c)}")
	# for i in sorted(dict_c): # looping through sorted keys(hexcolors)
	# 	print((i, dict_c[i]), end=" ")
	# 	list_c.append(i) # keys in ascending order

	# highest_value = dict_c.get(list_c[-1])
	# print(f"highest_value: {highest_value}")
	# highest_color = []
	# for j in list_c:
	# 	if dict_c[j] == highest_value:
	# 		highest_color.append(j)

	# print(f"highest_color: {highest_color}")
	# for c in color:
	# 	if c in highest_color:
	# 		print(c)


color = ['#C09BF3', '#676314', '#8FFE5C', '#7673DC', '#AEA11D', '#67F132', '#2A7B07', '#20065A', '#91FDB1', '#AB4E02', '#5F7F94', '#55F8CF', '#8EB35F', '#02D880', '#993C12']

brightest_commented(color)







def brightest(color):
	dict_c = {} 
	list_c = []
	for c in color: 
		r, g, b = c[1:3], c[3:5], c[5:7]
		color_value = max(r, g, b)
		dict_c[c] = color_value 
	
	for i in sorted(dict_c): 
		list_c.append(i) 

	highest_value = dict_c.get(list_c[-1])

	highest_color = []
	for j in list_c:
		if dict_c[j] == highest_value:
			highest_color.append(j)

	for c in color:
		if c in highest_color:
			return c
