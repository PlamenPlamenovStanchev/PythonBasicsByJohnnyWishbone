fats_as_percent = int(input())
protein_as_percent = int(input())
carbs_as_percent = int(input())
total_calories = int(input())
water_percent = int(input())
total_grams_fats = ((fats_as_percent/100) * total_calories)/9
total_grams_protein = ((protein_as_percent/100) * total_calories)/4
total_grams_carbs = ((carbs_as_percent/100 * total_calories))/4
food_weight = total_grams_fats + total_grams_protein + total_grams_carbs
calories_per_gram_food = total_calories/food_weight
calories = ((100 - water_percent)/100) * calories_per_gram_food
print(f'{calories:.4f}')