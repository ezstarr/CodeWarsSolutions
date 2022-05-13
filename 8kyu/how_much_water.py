def how_much_water(water, load, clothes):
    if clothes > (load *2):
        return "Too much clothes"
    if clothes < load:
        return "Not enough clothes"
    return round(water * 1.1 ** (clothes - load), 2)

load = 10
water = 10
clothes = 21

how_much_water(water, load, clothes)


#round(decimalNumber, significantDigits)