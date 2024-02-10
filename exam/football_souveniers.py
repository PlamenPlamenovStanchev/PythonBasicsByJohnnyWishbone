team = input()
souvenier = input()
souveniers_bought = int(input())
price = 0
sum = 0
if team == "Argentina":
    if souvenier == "flags":
        price = 3.25
    elif souvenier == "caps":
        price = 7.20
    elif souvenier == "posters":
        price = 5.10
    elif souvenier == "stickers":
        price = 1.25
elif team == "Brazil":
    if souvenier == "flags":
        price = 4.20
    elif souvenier == "caps":
        price = 8.50
    elif souvenier == "posters":
        price = 5.35
    elif souvenier == "stickers":
        price = 1.20
elif team == "Croatia":
    if souvenier == "flags":
        price = 2.75
    elif souvenier == "caps":
        price = 6.90
    elif souvenier == "posters":
        price = 4.95
    elif souvenier == "stickers":
        price = 1.10
elif team == "Denmark":
    if souvenier == "flags":
        price = 3.10
    elif souvenier == "caps":
        price = 6.50
    elif souvenier == "posters":
        price = 4.80
    elif souvenier == "stickers":
        price = 0.90
sum = souveniers_bought * price
if team == "Argentina" or team == "Brazil" or team == "Croatia" or team == "Denmark":
    print(f"Pepi bought {souveniers_bought} {souvenier} of {team} for {sum:.2f} lv. ")
if team != "Argentina" or team != "Brazil" or team != "Croatia" or team != "Denmark":
    print(f"Invalid country!")
if souvenier != "flags" or souvenier != "caps" or souvenier != "posters" or souvenier != "stickers":
    print(f"Invalid stock!")








