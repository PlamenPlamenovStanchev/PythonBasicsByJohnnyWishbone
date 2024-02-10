deposited_amount = float(input())
deposit_months = int(input())
annual_intrest_rate = float(input())/100
final_amount = deposited_amount+deposit_months*((deposited_amount*annual_intrest_rate)/12)
print(final_amount)