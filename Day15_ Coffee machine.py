MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
off = 1
money = 0




# TODO: 4 Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
def check_resources_sufficient(order_ingredients):
    """
    returns True when order can be made, false if ingredients are insufficient
    """
    for key in order_ingredients:
        if order_ingredients[key] > resources[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True


def process_coins():
    """
        returns the total of the coins inserted
    """
    print("please insert coins.")
    total = int(input("How many quarters?"))*0.25
    total +=int(input("How many dimes?"))* 0.1
    total +=int(input("How many nickles?"))* 0.05
    total +=int(input("How many nickles?"))*0.01
    return total


def Check_transaction_successful(money_received, drink_cost):
    """
        returns true when the payment is accepted, false if money is insufficient
    """
    if money_received >= drink_cost:
        change = round(money_received-drink_cost,2)
        print(f"The money change is {change}.")
        global money
        money +=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

# TODO: 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
def make_coffe(drink_name, order_ingredients):
    """
    Deduct the required ingredients from resources
    """
    for key in order_ingredients:
        resources[key] -= order_ingredients[key]
    print(f"Here is your {drink_name} ☕️")


while off != 0:

    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    # a. Check the user’s input to decide what to do next.
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    # b. The prompt should show every time action has completed, e.g. once the drink is
    # dispensed. The prompt should show again to serve the next customer

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    if user_choice == "off":
        off = 0
    # the machine. Your code should end execution when this happens.

    # TODO: 3. Print report.
    # a. When the user enters “report” to the prompt, a report should be generated that shows
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}ml\n"
              f"Money: ${money}")
# option+shift, multi line editing
    else:
        drink = MENU[user_choice]
        #print(drink)
        # TODO: 5. Process coins.
        # a. If there are sufficient resources to make the drink selected, then the program should

        # prompt the user to insert coins.
        # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
        # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
        if check_resources_sufficient(drink["ingredients"]) is True:
            payment = process_coins()
            # TODO: 6. Check transaction successful?
            # a. Check that the user has inserted enough money to purchase the drink they selected.
            # E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
            # program should say “Sorry that's not enough money. Money refunded.”.
            # b. But if the user has inserted enough money, then the cost of the drink gets added to the
            # machine as the profit and this will be reflected the next time “report” is triggered. E.g.
            # Water: 100ml
            # Milk: 50ml
            # Coffee: 76g
            # Money: $2.5
            # c. If the user has inserted too much money, the machine should offer change.\
            # E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
            # places.
            if Check_transaction_successful(payment, drink["cost"]) is True:
                make_coffe(user_choice,drink["ingredients"])


