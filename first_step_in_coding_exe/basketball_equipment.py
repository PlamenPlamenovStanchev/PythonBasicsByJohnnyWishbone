annual_fee = int(input())
basket_shoes = annual_fee*(1-0.40)
basket_uniform = basket_shoes*(1-0.2)
basket_ball = basket_uniform*1/4
basket_accessories=basket_ball*1/5
total_cost = annual_fee+basket_shoes+basket_uniform+basket_ball+basket_accessories
print(total_cost)