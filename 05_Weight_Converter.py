


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


for item in range (1, 10):

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

    if weight_type == "kg":
        print("Weight = {}".format(get_weight), weight_type)
        print()

    elif weight_type == "g":
        conv_weight = get_weight / 1000 
        print("Weight = {}".format(conv_weight), "kg")

    if weight_type == "L":
        print("Amount = {}".format(get_weight), weight_type)
        print()

    elif weight_type == "mL":
        conv_weight = get_weight / 1000 
        print("Amount = {}".format(conv_weight), "L")