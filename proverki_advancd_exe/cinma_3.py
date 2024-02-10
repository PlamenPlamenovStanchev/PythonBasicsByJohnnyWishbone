prices = {
    "Premiere": 12.00,
    "Normal": 7.50,
    "Discount": 5.00,
}

screening_type = input()
rows = int(input())
cols = int(input())

screening_capacity = rows * cols
price = prices[screening_type]

total_income = screening_capacity * price
print(f"{total_income :.2f} leva")