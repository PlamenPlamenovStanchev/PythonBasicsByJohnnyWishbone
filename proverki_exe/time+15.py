current_hour = int(input())
current_minute = int(input())

current_time_in_minutes = current_hour * 60 + current_minute + 15
current_time_as_hour = current_time_in_minutes // 60
if current_time_as_hour == 24:
    current_hour_as_hour = 0
current_time_as_minutes = current_time_in_minutes % 60
print(f'{current_time_as_hour}:{current_time_as_minutes:02d}')

