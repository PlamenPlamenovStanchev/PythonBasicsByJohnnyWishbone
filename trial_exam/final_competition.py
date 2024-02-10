dancers = int(input())
score = float(input())
season = input()
location = input()
winning_prize = dancers * score
money_after_expense = 0
money_for_charity = 0
if location == "Bulgaria":
    if season == "summer":
        money_after_expense = winning_prize * 0.95
    elif season == "winter":
        money_after_expense = winning_prize * 0.92
if location == "Abroad":
    if season == "summer":
        winning_prize *= 1.5
        money_after_expense = winning_prize * 0.9
    elif season == "winter":
        winning_prize *= 1.5
        money_after_expense = winning_prize * 0.85
money_for_charity = money_after_expense * 0.75
money_left = money_after_expense - money_for_charity
money_per_dancer = money_left / dancers
print(f"Charity - {money_for_charity:.2f}\n Money per dancer - {money_per_dancer:.2f}")
