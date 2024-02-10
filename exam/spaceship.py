import math
spaceship_width = float(input())
spaceship_lenght = float(input())
spaceship_height = float(input())
average_height_of_austronauts = float(input())
spaceship_volume = spaceship_height * spaceship_lenght * spaceship_width
spaceship_room_volume = (average_height_of_austronauts + 0.40) * 2 * 2
astronauts = spaceship_volume / spaceship_room_volume
if astronauts < 3:
    print(f'The spacecraft is too small.')
elif 3 <= astronauts <= 10:
    rounded_astronauts = math.floor(astronauts)
    print(f'The spacecraft holds {rounded_astronauts} astronauts.')
else:
    print(f'The spacecraft is too big.')
