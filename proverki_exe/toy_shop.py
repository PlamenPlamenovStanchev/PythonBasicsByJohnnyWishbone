vacation_cost = float(input())
puzzle_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
truck_count = int(input())
money_earned = puzzle_count * 2.60 \
               + talking_dolls_count * 3 \
               + teddy_bears_count * 4.10 \
               + minions_count * 8.20 \
               + truck_count * 2
total_count = puzzle_count + talking_dolls_count + teddy_bears_count + minions_count + truck_count
if total_count >= 50:
    money_earned = money_earned * (1-0.25)
money_earned = money_earned * (1-0.1)
if money_earned >= vacation_cost:
    print(f'Yes! {money_earned-vacation_cost :.2f} lv left.')
else:
    print(f"Not enough money! {vacation_cost-money_earned :.2f} lv needed.")
    

