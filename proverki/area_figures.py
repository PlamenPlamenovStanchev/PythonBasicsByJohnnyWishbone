import math

shape = input()
if shape == "square":
    side = float(input())
    area_for_square = side ** 2
    print(f"{area_for_square:.3f}")
elif shape == "circle":
    radious = float(input())
    area_for_circle = math.pi * radious ** 2
    print(f"{area_for_circle:.3f}")
elif shape == "rectangle":
    sidea = float(input())
    sideb = float(input())
    area_for_rectangle = sidea * sideb
    print(f"{area_for_rectangle:.3f}")
elif shape == "triangle":
    side = float(input())
    height = float(input())
    area_for_triangle = side * height / 2
    print(f"{area_for_triangle:.3f}")
