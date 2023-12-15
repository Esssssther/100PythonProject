from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



menu1=Menu()
coffee_maker=CoffeeMaker()
off=1
money_machine= MoneyMachine()



while off != 0:

    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    # a. Check the user’s input to decide what to do next.
    options= menu1.get_items()
    user_choice = input(f"What would you like? {options}:")
    if user_choice == "off":
        off = 0
        # the machine. Your code should end execution when this happens.

        # TODO: 3. Print report.
        # a. When the user enters “report” to the prompt, a report should be generated that shows
    elif user_choice == "report":
            coffee_maker.report()
            money_machine.report()
    else:
        # print(drink)
        # TODO: 5. Process coins.
        # a. If there are sufficient resources to make the drink selected, then the program should

        # prompt the user to insert coins.
        # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
        # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
        drink= menu1.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        #if (coffee_maker.is_resource_sufficient(menu1.find_drink(user_choice))) is True:
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
        #    if money_machine.make_payment(menu1.find_drink(user_choice).cost) is True:
        #        coffee_maker.make_coffee(menu1.find_drink(user_choice))
