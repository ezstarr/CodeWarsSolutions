def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left >= distance_to_pump/mpg:
        return True
    if fuel_left <= distance_to_pump/mpg:
        return False

distance_to_pump = 50
mpg = 25
fuel_left = 2

zero_fuel(distance_to_pump, mpg, fuel_left)