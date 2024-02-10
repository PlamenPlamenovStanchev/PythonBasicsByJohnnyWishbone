budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())
gpu_sum = 250 * gpu_count
cpu_cost = 0.35 * gpu_sum
cpu_sum = cpu_cost * cpu_count
ram_cost = 0.1 * gpu_sum
ram_sum = ram_cost * ram_count
sum_needed = gpu_sum + cpu_sum + ram_sum
discount = 0
if gpu_count > cpu_count:
    discount = sum_needed * 0.15
end_sum = sum_needed - discount
if budget >= end_sum:
    budget_left = budget - end_sum
    print(f"You have {budget_left :.2f} leva left!")
else:
    money_needed = end_sum - budget
    print(f"Not enough money! You need {money_needed :.2f} leva more!")
