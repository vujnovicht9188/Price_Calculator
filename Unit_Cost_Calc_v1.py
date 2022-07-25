import re
from urllib import response


def yes_no(question):

    to_check = ['yes', 'no']

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")

# number checker
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# **** Main Routine goes here ****

# set up dictionaries

price_comp_dict = {
    'Dark Elixir': 5.00,
    'Elixir': 2.50,
    'Gold': 2.50,
    'Crowns': 4.00,
    'Gems': 3.00,
    'Trophies': 3.50
}

weight_dict = {
    'Dark Elixir': 200,
    'Elixir': 180,
    'Gold': 250,
    'Crowns': 300,
    'Gems': 200,
    'Trophies': 350

}

want_help = yes_no("Do want to read the instructions? ")
if want_help == "yes":
    print()
    print("***** Instructions *****")
    print()
    print("insert instructions here")
    print()
    
# ask user for budget
print()
get_budget = num_check("What is your budget? $", "Please enter a number more than 0\n", float)

# confirm user budget
print("Your budget is ${}".format(get_budget))

# valid items holds list of all items
# Each item in valid snacks is a list with'
# valid options for each item <full name, letter code
# , and possible abbreviations etc>
valid_items = [
    ["dark elixir", "d", "de", "darkelixir"],
    ["elixir", "e"],
    ["gold", "gl" ],
    ["crowns", "crowns", "c",],
    ["trophies", "trophy", "t"],
    ["gems", "gem", "gm", "gms"],
    ["xxx"]
]

# initialise variables
item_ok = ""
item = ""

# loop three times to make testing quicker
for item in range(0, 14):

    item_valid = "valid"
    while item_valid != "valid":

    # ask user for desired item and put it in lowercase
        print()    
    print()
    desired_item = input("Item: ").lower()

    if desired_item == "xxx":
        break

    for var_list in valid_items:

        # if the item is in one of the lists, return the full name 
        if desired_item in var_list:

            # Get full name of item and put it 
            # in title case so it looks nice when outputted
            item = var_list[0].title()
            item_ok = "yes"
            break
    
        # if the chosen item is not valid, set item_ok to no
        else:
            item_ok = "no"
        
    # if the item is not OK - ask question again.'
    
    if item_ok == "yes":
        print()
        print("Item Choice:", item)
        print()
    else:
        print("Invalid choice")
        print()
        continue
    
    
    unit_type = "invalid"
    while unit_type != "valid":
        get_unit = input("What measuremnt unit would you like to use? (kg, g, mL, L): ")
        if get_unit == "g":
            weight_type ="g"
            unit_type = "valid"

        elif get_unit == "kg":
            weight_type = "kg"
            unit_type = "valid"
        
        elif get_unit == "mL" or get_unit == "ml":
            weight_type = "mL"
            unit_type = "valid"

        elif get_unit == "L" or get_unit == "l":
            weight_type = "L"
            unit_type = "valid"

        else:
            print("Error, please enter a valid unit type.")
            print()
            continue

    print()
    get_weight = num_check("What is the weight or amount of your item? ", "Error please enter valid number", float)
    print()

    if weight_type == "g":
        conv_weight = get_weight / 1000 
        print("Weight = {}".format(conv_weight), "kg")
    
    elif weight_type == "mL":
        conv_weight = get_weight / 1000 
        print("Weight = {}".format(conv_weight), "L")
    
    else:
     print("Weight = {}".format(get_weight), weight_type)

    

    

    