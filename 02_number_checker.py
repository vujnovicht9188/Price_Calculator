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

while 1 == 1:
    get_cost = num_check("What is your budget? $", "Please enter a number more than 0\n", float)
    print("your budget is ${}".format(get_cost))
    print()



