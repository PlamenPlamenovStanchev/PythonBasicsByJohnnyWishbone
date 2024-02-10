count_of_numbers = int(input())
odd_sum = 0
even_sum = 0
for numbers in range(count_of_numbers):
    current_number = int(input())
    if numbers % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number
if odd_sum == even_sum:
    print(f"Yes \n Sum = {odd_sum}")
else:
    difference = abs(odd_sum - even_sum)
    print(f"No \n Diff = {difference}")