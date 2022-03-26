SAEarth = (5.1 * (10 ** 8))
moonRadius = 3475 / 2
SAEarth *= 0.29

from math import pi
from turtle import *

setup()

forward(40)

done()

moonSA = 4 * pi * (moonRadius ** 2)

moon = int(moonSA)
earth = int(SAEarth)

print("Moon dry surface Area: ", round(moon))
print("Earth dry surface Area: ", round(earth))
