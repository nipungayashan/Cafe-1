print("----------Welcome to Central Perk Cafe----------")
#displaying all options available for the user to choose from
print("1. View Menu (Alphabetical Order)")          #view order menu  in alphabetical order
print("2. View Menu (Price: low to high)")          #view menu price from low to high
print("3. Search an item")                          #item search
print("4. Place an order")                          #order placement
print("5. Exit")

Choice = int(input("Select Option (1-5): "))        #taking input from user to choose an option

menu = {
    "Americano       "    :550,
    "Latte           "    :500,
    "Cappuccino      "    :450,
    "Mocha           "    :600,
    "Hot Chocolate   "    :700,
    "Espresso        "    :300,
    "Croissant       "    :370,
    "Chicken Sandwich"    :300,
    "Cheese Sandwich "    :250,
    "Blueberry Muffin"    :450,
    "Fish Pastry     "    :250,

}

#---------Match Case implemented for users selection----------
match Choice:
    #
    case 1:
        print("\n---------Cafe Menu---------")
        for item in sorted(menu):
            print(item, " - LKR", menu[item])

    case 2:
        print("\n---------Cafe Menu---------")
        def get_price(item):
            return item[1]

        sorted_menu = sorted(menu.items(), key=get_price)

        for item, price in sorted_menu:
            print(item, "-LKR", price)



