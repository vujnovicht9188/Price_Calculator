import re
import pandas

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

# set up dictionaries and lists

item_list = []
weight_list = []
price_list = []
unit_cost_list = []

variable_dict = {
    "Item": item_list,
    "Weight": weight_list,
    "Price": price_list,
    "Unit Cost": unit_cost_list
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
   
    
    unit_type = "invalid"
    while unit_type != "valid":
        # ask user what measurement unit they want to use
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

    # convert g to kg
    if weight_type == "g":
        conv_weight = get_weight / 1000 
        print("Weight = {}".format(conv_weight), "kg")
    
    # convert mL to L
    elif weight_type == "mL":
        conv_weight = get_weight / 1000 
        print("Weight = {}".format(conv_weight), "L")
    
    else:
     print("Weight = {}".format(get_weight), weight_type)

    print()
    get_cost = num_check("How much does your item cost? $", "Please enter a number more than 0", float)

    # print("{}".format(desired_item))
    # print("{}".format(get_weight))
    # print("{}".format(get_cost))

    # calculate unit cost
    unit_cost = get_cost / conv_weight
   
    # round unit cost to 2dp
    r_unit_cost = (round(unit_cost, 2))
    print("Unit Cost: ${}".format(r_unit_cost))

# add item, weight, price and unit cost to lists
item_list.append(desired_item)
weight_list.append(conv_weight)
price_list.append(get_cost)
unit_cost_list.append(r_unit_cost)

variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('Item')

print(variable_frame)









        