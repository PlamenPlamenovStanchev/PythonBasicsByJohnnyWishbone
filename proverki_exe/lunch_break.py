import math

show_name = input()
episode_lenght = int(input())
break_lenght =int(input())

lunch_lenght = break_lenght / 8
rest_lenght = break_lenght / 4

time_needed = lunch_lenght + rest_lenght + episode_lenght
if time_needed <= break_lenght:
    time_left = math.ceil(break_lenght - time_needed)
    print(f'You have enough time to watch {show_name} and left with {time_left} minutes free time.')
else:
    time_not_enough = math.ceil(time_needed - break_lenght)
    print(f"You don't have enough time to watch {show_name}, you need {time_not_enough} more minutes.")
