t_shirt_price = float(input())
needed_sum = float(input())
shorts_price = t_shirt_price * 0.75
sox_price = shorts_price * 0.2
cleats_price = (t_shirt_price + shorts_price) * 2
footbal_kit_price = t_shirt_price + shorts_price + sox_price + cleats_price
total_price = footbal_kit_price * 0.85
difference = abs(total_price - needed_sum)
if total_price >= needed_sum:
    print(f"Yes, he will earn the world-cup replica ball!\n His sum is {total_price:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.\n He needs {difference:.2f} lv. more.")