# import libraries
import math
import pandas
import time
import sys

# *** Functions go here ***

# checks that input is either float or integer that is more than zero.
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


# Ask user Yes/No question and make sure answer is valid
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

def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}.  \nPlease try again. \n".format(error))
            continue
    
        return response

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# Gets expenses, returns list which has the data frame and sub total
def get_expenses(var_fixed):
   
    # Set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list,
    }
    
    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        
        # get name, quantity and item
        item_name = not_blank("Item name: ", "The component name can't be blank.")
        if item_name.lower() == "xxx":
            break

        if item_name == "ihskt":
            def delay_print(text, delay):
                for i in text:
                    time.sleep(delay)
                    print(i, end='')
                    sys.stdout.flush()
                print()

            delay_print("Ylilo :p", 0.1)
            
            def print_slow(str):
                for letter in str:
                    print(letter)
                    time.sleep(.1)

            print_slow("pnk tils")

        if item_name == "toby":
            def delay_print(text, delay):
                for i in text:
                    time.sleep(delay)
                    print(i, end='')
                    sys.stdout.flush()
                print()
            
            delay_print("The Legend of Zelda is a high fantasy action-adventure video game franchise created by Japanese game designers Shigeru Miyamoto and Takashi Tezuka. Also a mid game series - jigachad *skull emoji x7", 0.01)
            
        if item_name == "pokemon":
            def delay_print(text, delay):
                for i in text:
                    time.sleep(delay)
                    print(i, end='')
                    sys.stdout.flush()
                print()

            delay_print("1. Treecko", 0.5)
            delay_print("2. Abra", 0.5)
            delay_print("3. Greninja", 0.5)
            delay_print("4. Beedrill", 0.5)
            delay_print("5. Sylveon", 0.5)
            
            
        if var_fixed == "variable":
            
            quantity = num_check("Quantity: ", "The amount must be a whole number more than zero", int)
        
        else:
            quantity = 1

        price = num_check("How much for a single item? $", "The price must be a number <more than zero>", float)

          # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    variable_frame = pandas.DataFrame(variable_dict)
    variable_frame = variable_frame.set_index('Item')

    # calculate cost of each component
    variable_frame['Cost'] = variable_frame['Quantity'] * variable_frame['Price']

    # Find sub total
    sub_total= variable_frame['Cost'].sum()

    # Currency fortmatting (uses currency function)
    add_dollars = ['Price' , 'Cost']
    for item in add_dollars:
        variable_frame[item] = variable_frame[item].apply(currency)

    return [variable_frame, sub_total]

# prints expense frame
def expense_print(heading, frame, subtotal):
    print()
    print("**** {} Costs ****".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))

# work out profit goal and total sales required
def profit_goal(total_costs):

    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask user for profit goal
        response = input("What is your profit goal? (eg $500 or 50%) ")

        # check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]
            
            # check if last charcter is %
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything after the %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue
        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f} ie {:.2f} dollars?, y / n ".format(amount, amount))

            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            dollar_type = yes_no("Do you mean ${:.2f} ie {:.2f} dollars?, y / n ".format(amount, amount))

            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"               

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal

# rounding function
def round_up(amount, var_round_to):
    return int(math.ceil(amount / var_round_to)) * var_round_to

# ***** Main Routine goes here *****

# ask user if they have used the program before
instructions = yes_no("Have you used this program before? ")
if instructions == "no":
    print()
    print("***** Instructions *****")
    print()
    print(""" This program will ask you for... 
    - The name of the product you are selling
    - How many items you plan on selling
    - The costs for each component of the product
    - How much money you want to make
    
    It will then output an itemised list of the costs with
    subtotals for the variable and fixed costs. Fianlly it
    will tell you how much you should sell each item for to
    reach your profit goal.
    
    The data will also be written to a text file which has
    the same name as your product""")


print()
print("**** Program Lauched :) ****")
print()   

# Get user data
company_name = not_blank("Company name: ", "The product name cannot be blank!")

how_many = num_check("How many items will you be producing ", "The number of items must be a whole number more than zero", int)

print()
print("Please enter your variable costs below...")
# get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs (y / n)? ")

if have_fixed == "yes":
# get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]
else:
    fixed_sub = 0
    fixed_frame = None

# work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# calculates total sales needed to reach goal
sales_needed = all_costs + profit_target

# ask for rounding
round_to = num_check("Round to nearest...? $", "Can't be zero", int)

# calculate recommended price
selling_price = sales_needed / how_many
print("Selling Price (unrounded): "
"${:.2f}".format(selling_price))

str_company_name = "**** Fund Raising - {} ****".format(company_name)
recommended_price = round_up(selling_price, round_to)
str_recommended_price = "Recommended Price ${:.2f}".format(recommended_price)
str_profit_target = "Profit Target: ${:.2f}".format(profit_target)
str_sales_needed = "Sales Needed: ${:.2f}".format(sales_needed)
str_total_costs = "**** Total Costs: ${:.2f} ****".format(all_costs)

# write data to file

# *** Printing Area ***

# print()
# print("**** Fund Raising - {} ****".format(company_name))
# print()
# expense_print("Variable", variable_frame, variable_sub)

# if have_fixed == "yes":
#     expense_print("Fixed", fixed_frame[['Cost']], fixed_sub)

# print()
# print("**** Total Costs: ${:.2f} ****".format(all_costs))
# print()

# print()
# print("**** Profit & Sales Targets ****")
# print("Profit Target: ${:.2f}".format(profit_target))
# print("Total Sales: ${:.2f}".format(all_costs + profit_target))

# print()
# print("**** Pricing ****")
# print("Minimum Price: ${:.2f}".format(selling_price))
# print("Recommended Price: {:.2f}".format(recommended_price))

# Change dataframe to string (so it can be written to a txt file)

company_name_txt = "/n***** {} ******".format(company_name)

variable_txt = pandas.DataFrame.to_string(variable_frame)

if have_fixed == "yes":
    fixed_txt = pandas.DataFrame.to_string(fixed_frame)
else: 
    fixed_txt = "There are no fixed costs"

# list holding stuff to print / write to file
to_write = [company_name_txt, '/n------ Variable Costs ------', variable_txt, '/n----- Fixed  Costs-----', fixed_txt, str_total_costs, '/n----- Sales Advice ------', str_profit_target, str_sales_needed, '\n', str_recommended_price]

# Write to file...
# Create file to hold data (add .txt extension)
file_name = "{}.txt".format(company_name)
text_file = open(file_name, "w+")

# heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()

# print stuff
for item in to_write:
    print(item)
    print()