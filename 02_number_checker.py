def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response < 2:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main Routine goes here

while 1 == 1:
    get_cost = num_check("What is your budget? $", "Please enter a number more than or equal to $2.00\n", float)
    print("your budget is ${}".format(get_cost))
    print()



