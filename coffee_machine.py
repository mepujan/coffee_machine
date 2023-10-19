from resources_needed import resources_required

# defining the initial resources available in coffee machine
initial_resources ={
    'water': 300,
    'milk': 200,
    'coffee': 20,
    'money': 0
}


# copying that initial resources to available resources for manipulation purpose
available_resources = initial_resources


# function that calculate the difference of available resources and required resources
def calculate_available_resource(coffee_type):
    '''Takes coffee_type as a parameter and returned the calculated water milk and coffee value'''

    water = available_resources.get('water') - resources_required.get(coffee_type).get('water')
    milk = available_resources.get('milk') - resources_required.get(coffee_type).get('milk')
    coffee = available_resources.get('coffee') - resources_required.get(coffee_type).get('coffee')
    return water,milk,coffee


# function that takes input from the user
def get_user_choice():
    ''' takes input from the user and returend the user choice to the program'''

    choices = ['espresso','latte','cappuccino','off','report']
    print("---------------------------------------------------------------")
    print("Note: Type 'off' to shut down the machine.")
    print("Note: Type 'report' to print the current resource value.")
    print("---------------------------------------------------------------")
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    while user_choice.lower() not in choices:
        print("Wrong Input. Try Again....")
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    return user_choice


# function that prints the current available resources
def print_report():
    print("-----------------------------------------------------")
    print("Current Resources Available")
    print("-----------------------------------------------------")
    print("Water: ", available_resources.get('water'),'ml')
    print("Milk: ", available_resources.get('milk'),'ml')
    print("Coffee: ",available_resources.get('coffee'),'gm')
    print("Money: $", available_resources.get('money'))


# function checks if required milk is available to make coffee or not
def check_milk(milk,min_value):
    ''' this function takes two parameters [milk] and [min_value] and returned boolean True or False
        @milk ->[float], current value of milk 
        @min_value ->[float], minimum value of milk required to make coffee
    '''
    if milk >= min_value:
        return True
    print("Not enough milk to make coffee")
    return False 

# function checks if required water is available to make coffee or not
def check_water(water,min_value):
    '''this function takes two parameters [water] and [min_value] and returned boolean True or False
        @water ->[float], current value of water
        @min_value ->[float], minimum value of milk required to make coffee
    '''
    if water >= min_value:
        return True
    print("Not enough water to make coffee")
    return False

# function checks if required coffee is available to make coffee or not
def check_coffee(coffee,min_value):
    '''this function takes two parameters [coffee] and [min_value] and returned boolean True or False
        @coffee ->[float], current value of water
        @min_value ->[float], minimum value of coffee required to make coffee
    '''
    if coffee >= min_value:
        return True
    print("Not enough coffee to make coffee")
    return False

# function checks whether the required resources are available to make coffee or not
def check_resources(coffee_type):
    ''' takes one parameter [coffee_type] and returns boolean true or false
        @coffee_type -> string  
    '''
    water = available_resources.get("water")
    milk= available_resources.get("milk")
    coffee= available_resources.get("coffee")

    if coffee_type == 'latte':
        have_milk = check_milk(milk,resources_required.get(coffee_type).get('milk'))
        have_water = check_water(water,resources_required.get(coffee_type).get('water'))
        have_coffee = check_coffee(coffee,resources_required.get(coffee_type).get('coffee'))
        if have_milk and have_coffee and have_water:
            return True
        return False
    elif coffee_type == 'cappuccino':
        have_milk = check_milk(milk,resources_required.get(coffee_type).get('milk'))
        have_water = check_water(water,resources_required.get(coffee_type).get('water'))
        have_coffee = check_coffee(coffee,resources_required.get(coffee_type).get('coffee'))
        if have_milk and have_coffee and have_water:
            return True
        return False
    else:
        have_water = check_water(water,resources_required.get(coffee_type).get('water'))
        have_coffee = check_coffee(coffee,resources_required.get(coffee_type).get('coffee'))
        if have_water and have_coffee:
            return True
        return False


# function that checks the transaction and resources and make coffee for the user
def make_coffee(coffee_type):
    if check_resources(coffee_type) and process_transaction(coffee_type):
        match coffee_type:
            case 'latte':
                water,milk,coffee = calculate_available_resource('latte')
            case 'espresso':
               water,milk,coffee = calculate_available_resource('espresso')
            case 'cappuccino':
                water,milk,coffee = calculate_available_resource('cappuccino')
            case _:
                print("Not Available")
        updated_resources = {
            "water":water,
            "milk":milk,
            "coffee":coffee
        }
        available_resources.update(updated_resources)
        print("Here is your ", coffee_type, ' enjoy...')
    

# function that handles the monetary transaction of coffee machine
def process_transaction(coffee_type):
    print("Pay: $",resources_required.get(coffee_type).get('price'))
    print("Insert Coins: ")
    dollar = float(input("Dollars: "))
    quarters = float(input("Quarters: "))
    dimes = float(input("Dimes: "))
    nickel = float(input("Nickle: "))
    pennies = float(input("Pennies: "))
    total_amount = dollar + 0.25 * quarters + 0.1 * dimes + 0.05 * nickel + 0.01 * pennies
    price = resources_required.get(coffee_type).get('price')
    print("You Paid: $", round(total_amount,2))
    match coffee_type:
        case 'latte':
            if check_price(price,total_amount):
                update_and_generate_change(total_amount,price)
            else:
                print("Sorry Thats not enough money. Money Refunded.")

        case 'espresso':
            if check_price(price,total_amount):
                update_and_generate_change(total_amount,price)
            else:
                print("Sorry Thats not enough money. Money Refunded.")
        case 'cappuccino':
            if check_price(price,total_amount):
               update_and_generate_change(total_amount,price)
            else:
                print("Sorry Thats not enough money. Money Refunded.")
    return True


# function that checks if amount paid is greater than price or not
def check_price(price,amount):
    ''' takes [price] and [amount] as a parameter and returns the boolean value.
        @price -> [float], price of coffee.
        @amount -> [float], amount paid by client
    '''
    if amount >= price:
        return True
    return False

# function that generate the change to the user and update the available resources
def update_and_generate_change(total_amount, price):
    '''takes [price] and [total_amount] as a parameter and updates the available resources and print changes.
        @price -> [float], price of coffee.
        @total_amount -> [float], amount paid by client
    '''
    available_amount = available_resources.get("money")
    if total_amount > available_amount:
        change = total_amount - price
        print("Here is your change: $", round(change,2))
    new_amount = available_amount + price
    available_resources['money'] = new_amount


# collection of all functions
def main():
    while True:
        user_choice = get_user_choice()
        if user_choice.lower() == 'report':
            print_report()
        elif user_choice.lower() == 'off':
            exit(0)
        else:
            make_coffee(user_choice)

# main program
if __name__ == "__main__":
    main()





