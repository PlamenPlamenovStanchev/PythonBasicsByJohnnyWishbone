food_bought = int(input())
command = input()
total_food_eaten_by_dog =0
while command != "Adopted":
    food_to_grams = food_bought * 1000
    current_food_eaten_by_dog = int(input())
    current_food_eaten_by_dog = total_food_eaten_by_dog
    total_food_eaten_by_dog += current_food_eaten_by_dog
    command = input()
if total_food_eaten_by_dog > food_to_grams:
    leftovers = food_to_grams - total_food_eaten_by_dog
    print(f"Food i enough! Leftovers:{leftovers} grams.")
else:
    needed_food = total_food_eaten_by_dog - food_to_grams
    print(f"Food is not enough.You need {needed_food} grams more.")
