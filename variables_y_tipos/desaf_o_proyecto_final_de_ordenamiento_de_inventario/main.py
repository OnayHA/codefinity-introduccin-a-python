# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"
#_______________________________________
palabras = items.split(", ") # donde "items" es la variable que define las palabras 
inicio = 0
for palabra in palabras:
    fin = inicio + len(palabra)
    print(f"SEGMANTACION DE ITEMS:'{palabra}' inicio: |{inicio}| fin |{fin}|")
    inicio = fin + 2 # contando la coma mas el espacio
#______________________________________
candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:27]
#___________________________________
# palabras = categories.split(", ")
# inicio = 0
# for palabra in palabras:
#     fin = inicio + len(palabra)
#     print(f" SEGMANTACION DE CATEGORIES: '{palabra}' inicio: |{inicio}| fin |{fin}|")
#     inicio = fin + 3
#__________________________________
category1 = categories[0:11]
category2 = categories[13:24]
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"
print(f"We have {candy1} for {bubblegum_price} in the {category1}")
print(f"We have {candy2} for {chocolate_price} in the {category1}")
print(f"We have {dry_goods} for {pasta_price} in the {category2}")