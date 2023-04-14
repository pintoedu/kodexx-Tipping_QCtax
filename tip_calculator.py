# Eduardo Pinto - Tip Calculator Assignment - Concordia


# Created variable to get an int number of diners - no need for a float as this should be a whole number
while True:
    diners = input("How many diners today? > ")
# Created while loop to verify the int input using try and except to catch ValueError exceptions
    try:
        diners = int(diners)
        break
    except ValueError:
        print("Please enter a valid number.")

# Created variable to get a float number as we are fetching the cost of the meal (without taxes yet)
while True:
    cost_meal = input("What is the cost of all meals before taxes?: > ")
# Again, using try and except to catch ValueError exceptions for float values this time
    try:
        cost_meal = float(cost_meal)
        break
    except ValueError:
        print("Please enter a valid value.")

# While loop with an input to ask for tip amount with an if loops inside to fetch the selection and respective tip rates
while True:
    tip_selection = input("How much do you want to tip?\n 1) Exceptional 20% \n 2) Good 15% \n 3) Basic 10% \n 4) Horrible 0%\n > ")
    if tip_selection in ("1", "2", "3", "4"):
        tip_selection = int(tip_selection)
        if tip_selection == 1:
            tip_rate = 0.20
        elif tip_selection == 2:
            tip_rate = 0.15
        elif tip_selection == 3:
            tip_rate = 0.10
        else:
            tip_rate = 0.00

# Defined variables for all the calculations needed
        tip = cost_meal * tip_rate      # Tip amount without taxes
        qst = 0.09975 * cost_meal       # Quebec provincial tax calculation over the cost of the meal
        gst = 0.05 * cost_meal          # Federal tax calculation over the cost of the meal
        ttl = cost_meal + qst + gst     # Total calculation including taxes
        grand = ttl + tip               # Grand total including taxes and tips
        each = grand / diners           # The grand total each person will pay

# List of prints used to display all results asked
        print("\n************************ CALCULATION ************************")
        print(f"Number of diners:                                {diners}\n")
        print(f"Total price of all meals before tax:        CAD$ {cost_meal:.2f}")
        print(f"The provincial tax (QST) added is:          CAD$ {qst:.2f}")
        print(f"The federal tax (GST) added is:             CAD$ {gst:.2f}")
        print(f"The total including tax is:                 CAD$ {ttl:.2f}")
        print(f"The tip amount is:                          CAD$ {tip:.2f}\n")
        print(f"GRAND TOTAL:                                CAD$ {grand:.2f}")
        print(f"Each person pays:                           CAD$ {each:.2f}")
        print("**************************************************************")
# Break to exit loop while all the conditions are met
        break
# If somehow a value other than the selection 1 to 4  is made, the "else: print()" below will prompt to correct it
    else:
        print("Please, enter a valid option.")
