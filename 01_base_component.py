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

# Main Routine goes here
want_help = yes_no("Do want to read the instructions? ")
if want_help == "yes":
    print()
    print("***** Instructions *****")
    print()
    print("insert instructions here")
    print()
    
get_budget = num_check("What is your budget? $", "Please enter a number more than 0\n", float)
print("your budget is ${}".format(get_budget))