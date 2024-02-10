day_training = int(input())
kilometers = float(input())
daily_raise = int(input())

current_kilometers = 0
total_kilometars = 0
for current_day in range(1, day_training+1):
    current_kilometers = kilometers

    total_kilometars += current_kilometers
if total_kilometars >= 1000:
    print(f"You've done a great job running {total_kilometars - 1000} more kilometers")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {1000 - total_kilometars} more kilometers")


