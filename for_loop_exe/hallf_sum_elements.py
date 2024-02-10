import sys

count_number = int(input())
max_number = -sys.maxsize
sum_numbers = 0
for _ in range(0, count_number):
    num = int(input())
    if num > max_number:
        max_number = num

    sum_numbers += num
rest_sum = sum_numbers - max_number
if max_number == rest_sum:
    print(f"Yes\n Sum = {max_number}")
else:
    diff = abs(max_number - rest_sum)
    print(f"No\n Diff ={diff}")

