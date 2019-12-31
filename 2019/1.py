import os
import math

input = open(os.path.dirname(__file__) + "/1.txt", "r")
result = 0
for row in input.readlines():
    result += math.floor(int(row) / 3)  - 2

print(f'solution 1: {result}')


def extra_fuel(mass, fuel=0):
    fuel_needed = math.floor(mass / 3) - 2
    if fuel_needed <= 0:
        return fuel
    else:
        return extra_fuel(fuel_needed, fuel + fuel_needed)

# tests
print(extra_fuel(14))
print(extra_fuel(1969))
print(extra_fuel(100756))

input = open(os.path.dirname(__file__) + "/1.txt", "r")
result = 0
for row in input.readlines():
    result += extra_fuel(int(row))

print(f'solution 2: {result}')
