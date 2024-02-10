film_budget = float(input())
extras_count = float(input())
clothing_for_one = float(input())

decor = film_budget * 0.10
if extras_count>150:
    clothing_for_one = clothing_for_one * 0.90

money_needed = decor + extras_count * clothing_for_one

if money_needed > film_budget:
    print (f"Not enough money!")
    print(f"Wingard need {money_needed - film_budget :.2f} leva more")
else:
    print('Action!')
    print(f'Wingard starts filming with {film_budget - money_needed :.2f} leva left.')