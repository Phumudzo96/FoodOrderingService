# creating lists to store the orders and their prices
food = []
price = []

# ask the user for thier name so you can elcome them to the program
username = input("Enter your name:  ")
print(
    "Hi there👋 "
    + username
    + "... and welcome to our food ordering services. Kindly select from the following so we can asisst you:"
)

# the pragram will always return to the main menu since its always true
while True:
    user = input("Main menu: \n 1) Order food \n 2) List of our outlets \n 3) Order checkout \n 4) Exit \n : " ) # The Main Menu

    #if the user selects 1 the following needs to happen
    if user == "1":
        food_order = input(
            "select a number for the following \n"
            " 1) Special🍽️ \n 2) Combo🍔🍟 \n 3) Wings🍗 \n 4) Burgers🍔  \n 5) Drinks🍦 \n 6) Sides🌭 \n 0) Back to menu🔙 \n : " ) # The Food Menu
        
        # When the special option is selected
        if food_order == "1":
            special_food = input(
                "Menu: \n 1) Breakefast special = American breakefest(waffles + wings(4) + coffee) \n 2) Midday special(Large burger + wings(6) + Miranda cold drink) \n 0) Back to menu \n : "
            ) # The sepcial menu 
            if special_food == "1":
                food_size = input(
                    "Coffee size: \n 1) Small = R35.00(Meal) \n 2) Medium = R45.00(Meal) \n 3) Large = R50.00(Meal) \n 0) Back to Main Menu \n : "
                ) # Selecting the size and price of your coffee
                if food_size == "1":
                    how_many = int(
                        input("how many Small Breakfast special meals would you like? ")
                    ) # asking user the how many specials would you like to order
                    final_price = float(35.00) * how_many  #calculating how much your order is going to be
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    ) # Showing the user how much their order is going to be
                    food.append("Small Breakfast special X{}".format(how_many)) #Add your order to the food list
                    price.append(final_price) # Add the price of the order to the price list
                elif food_size == "2":
                    how_many = int(
                        input(
                            "how many Medium Breakfast special meals would you like? "
                        )
                    )
                    final_price = float(45.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Medium Breakfast special X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "3":
                    how_many = int(
                        input("how many Large Breakfast special meals would you like? ")
                    )
                    final_price = float(50.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Large Breakfast special X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "0":
                    print("Back to the main menu")
                else:
                    print("Wrong selection has been made... Back to the main menu")
            elif special_food == "2":
                food_size = input(
                    "Drink size: \n 1) Small = R40.00(Meal) \n 2) Medium = R45.00(Meal) \n 3) Large = R55.00(Meal) \n 0) Back to Main Menu \n : "
                ) #the size of the drink plus the price of the meals being ordered 
                if food_size == "1":
                    how_many = int(
                        input("how many Small Midday special meals would you like? ")
                    )
                    final_price = float(40.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Small Midday special X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "2":
                    how_many = int(
                        input("how many Medium Midday special meals would you like? ")
                    )
                    final_price = float(45.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Medium Midday special X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "3":
                    how_many = int(
                        input("how many Large Midday special meals would you like? ")
                    )
                    final_price = float(55.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Large Midday special X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "0":
                    print("Back to the main menu")
                else:
                    print("Wrong selection has been made... Back to Menu")
            elif special_food == "0":
                print("Let's go back to the main menu")
            else:
                print("Wrong selection has been made. Back to the main menu")

        elif food_order == "2": # When the combo option is selected
            combo = input(
                "Menu: \n 1) Burger + chips \n 2) Burger + wings \n"
                " 3) wings + cold drink \n 4) wings + chips \n 0) Back to Menu \n : "
            ) # The combo menu

            if combo == "1":
                food_size = input(
                    "Meals size: \n 1) Small = R30.00 \n 2) Medium = R40.00 \n 3) Large = R50.00 \n 0) Back to Main Menu \n : "
                ) #the size and price of the meals being ordered 
                if food_size == "1":
                    how_many = int(
                        input("how many Small Burger + chips meals would you like? ")
                    )
                    final_price = float(30.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Small Burger + chips X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "2":
                    how_many = int(
                        input("how many Medium Burger + chips meals would you like? ")
                    )
                    final_price = float(40.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Medium Burger + chips X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "3":
                    how_many = int(
                        input("how many Large Burger + chips meals would you like? ")
                    )
                    final_price = float(50.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Large Burger + chips X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "0":
                    print("Back to the main menu")

            elif combo == "2":
                food_size = input(
                    "Meals size: \n 1) Small = R35.00 \n 2) Medium = R45.00 \n 3) Large = R55.00 \n 0) Back to Main Menu \n : "
                ) #the size and price of the meals being ordered 
                if food_size == "1":
                    how_many = int(
                        input("how many Small Burger + wings(6) meals would you like? ")
                    )
                    final_price = float(35.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Small Burger + wings(6) X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "2":
                    how_many = int(
                        input(
                            "how many Medium Burger + wings(6) meals would you like? "
                        )
                    )
                    final_price = float(45.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Medium Burger + wings(6) X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "3":
                    how_many = int(
                        input("how many Large Burger + wings meals would you like? ")
                    )
                    final_price = float(55.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Large Burger + wings X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "0":
                    print("Back to the main menu")
            elif combo == "3":
                food_size = input(
                    "Wings size: \n 1) Wings(4) = R30.00 \n 2) Wing(6) = R40.00 \n 3) Wings(10) = R50.00 \n 0) Back to Main Menu \n : "
                ) # the size and the price of the wings
                if food_size == "1":
                    how_many = int(
                        input("how many Wings(4) + cold drink meals would you like? ")
                    )
                    final_price = float(30.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Wings(4) + cold drink X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "2":
                    how_many = int(
                        input("how many Wings(6) + cold drink meals would you like? ")
                    )
                    final_price = float(40.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Wings(6) + cold drink X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "3":
                    how_many = int(
                        input("how many Wings(10) + cold drink meals would you like? ")
                    )
                    final_price = float(50.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Wings(10) + cold drink X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "0":
                    print("Back to the main menu")
            elif combo == "4":
                food_size = input(
                    "Wings size: \n 1) Wings(4) = R35.00 \n 2) Wing(6) = R45.00 \n 3) Wings(10) = R55.00 \n 0) Back to Main Menu \n : "
                )
                if food_size == "1":
                    how_many = int(
                        input("how many Wings(4) + chips meals would you like? ")
                    )
                    final_price = float(35.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Wings(4) + chips X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "2":
                    how_many = int(
                        input("how many Wings(6) + chips meals would you like? ")
                    )
                    final_price = float(45.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Wings(6) + chips X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "3":
                    how_many = int(
                        input("how many Wings(10) + chips meals would you like? ")
                    )
                    final_price = float(55.00) * how_many
                    print(
                        "The price for what you've ordered is : R{}".format(final_price)
                    )
                    food.append("Wings(10) + chips X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "0":
                    print("Back to the main menu")
            elif combo == "0":
                print("Let's go back")
            else:
                print("Wrong selection has been entered") #When an invaild number has been entered this message with displayed

        elif food_order == "3":  # When the wings option is selected
            wings = input("Menu: \n 1) BBQ wings \n 2) Sweet & sour wings \n 3) Chilli wings \n "
                "4) Mixed wings \n 0) Back to menu \n : ")

            if wings == "1":
                food_size = input("Wings size: \n 1) Wings(4) = R35.00 \n 2) Wing(6) = R45.00 \n 3) Wings(10) = R55.00 \n 0) Back to Main Menu \n : ")
                if food_size == "1":
                    how_many = int(input("how many BBQ Wings(4) would you like? "))
                    final_price = float(30.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("BBQ Wings(4) X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "2":
                    how_many = int(input("how many BBQ Wings(6) would you like? "))
                    final_price = float(45.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("BBQ Wings(6) X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "3":
                    how_many = int(input("how many BBQ Wings(10) would you like? "))
                    final_price = float(55.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("BBQ Wings(10) X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "0":
                    print("Back to the main menu")
            elif wings == "2":
                food_size = input("Wings size: \n 1) Wings(4) = R35.00 \n 2) Wing(6) = R45.00 \n 3) Wings(10) = R55.00 \n 0) Back to Main Menu \n : ")
                if food_size == "1":
                    how_many = int(input("how many Sweet & sour Wings(4) would you like? "))
                    final_price = float(35.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Sweet & sour Wings(4) X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "2":
                    how_many = int(input("how many Sweet & sour Wings(6) would you like? "))
                    final_price = float(45.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Sweet & sour Wings(6) X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "3":
                    how_many = int(input("how many Sweet & sour Wings(10) would you like? "))
                    final_price = float(55.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Sweet & sour Wings(10) X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "0":
                    print("Back to the main menu")
            elif wings == "3":
                food_size = input("Wings size: \n 1) Wings(4) = R35.00 \n 2) Wing(6) = R45.00 \n 3) Wings(10) = R55.00 \n 0) Back to Main Menu \n : ")
                if food_size == "1":
                    how_many = int(input("how many Chilli Wings(4) would you like? "))
                    final_price = float(35.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Chilli Wings(4) X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "2":
                    how_many = int(input("how many Chilli Wings(6) would you like? "))
                    final_price = float(45.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Chilli Wings(6) X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "3":
                    how_many = int(input("how many Chilli Wings(10) would you like? "))
                    final_price = float(55.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Chilli Wings(10) X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "0":
                    print("Back to the main menu")
            elif wings == "4":
                food_size = input("Wings size: \n 1) Wings(4) = R35.00 \n 2) Wing(6) = R45.00 \n 3) Wings(10) = R55.00 \n 0) Back to Main Menu \n : ")
                if food_size == "1":
                    how_many = int(input("how many Mixed Wings(4) would you like? "))
                    final_price = float(35.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Mixed Wings(4) X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "2":
                    how_many = int(input("how many Mixed Wings(6) would you like? "))
                    final_price = float(45.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Mixed Wings(6) X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "3":
                    how_many = int(input("how many Mixed Wings(10) would you like? "))
                    final_price = float(55.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Mixed Wings(10) X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "0":
                    print("Back to the main menu")
                elif wings == "0":
                    print("Let's go back")
                else:
                    print("Wrong selection has been entered")

        elif food_order == "4": # When a burger option is selected
            burgers = input(
                "Menu: \n 1) Turkey burger \n 2) Beef burger \n 3) Chicken burger \n "
                "4) Cheeseburger \n 0) Back to menu \n : "
            )

            if burgers == "1":
                food_size = input("Burger size: \n 1) Small = R30.00 \n 2) Medium = R40.00 \n 3) Large = R50.00 \n 0) Back to Main Menu \n : ")
                if food_size == "1":
                    how_many = int(input("how many Small Turkey Burgers would you like? "))
                    final_price = float(30.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Small Turkey Burger X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "2":
                    how_many = int(input("how many Medium Turkey Burgers would you like? "))
                    final_price = float(40.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Medium Turkey Burger X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "3":
                    how_many = int(input("how many Large Turkey Burgers would you like? "))
                    final_price = float(50.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Large Turkey Burger X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "0":
                    print("Back to the main menu")
            elif burgers == "2":
                food_size = input("Burger size: \n 1) Small = R30.00 \n 2) Medium = R40.00 \n 3) Large = R50.00 \n 0) Back to Main Menu \n : ")
                if food_size == "1":
                    how_many = int(input("how many Small Beef Burgers would you like? "))
                    final_price = float(30.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Small Beef Burger X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "2":
                    how_many = int(input("how many Medium Beef Burgers would you like? "))
                    final_price = float(40.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Medium Beef Burger X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "3":
                    how_many = int(input("how many Large Beef Burgers would you like? "))
                    final_price = float(50.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Large Beef Burger X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "0":
                    print("Back to the main menu")
            elif burgers == "3":
                food_size = input("Burger size: \n 1) Small = R30.00 \n 2) Medium = R40.00 \n 3) Large = R50.00 \n 0) Back to Main Menu \n : ")
                if food_size == "1":
                    how_many = int(input("how many Small Chicken Burgers would you like? "))
                    final_price = float(30.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Small Chicken Burger X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "2":
                    how_many = int(input("how many Medium Chicken Burgers would you like? "))
                    final_price = float(40.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Medium Chicken Burger X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "3":
                    how_many = int(input("how many Large Chicken Burgers would you like? "))
                    final_price = float(50.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Large Chicken Burger X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "0":
                    print("Back to the main menu")
            elif burgers == "4":
                food_size = input("Buurger size: \n 1) Small = R30.00 \n 2) Medium = R40.00 \n 3) Large = R50.00 \n 0) Back to Main Menu \n : ")
                if food_size == "1":
                    how_many = int(input("how many Small Cheeseburgers would you like? "))
                    final_price = float(30.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Small Cheeseburger X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "2":
                    how_many = int(input("how many Medium Cheeseburgers would you like? "))
                    final_price = float(40.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Medium Cheeseburger X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "3":
                    how_many = int(input("how many Large Cheeseburgers would you like? "))
                    final_price = float(50.00) * how_many
                    print("The price for what you've ordered is : R{}".format(final_price))
                    food.append("Large Cheeseburger X{}".format(how_many))
                    price.append(final_price)
                elif food_size == "0":
                    print("Back to the main menu")
            elif burgers == "0":
                print("Let's go back")
            else:
                print("Wrong selection has been entered")

        elif food_order == "5":  #We the drinks option is selected
            extras = input(
                "Menu: \n 1) Water \n 2) Milkshake \n 3) Juice \n "
                "4) Colddrink \n 5) Ice-cream  \n 0) Back to menu \n : "
            )

            if extras == "1":
                food_size = input("Water size: \n 1) Small = R15.00 \n 2) Medium = R25.00 \n 3) Large = R30.00 \n 0) Back to Main Menu \n : ")
                ice = input("Ice: \n 1) Add ice \n 2) No ice \n : ")
                if food_size == "1":
                    if ice == "1":
                        how_many = int(input("how many Small Water would you like? "))
                        final_price = float(15.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Small Water(with ice) X{}".format(how_many))
                        price.append(final_price)
                    elif ice == "2":
                        how_many = int(input("how many Small Water would you like? "))
                        final_price = float(15.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Small Water(no ice) X{}".format(how_many))
                        price.append(final_price)
                    else:
                        print("Wrong selection has been entered")
                elif food_size == "2":
                    if ice == "1":
                        how_many = int(input("how many Medium Water would you like? "))
                        final_price = float(25.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Medium Water(with ice) X{}".format(how_many))
                        price.append(final_price)
                    elif ice == "2":
                        how_many = int(input("how many Medium Water would you like? "))
                        final_price = float(30.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Medium Water(no ice) X{}".format(how_many))
                        price.append(final_price)
                    else:
                        print("Wrong selection has been entered")
                elif food_size == "3":
                    if ice == "1":
                        how_many = int(input("how many Large Water would you like? "))
                        final_price = float(15.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Large Water(with ice) X{}".format(how_many))
                        price.append(final_price)
                    elif ice == "2":
                        how_many = int(input("how many Large Water would you like? "))
                        final_price = float(15.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Large Water(no ice) X{}".format(how_many))
                        price.append(final_price)
                    else:
                        print("Wrong selection has been entered")
                elif food_size == "0":
                    print("Back to the main menu")
            elif extras == "2":
                food_size = input("Milkshakes size: \n 1) Small = R20.00 \n 2) Medium = R25.00 \n 3) Large = R30.00 \n 0) Back to Main Menu \n : ")
                flavour = input("Milkshakes flavour: \n 1) Strawberry \n 2) Chocolate \n 3) Bubblegum \n : ") 
                if food_size == "1":
                    if flavour == "1":
                        how_many = int(input("how many Small Strawberry milkshakes would you like? "))
                        final_price = float(20.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Small Strawberry milkshakes X{}".format(how_many))
                        price.append(final_price)
                    elif flavour == "2":
                        how_many = int(input("how many Small Chocolate milkshakes would you like? "))
                        final_price = float(20.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Small Chocolate milkshakes X{}".format(how_many))
                        price.append(final_price)
                    elif flavour == "3":
                        how_many = int(input("how many Small Bubblegaum milkshakes would you like? "))
                        final_price = float(20.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Small Bubblegum milkshakes X{}".format(how_many))
                        price.append(final_price)
                    else: 
                        print("Wrong selection has been entered... back to menu")
                elif food_size == "2":
                    if flavour == "1":
                        how_many = int(input("how many Medium Strawberry milkshakes would you like? "))
                        final_price = float(25.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Medium Strawberry milkshakes X{}".format(how_many))
                        price.append(final_price)
                    elif flavour == "2":
                        how_many = int(input("how many Small Chocolate milkshakes would you like? "))
                        final_price = float(25.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Medium Chocolate milkshakes X{}".format(how_many))
                        price.append(final_price)
                    elif flavour == "3":
                        how_many = int(input("how many Small Bubblegaum milkshakes would you like? "))
                        final_price = float(25.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Medium Bubblegum milkshakes X{}".format(how_many))
                        price.append(final_price)
                    else: 
                        print("Wrong selection has been entered... back to menu")
                elif food_size == "3":
                    if flavour == "1":
                        how_many = int(input("how many Large Strawberry milkshakes would you like? "))
                        final_price = float(30.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Large Strawberry milkshakes X{}".format(how_many))
                        price.append(final_price)
                    elif flavour == "2":
                        how_many = int(input("how many Large Chocolate milkshakes would you like? "))
                        final_price = float(30.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Large Chocolate milkshakes X{}".format(how_many))
                        price.append(final_price)
                    elif flavour == "3":
                        how_many = int(input("how many Large Bubblegaum milkshakes would you like? "))
                        final_price = float(30.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Large Bubblegum milkshakes X{}".format(how_many))
                        price.append(final_price)
                    else: 
                        print("Wrong selection has been entered... back to menu")
                elif food_size == "0":
                    print("Back to the main menu")
            elif extras == "3":
                food_size = input("Juice size: \n 1) Small = R20.00 \n 2) Medium = R25.00 \n 3) Large = R30.00 \n 0) Back to Main Menu \n : ")
                flavour = input("Juice flavour: \n 1) Apple \n 2) Orange \n 3) Grape \n : ") 
                ice = input("Ice: \n 1) Add ice \n 2) No ice \n : ")
                if food_size == "1":
                    if flavour == "1":
                        if ice == "1":
                            how_many = int(input("how many Small Apple juice(with ice) would you like? "))
                            final_price = float(20.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Small Apple juice(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Small Apple juice would you like? "))
                            final_price = float(20.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Small Apple juice(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    elif flavour == "2":
                        if ice == "1":
                            how_many = int(input("how many Small Orange juice(with ice) would you like? "))
                            final_price = float(20.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Small Apple juice(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Small Orange juice would you like? "))
                            final_price = float(20.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Small Orange juice(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    elif flavour == "3":
                        if ice == "1":
                            how_many = int(input("how many Small Grape juice(with ice) would you like? "))
                            final_price = float(20.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Small Grape juice(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Small Grape juice would you like? "))
                            final_price = float(20.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Small Grape juice(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    else: 
                        print("Wrong selection has been entered... back to menu")
                elif food_size == "2":
                    if flavour == "1":
                        if ice == "1":
                            how_many = int(input("how many Medium Apple juice(with ice) would you like? "))
                            final_price = float(25.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Medium Apple juice(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Medium Apple juice would you like? "))
                            final_price = float(25.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Medium Apple juice(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    elif flavour == "2":
                        if ice == "1":
                            how_many = int(input("how many Medium Orange juice(with ice) would you like? "))
                            final_price = float(25.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Medium Orange juice(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Medium Orange juice would you like? "))
                            final_price = float(25.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Medium Orange juice(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    elif flavour == "3":
                        if ice == "1":
                            how_many = int(input("how many Medium Grape juice(with ice) would you like? "))
                            final_price = float(25.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Medium Grape juice(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Medium Grape juice would you like? "))
                            final_price = float(25.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Medium Grape juice(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    else: 
                        print("Wrong selection has been entered... back to menu")
                elif food_size == "3":
                    if flavour == "1":
                        if ice == "1":
                            how_many = int(input("how many Large Apple juice(with ice) would you like? "))
                            final_price = float(30.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Large Apple juice(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Large Apple juice would you like? "))
                            final_price = float(30.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Large Apple juice(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    elif flavour == "2":
                        if ice == "1":
                            how_many = int(input("how many Large Orange juice(with ice) would you like? "))
                            final_price = float(30.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Large Orange juice(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Large Orange juice would you like? "))
                            final_price = float(30.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Large Orange juice(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    elif flavour == "3":
                        if ice == "1":
                            how_many = int(input("how many Large Grape juice(with ice) would you like? "))
                            final_price = float(30.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Large Grape juice(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Large Grape juice would you like? "))
                            final_price = float(30.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Large Grape juice(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    else: 
                        print("Wrong selection has been entered... back to menu")
                elif food_size == "0":
                    print("Back to the main menu")
            elif extras == "4":
                food_size = input("Cold drink size: \n 1) Small = R20.00 \n 2) Medium = R25.00 \n 3) Large = R30.00 \n 0) Back to Main Menu \n : ")
                flavour = input("Cold drink flavour: \n 1) Miranda \n 2) Iron brew \n 3) Coke \n : ") 
                ice = input("Ice: \n 1) Add ice \n 2) No ice \n : ")
                if food_size == "1":
                    if flavour == "1":
                        if ice == "1":
                            how_many = int(input("how many Small Miranda cold drink(with ice) would you like? "))
                            final_price = float(20.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Small Miranda cold drink(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Small Miranda cold drink(no ice) would you like? "))
                            final_price = float(20.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Small Miranda cold drink(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    elif flavour == "2":
                        if ice == "1":
                            how_many = int(input("how many Small Iron brew cold drink(with ice) would you like? "))
                            final_price = float(20.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Small Iron brew cold drink(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Small Iron brew cold drink(no ice) would you like? "))
                            final_price = float(20.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Small Iron brew cold drink(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    elif flavour == "3":
                        if ice == "1":
                            how_many = int(input("how many Small Coke cold drink(with ice) would you like? "))
                            final_price = float(20.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Small Coke cold drink(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Small Coke cold drink(no ice) would you like? "))
                            final_price = float(20.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Small Coke cold drink(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    else: 
                        print("Wrong selection has been entered... back to menu")
                elif food_size == "2":
                    if flavour == "1":
                        if ice == "1":
                            how_many = int(input("how many Medium Miranda cold drink(with ice) would you like? "))
                            final_price = float(25.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Medium Miranda cold drink(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Medium Miranda cold drink(no ice) would you like? "))
                            final_price = float(25.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Medium Miranda cold drink(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    elif flavour == "2":
                        if ice == "1":
                            how_many = int(input("how many Medium Iron brew cold drink(with ice) would you like? "))
                            final_price = float(25.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Medium Iron brew cold drink(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Medium Iron brew cold drink(no ice) would you like? "))
                            final_price = float(25.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Medium Iron brew cold drink(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    elif flavour == "3":
                        if ice == "1":
                            how_many = int(input("how many Medium Coke cold drink(with ice) would you like? "))
                            final_price = float(25.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Medium Coke cold drink(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Medium Coke cold drink(no ice) would you like? "))
                            final_price = float(25.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Medium Coke cold drink(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    else: 
                        print("Wrong selection has been entered... back to menu")
                elif food_size == "3":
                    if flavour == "1":
                        if ice == "1":
                            how_many = int(input("how many Large Miranda cold drink(with ice) would you like? "))
                            final_price = float(30.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Large Miranda cold drink(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Large Miranda cold drink(no ice) would you like? "))
                            final_price = float(30.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Large Miranda cold drink(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    elif flavour == "2":
                        if ice == "1":
                            how_many = int(input("how many Large Iron brew cold drink(with ice) would you like? "))
                            final_price = float(30.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Large Iron brew cold drink(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Large Iron brew cold drink(no ice) would you like? "))
                            final_price = float(30.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Large Iron brew cold drink(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    elif flavour == "3":
                        if ice == "1":
                            how_many = int(input("how many Large Coke cold drink(with ice) would you like? "))
                            final_price = float(30.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Large Coke cold drink(with ice) X{}".format(how_many))
                            price.append(final_price)
                        elif ice == "2":
                            how_many = int(input("how many Large Coke cold drink(no ice) would you like? "))
                            final_price = float(30.00) * how_many
                            print("The price for what you've ordered is : R{}".format(final_price))
                            food.append("Large Coke cold drink(no ice) X{}".format(how_many))
                            price.append(final_price)
                        else:
                            print("Wrong selection has been entered")
                    else: 
                        print("Wrong selection has been entered... back to menu")
                elif food_size == "0":
                    print("Back to the main menu")
            elif extras == "5":
                food_size = input("Ice - cream size: \n 1) Small = R5.00 \n 2) Medium = R10.00 \n 3) Large = R15.00 \n 0) Back to Main Menu \n : ")
                flavour = input("Ice - cream flavour: \n 1) Vanilla \n 2) Chocolate \n 3) Mixed \n : ") 
                if food_size == "1":
                    if flavour == "1":
                        how_many = int(input("how many Small Vanilla Icecream would you like? "))
                        final_price = float(5.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Small Vanilla Icecream X{}".format(how_many))
                        price.append(final_price)
                    elif flavour == "2":
                        how_many = int(input("how many Small Chocolate Icecream would you like? "))
                        final_price = float(5.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Small Chocholate Icecream X{}".format(how_many))
                        price.append(final_price)
                    elif flavour == "3":
                        how_many = int(input("how many Small Mixed Icecream would you like? "))
                        final_price = float(5.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Small Mixed Icecream X{}".format(how_many))
                        price.append(final_price)
                    else: 
                        print("Wrong selection has been entered... back to menu")
                elif food_size == "2":
                    if flavour == "1":
                        how_many = int(input("how many Medium Vanilla Icecream would you like? "))
                        final_price = float(10.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Medium Vanilla Icecream X{}".format(how_many))
                        price.append(final_price)
                    elif flavour == "2":
                        how_many = int(input("how many Medium Chocholate Icecream would you like? "))
                        final_price = float(10.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Medium Chocolate Icecream X{}".format(how_many))
                        price.append(final_price)
                    elif flavour == "3":
                        how_many = int(input("how many Medium Mixed Icecream would you like? "))
                        final_price = float(10.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Medium Mixed Icecream X{}".format(how_many))
                        price.append(final_price)
                    else: 
                        print("Wrong selection has been entered... back to menu")
                elif food_size == "3":
                    if flavour == "1":
                        how_many = int(input("how many Large Vanilla Icecream would you like? "))
                        final_price = float(15.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Large Vanilla Chocolate Icecream X{}".format(how_many))
                        price.append(final_price)
                    elif flavour == "2":
                        how_many = int(input("how many Large Chocolate Icecream would you like? "))
                        final_price = float(15.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Large Chocolate Icecream X{}".format(how_many))
                        price.append(final_price)
                    elif flavour == "3":
                        how_many = int(input("how many Large Mixed Icecream would you like? "))
                        final_price = float(15.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Large Mixed Icecream X{}".format(how_many))
                        price.append(final_price)
                    else: 
                        print("Wrong selection has been entered... back to menu")
                elif food_size == "0":
                    print("Back to the main menu")
            elif extras == "0":
                print("Let's go back")
            else:
                print("Wrong selection has been entered...back to menu")
        elif food_order == "6":    # When the sides option is selected
            side = input(" Menu: \n 1) Wing = R7 \n 2) Coleslaw = R10 \n 3) Mini Loaf = R5 \n 4) Mash = R10 \n 0) Back to menu \n : ")

            if side == "1":
                        how_many = int(input("how many side wing would you like? "))
                        final_price = float(7.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Side wing X{}".format(how_many))
                        price.append(final_price)
            elif side == "2":
                        how_many = int(input("how many side coleslaw would you like? "))
                        final_price = float(10.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Side coleslaw X{}".format(how_many))
                        price.append(final_price)
            elif side == "3":
                        how_many = int(input("how many side mini loaf would you like? "))
                        final_price = float(5.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Side mini loaf X{}".format(how_many))
                        price.append(final_price)
            elif side == "4":
                        how_many = int(input("how many side mash would you like? "))
                        final_price = float(10.00) * how_many
                        print("The price for what you've ordered is : R{}".format(final_price))
                        food.append("Side mash X{}".format(how_many))
                        price.append(final_price)
            elif side == "0":
                        print("Back to the main menu")
            else:
                print("Wrong selection has been entered...back to menu")
        elif food_order == "0":
            print("Back to the main menu")
        else:
            print("Wrong selection has been entered...back to menu")


    elif user == "2": # When the user wants to see the other outlets they can go to next time
        print(username + ", These are some of the outlets we currently have.")
        print(
            "JHB: \n Sandton 24th ivy road \n Sandton City three floor E3 \n Randburg 18th sweet road \nCPT: \n Somewest Ave road \n"
        )
        print("Do give us a visit, when you can.")


    elif user == "3":    # When the user wants to checkout with their order(s)
        print(username + ",These are your current orders: \n{} \n".format(food)) # Show the food orders the user has selected
        print(username + ", the total amount of everything is R{}".format(sum(price)))  # Show the price of the user's orders
        checkout = input(
            " would you like to checkout: \n 1) Checkout and pay \n 2) Go back and order more \n 3) Remove item from order \n 0) Back to main menu \n : "
        ) # Checkout menu

        if checkout == "1": # When the user is ready to pay for their order(s)
            print(
                "Good to goooooooo..." + username + " thank you for your supoort and enjoy your meal. Please pay at the till, come again 🙂"
            )
            break
        elif checkout == "2": # Going back to order some more food
            print("Okay, lets's go order some more...")
        elif checkout == "3":   # Remove item(s) you dont want in your list anymore
            print(food)
            item_remove = input("Please enter the number of where the item you want to remove is at: ")
            del food[int(item_remove) - 1] # Remove the item(s) in the food list
            del price[int(item_remove) - 1] # Remove the price of item(s) that's being removed
        elif checkout == "0":
            print("Back to the main menu") # Return to the main menu
        else:
            print("Wrong selection has been entered... back to the main menu")


    elif user == "4": # When the user wants to exit the program
        print("All orders placed are going to be canceled... if you wish to go through with the exit")
        exit = input("Would you like to go through with the exit: \n 1) Yes \n 2) No \n : ")  # Making sure that the user wants to exit

        if exit == "1": # When they select the exit option
            print("CANCELED")
            break
        elif exit == "2": # When they dont want to exit yet
            print("Okay let's go back...")

    else:
        print("Wrong selection has been entered. Please try again")  # When the user enters an invaild number
