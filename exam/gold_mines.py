locations = int(input())

for _ in range(locations):
    average_yield_per_day_expected = float(input())
    days_digging_on_location = int(input())
    for _ in range(days_digging_on_location):
        gold_yield_per_day = float(input())
        average_yield = gold_yield_per_day / days_digging_on_location
        if average_yield >= average_yield_per_day_expected:
            print(f"Good job! Average gold per day{average_yield:.2f}.")
        else:
            needed_gold = average_yield_per_day_expected - average_yield
            print(f'You need {needed_gold:.2f}.')
