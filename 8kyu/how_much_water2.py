def how_much_water(water, load, clothes):

	if clothes > load * 2:
		return 'Too much clothes'
	
	if clothes < load:
		return 'Not enough clothes'

	else:
		return round(water * 1.1 **(clothes-load),2)

water=5
load = 10
clothes = 14

# desired outcome is:
#print(5 * 1.1 **(14-10))5 * 1.1 **(14-10))

print(how_much_water(water, load, clothes))