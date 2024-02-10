current_hour = int(input())
current_minute = int(input())

current_minute_plus_15 = current_minute + 15
if current_minute_plus_15 >= 60:
    current_minute_plus_15 -= 60
    current_hour += 1
if current_hour == 24:
    current_hour = 0
print(f"{current_hour}:{current_minute_plus_15:02d}")
