import math

shape = input()

area = 0
if shape == 'square':
    side = float(input())
    area = side * side
elif shape == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    _area = side_a * side_b
elif shape == 'circle':
    circle_radious = float(input())
    area = math.pi * circle_radious ** 2
elif shape == 'triangle':
    side = float(input())
    height = float(input())
    area = side * height / 2
    print(f"{area :.3f}")
