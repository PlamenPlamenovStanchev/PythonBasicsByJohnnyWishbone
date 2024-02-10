price_per_page = float(input())
price_per_cover = float(input())
discount_percent_printing = int(input())
designing_cost = float(input())
self_funding_percent = int(input())
begining_printing_sum = (899 * price_per_page) + (2 * price_per_cover)
discount = begining_printing_sum * discount_percent_printing / 100
discounted_sum = begining_printing_sum - discount
sum_after_design = designing_cost + discounted_sum
prefinal_sum = sum_after_design * self_funding_percent / 100
final_sum = sum_after_design - prefinal_sum
print(f"Avtonom should pay {final_sum:.2f} BGN.")

